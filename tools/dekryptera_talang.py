from pathlib import Path
from getpass import getpass
from Crypto.Cipher import AES
import shutil
import os

ROOT = Path("/Volumes/LG-TV/LG Smart TV/lg_dvr")
OUTPUT = Path.home() / "LG-Talang-Backup"

RECORDINGS = [
    ("00000001REC", "Talang-2020-01-10.ts"),
    ("00000002REC", "Talang-2021-02-05.ts"),
]

print("LG Talang – dekryptering av inspelningar")
print("----------------------------------------")

key = bytes.fromhex(
    getpass("AES-nyckel (32 hextecken): ").strip()
)

if len(key) != 16:
    raise ValueError("Nyckeln måste vara exakt 16 byte.")

aes = AES.new(key, AES.MODE_ECB)

# Verifiera nyckeln med LG:s identifieringsfil.
dev = (ROOT / ".lg_dvr_dev").read_bytes()
identifier = aes.decrypt(dev[4:100])[:32]

if not (
    all(32 <= x <= 126 for x in identifier[:16])
    and identifier[16:] == bytes(16)
):
    raise ValueError("Nyckeln klarade inte identifieringstestet.")

print("Nyckel verifierad.")

jobs = []
total_output = 0

for folder, filename in RECORDINGS:
    directory = ROOT / folder
    segments = sorted(directory.glob("*STR"))

    if not segments:
        raise FileNotFoundError(
            f"Inga STR-segment hittades i {directory}"
        )

    sizes = [p.stat().st_size for p in segments]
    total_bytes = sum(sizes)

    if total_bytes % 192 != 0:
        raise ValueError(
            f"{folder}: total datastorlek är inte delbar med 192."
        )

    output = OUTPUT / filename
    temporary = OUTPUT / (filename + ".partial")

    if output.exists() or temporary.exists():
        raise FileExistsError(
            f"Utfil finns redan: {output} eller {temporary}"
        )

    expected = (total_bytes // 192) * 188
    total_output += expected
    jobs.append((folder, segments, output, temporary, expected))

    print(
        f"{folder}: {len(segments)} segment, "
        f"cirka {expected / 1073741824:.2f} GiB"
    )

free = shutil.disk_usage(OUTPUT).free

if free < total_output + 256 * 1048576:
    raise OSError(
        "Otillräckligt diskutrymme. "
        f"Behöver cirka {total_output / 1073741824:.2f} GiB."
    )

print(
    f"Ledigt diskutrymme: {free / 1073741824:.2f} GiB"
)
print()

def decrypt_packet(packet):
    if len(packet) != 192 or packet[4] != 0x47:
        raise ValueError("Ogiltigt 192-byte-paket.")

    result = bytearray(packet)
    mode = (packet[7] >> 4) & 3

    if mode == 2:
        start = 192
    elif mode == 3:
        start = 9 + packet[8]
    else:
        start = 8

    if start > 192:
        raise ValueError("Ogiltigt anpassningsfält.")

    end = start + ((192 - start) // 16) * 16

    if end > start:
        result[start:end] = aes.decrypt(packet[start:end])

    # Nollställ krypteringsflaggan.
    result[7] &= 0x3f

    # Ta bort LG:s fyra extra byte.
    return result[4:192]

for folder, segments, output, temporary, expected in jobs:
    print(f"Bearbetar {folder} ...", flush=True)

    packets = 0
    carry = b""

    with temporary.open("wb") as dst:
        for index, segment in enumerate(segments, 1):
            with segment.open("rb") as src:
                while True:
                    block = src.read(192 * 4096)
                    if not block:
                        break

                    data = carry + block
                    usable = (len(data) // 192) * 192
                    carry = data[usable:]

                    result = bytearray()
                    for offset in range(0, usable, 192):
                        result.extend(
                            decrypt_packet(data[offset:offset + 192])
                        )
                        packets += 1

                    dst.write(result)

            if index % 10 == 0 or index == len(segments):
                print(
                    f"  {index}/{len(segments)} segment",
                    flush=True
                )

    if carry:
        raise ValueError(
            f"{folder}: {len(carry)} ofullständiga slutbyte."
        )

    if temporary.stat().st_size != expected:
        raise ValueError("Felaktig storlek på resultatfilen.")

    os.replace(temporary, output)

    print(f"KLAR: {output.name}")
    print(f"  Paket: {packets:,}")
    print(
        f"  Storlek: {output.stat().st_size / 1073741824:.2f} GiB"
    )
    print()

print("BÅDA INSPELNINGARNA ÄR FÄRDIGBEARBETADE.")

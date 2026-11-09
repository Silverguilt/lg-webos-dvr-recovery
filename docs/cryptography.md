# Cryptography and packet structure

## How the mode was identified

Recovered discussion notes report Ghidra analysis of `DASY_AES_CipherInit`: mode 1 was selected without an IV, and `_DASY_AES_BlockCipherMode` used direct Rijndael decryption. Notes also report `_DASY_DEBUG_CheckIndexStream` following IDX-to-STR reads with `DASY_AES_Decrypt(..., 1, 0xc0)`. These observations supported the ECB hypothesis; a numeric mode value alone would not establish ECB.

The supplied working implementation explicitly uses `AES.new(key, AES.MODE_ECB)` and requires a 16-byte key, establishing AES-128-ECB as the implemented method. Device-identifier plausibility and subsequently reported VLC picture/audio provided practical corroboration for these two recordings. The original binary, disassembly and full experiment transcript are unavailable here; no unsuccessful mode tests or key-discovery procedure are reconstructed.

## 192-byte units

| Offset in stored unit | Length | Treatment |
| --- | --- | --- |
| 0–3 | 4 | LG prefix removed; meaning not established |
| 4 | 1 | MPEG-TS sync byte, expected `0x47` |
| 4–7 | 4 | TS header, retained except scrambling bits |
| 8 onward | Variable | Optional adaptation field, followed by payload |

The 192-byte layout consists of a four-byte prefix plus a 188-byte MPEG transport packet. Prior notes reported 100/100 sampled sync checks at the expected position. The supplied script enforces `packet[4] == 0x47` for every processed unit.

## Packet-aware decryption in the original script

Read adaptation-field-control from `(packet[7] >> 4) & 3`:

- `2`: adaptation only; no payload decryption (`start = 192`).
- `3`: adaptation plus payload; `start = 9 + packet[8]`.
- Otherwise: `start = 8`.

Decrypt only the largest whole number of 16-byte blocks from `start`: `end = start + ((192 - start) // 16) * 16`. Leave any shorter tail unchanged. Clear transport scrambling control with `result[7] &= 0x3f`, then output `[4:192]`.

This describes the verified case workflow, not a claim that all LG payloads use this rule. The script treats reserved adaptation control `0` like payload-only and does not condition decryption on scrambling control. These are known limitations, not behavior endorsed for arbitrary inputs. AES-ECB provides no authenticity or integrity guarantee.

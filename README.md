# LG webOS DVR Recovery

A case study in recovering two personally held TV recordings from an LG webOS DVR archive. This repository documents the reverse engineering, packet-aware AES decryption and verification used in that recovery.

**Status:** research case study; archival implementation with known limitations. No keys, recordings, firmware or LG binaries are included. Compatibility beyond the two recordings is unknown.

## Outcome

The original session reported successful recovery of both recordings and VLC playback with picture and sound. The supplied working script is preserved unchanged. The recordings and key are unavailable in this repository, so the recovery has not been rerun here. Playback is not evidence of a complete, error-free decode of every frame.

| Case | Original folder | Recording date | Reported STR segments |
| --- | --- | --- | --- |
| A | `00000001REC` | 2020-01-10 | 60 |
| B | `00000002REC` | 2021-02-05 | 51 |

These were Talang broadcasts on TV4. Personal ownership of a recording does not establish permission to redistribute its broadcast content.

## Repository guide

- [File formats](docs/file-formats.md): STR, IDX, PIF and device identifier observations.
- [Cryptography and packet layout](docs/cryptography.md): evidence for AES-128-ECB and the 192-byte structure.
- [Recovery procedure](docs/recovery.md): the working process and operational limitations.
- [Verification and evidence](docs/verification.md): what was checked, reported or remains unknown.
- [Publication review](docs/publication-review.md): release risks and outstanding decisions.
- [Security policy](SECURITY.md): handling secrets and private inputs.
- `tools/dekryptera_talang.py`: original project-written recovery script, reviewed for embedded secrets.

## Running the preserved script

Use Python 3 and PyCryptodome (`Crypto.Cipher.AES`). Install dependencies from `requirements.txt` in an isolated environment. Review the script before running it. Its Swedish prompts and original case-specific paths are preserved.

Edit `ROOT`, `OUTPUT` and `RECORDINGS` for a local copy of your own archive; create the output directory first. Run `python tools/dekryptera_talang.py` and enter the 32-hex-character key at the hidden prompt. Never put the key in shell arguments, source control or an issue.

The script is an archival implementation, not a hardened general-purpose parser. Read the procedure and limitations first. It does not obtain keys, access a TV, download firmware or modify the original archive.

## Scope and provenance

Documentation is based on the supplied script and recovered notes from the original conversation. Raw investigation logs and binaries are deliberately excluded. Recovered discussion summaries are labeled as such; absent details have not been reconstructed. No third-party implementation or decompiled LG source is included.

No redistribution license has been selected. Public visibility does not grant a general reuse license. LG, webOS and other names remain their respective owners' marks. This project is unaffiliated with LG.

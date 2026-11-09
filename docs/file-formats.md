# Observed DVR files

This is a case-specific description, not a complete LG format specification. Offsets are zero-based; Python slices exclude their end.

| File | Evidence and role | Limits |
| --- | --- | --- |
| `.STR` | Segmented recording data; the working script reads concatenated 192-byte units and emits 188-byte TS packets. | Segment naming/order is assumed lexicographic; no universal naming specification is established. |
| `.IDX` | Earlier metadata notes describe 32-byte records interpreted as eight little-endian uint32 values, with byte offsets aligned to 192 bytes. | Raw IDX is unavailable here; complete field order, units and semantics are not independently verified. Not consumed by the recovery script. |
| `.PIF` | Earlier notes describe STR/IDX segment pair references. Investigation reported a shared identifier block at offset `0x08`, matching `.lg_dvr_dev` from `0x04`. | Block length and full schema are not established by the supplied script. Not required by that script. |
| `.lg_dvr_dev` | Earlier investigation reported a 104-byte (`0x68`) file. The script decrypts bytes `[4:100]` (96 bytes). | Meanings of the first four and final four bytes are unknown. Never publish the actual file or identifier. |

## IDX interpretations from prior notes

Kinds were interpreted as `3` = I-frame, `4` = P-frame, `8` = B-frame, and `64` = checkpoint/coarse seek. These are historical interpretations, not a validated parser contract. No field map is supplied because the original raw records and analysis are not available in this review.

## Device identifier plausibility check

The script decrypts `.lg_dvr_dev[4:100]` with the entered key, then examines the first 32 decrypted bytes: the first 16 must be printable ASCII (`32..126`) and the next 16 must be zero. It does not expose the identifier. This is a plausibility check, not cryptographic authentication or a full format validator. The script does not explicitly enforce the reported 104-byte file length.

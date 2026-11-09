# Verification and evidence ledger

Evidence classes: **code** = directly inspectable in the supplied script; **reported** = recovered original-session notes/user confirmation; **unknown** = unavailable evidence. Documentation review is not a new recovery run.

| Claim | Evidence | Qualification |
| --- | --- | --- |
| Both recovered recordings played with picture and audio in VLC | Reported user confirmation from original session | No playback repeated here; full-duration viewing not established |
| 192-byte stored units and 188-byte output | Code; reported 100/100 sync sample | Original byte samples not included |
| AES-128-ECB | Code; reported reverse engineering | Key and binary excluded |
| Identifier plausibility test | Code | Not authenticated key verification |
| Segment carry-over, size checks and partial output | Code | Presence of checks does not supply original run counters |
| 60 and 51 STR segments | Reported investigation notes | Not recounted here |
| Sampled TS inspection | Prior notes mention 111,000 packets and scrambling control 1 throughout | Sampling scope/raw output not recovered; do not treat as whole-file statistics |
| Final success | User said everything worked | Exact final byte counts, checksums, codec details and decoder errors unavailable |
| ffprobe verification | Unknown/not established | User stated ffprobe was not installed during the discussion |

## Further verification before broader claims

Run a full TS continuity/PAT/PMT/PES audit and a complete audio/video decode on local outputs. If ffprobe/FFmpeg is later used, record its version and actual results; no such output is claimed in this repository. Check the beginning, middle, end, audio sync and seeks for each recording. Do not infer exact duration from metadata estimates.

## Review performed for this repository

The supplied source was inspected for embedded keys, SSH material, network access and LG binary/decompiled code. No embedded secret values were found. Its AES key is entered with `getpass`. The repository excludes raw investigation logs and media. Pre-commit checks passed: Python AST syntax parsing, relative Markdown link resolution, exact byte comparison of the archived script against the supplied source, and pattern checks for private-key headers, long hexadecimal values and common GitHub token prefixes. These pattern checks are not a dedicated secret scanner or a guarantee. No original media is available for an end-to-end rerun.

# Recovery procedure

1. Preserve the source archive and work from a local copy. Keep raw files, metadata and keys outside the repository.
2. Inventory the recording folders and STR segments. Confirm the intended order separately; the script uses `sorted(directory.glob("*STR"))`, not a PIF/IDX parser.
3. Review local paths and recording/output mappings in `tools/dekryptera_talang.py`. Create `OUTPUT` before running; `shutil.disk_usage(OUTPUT)` requires it to exist.
4. Supply the known 16-byte key through the hidden prompt. The script runs the device-identifier plausibility test before processing.
5. Preflight each recording: require segments, reject existing final or `.partial` files, require total length divisible by 192, and check free space for expected output plus 256 MiB.
6. Stream segments with carry-over across segment boundaries. Apply packet-aware AES decryption, clear scrambling bits and remove the prefix.
7. Require no trailing partial unit and an output size of `(total_input_bytes / 192) * 188`. Rename the `.partial` file to its final filename.
8. Inspect TS structure and test playback with both audio and video. Preserve any local verification report privately.

## Failure and recovery limitations

- The source archive is read only by the script; output is newly written.
- Failed runs can leave `.partial` files. Inspect and move them aside before retrying; there is no resume support.
- Disk checks are estimates, not reservations. Source changes during processing are not detected.
- The existence check plus `open("wb")` is not an atomic no-overwrite guarantee; `os.replace` can replace a concurrently created final file. Use a dedicated output directory with no concurrent writers.
- Malformed headers are only partly checked. There is no authentication, continuity-counter audit, PAT/PMT/PES validator or full decode test in the recovery script.
- The original paths and case names are retained for provenance. No dependency version from the successful run was recovered; the requirement is intentionally unpinned and not a reproducibility lockfile.

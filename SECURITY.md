# Security policy

Do not attach raw archives, keys, device identifiers, firmware, LG executables, memory dumps or connection transcripts to issues or pull requests.

The script accepts a key through a hidden interactive prompt. It does not log or persist it, but the key exists in process memory and is not securely erased. Run only on a trusted local machine. The device identifier check is heuristic and AES-ECB is unauthenticated.

`.gitignore` is an accident-prevention measure, not a security boundary. It does not protect already tracked files, history, forced additions, issue attachments or releases. Review the staged diff and full history before any visibility change. Keep real fixtures outside this checkout; use synthetic data for future tests.

If a credential is exposed, stop distribution and rotate/revoke it where possible; deleting a file in a later commit is insufficient. A device-bound AES secret may not be readily rotatable. Never post its value while reporting a problem.

Report sensitive findings privately to the repository owner through an established private channel. No dedicated vulnerability-reporting address has been configured. Do not use a public issue for secrets.

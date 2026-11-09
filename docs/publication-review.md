# Publication review

## Technical review — 2026-11-09

The owner requested public publication following review. The ten repository files and both pre-publication commits were inspected. The initial commit contains only README.md; the second adds the nine other reviewed files. Only main was returned by branch search. No embedded AES key, private SSH key, recording, firmware, LG binary or decompiled source was found. The project-written script is unchanged from the supplied source and asks for the key with getpass.

Detect-secrets 1.5.0 scanned all ten local files matching the fetched repository content and returned zero findings. Manual review and syntax/link checks supplement that scan; no scanner guarantees absence of secrets. The historical README is identical to the scanned pre-publication README. No raw data or binary fixtures are included.

## Legal scope remains unresolved

This is a technical/content review, not legal clearance. The [Swedish Copyright Act](https://www.riksdagen.se/sv/dokument-och-lagar/dokument/svensk-forfattningssamling/lag-1960729-om-upphovsratt-till-litterara-och_sfs-1960-729/), sections 52 c–e, distinguishes exclusions, circumvention and distribution of circumvention products/services. Section 52 d includes an exception concerning viewing/listening to a lawfully accessible copy; this does not establish that distributing a tool is permitted under 52 e. Section 52 c also includes exclusions, including cryptographic research. Applicability to this case has not been determined. No exception is claimed merely by describing the repository as research.

A keyless decryption implementation can be combined with unauthorized keys or media. Ownership of a TV or recording alone does not resolve publication rights, contractual restrictions or rules in other jurisdictions. The repository does not extract keys or exploit a TV, but that does not eliminate circumvention-distribution questions. Obtain qualified legal advice before relying on a right to distribute or use it.

## Release scope and limits

- The archival decryptor is included, with no embedded secret or vendor code.
- No general reuse license has been granted. Visibility and licensing are separate decisions.
- No claim of universal LG/webOS compatibility, full-file integrity or ffprobe validation is made.
- Playback success remains original-session user-reported evidence; no media recovery was rerun during this review.
- Parser hardening, synthetic fixtures, dependency pinning and a full decode audit remain future work if a supported tool is desired.
- Removing a file in a later commit does not remove it from public history or copies already made.

# Public-release review

## Decision for the initial repository

Private only. The original project-written decryption script contains no embedded key, private SSH material or vendor code. It is included as an archival implementation, with limitations documented. No firmware, binaries, decompiled source, recordings or raw metadata are included. No permissive license is granted yet.

## Specific risks of releasing the tool

A keyless tool still describes and implements a protection-removal method. Others may combine it with keys or media obtained without authorization. Publication can raise copyright, anti-circumvention, contractual and reverse-engineering questions that depend on jurisdiction, provenance and purpose. Owning a TV or making a recording does not by itself settle those questions. This is a release risk assessment, not a legal determination or a claim of a statutory exception.

The code itself does not extract keys or exploit a TV. Removing embedded secrets therefore reduces disclosure risk but does not resolve distribution rights or circumvention concerns. Operationally, it assumes this archive's encryption and ordering rules and could produce corrupt output on other variants.

## Before making public

- Obtain a qualified review of applicable law and any relevant agreements, including whether publishing the decryption implementation is appropriate.
- Confirm code authorship and rights, then choose an explicit license. Do not imply rights over LG code or broadcast content.
- Decide whether the public repository should include the decryptor or documentation only. Removing it only in a later commit leaves it in history; create an independently reviewed clean public history if withholding it.
- Review every commit, branch, tag, attachment and release for secrets and identifying metadata, with a dedicated secret scanner as well as manual review.
- Improve parser validation, ordering checks and output creation if offering a supported tool; test using synthetic fixtures and authorized local samples.
- Preserve the evidence distinction. Do not claim universal webOS compatibility, full-file integrity or ffprobe validation without new results.

This checklist is intentionally unresolved. The current review does not constitute legal clearance or production hardening.

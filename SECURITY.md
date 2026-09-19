# Security policy

## Scope

This repository is a reproducible research archive and analysis pipeline, not a network service. Security-relevant findings nevertheless include:

- credentials, API tokens, personal email addresses, machine-local paths or private handoff/strategy material committed to the public tree or history;
- workflow or dependency changes that allow untrusted code to run with elevated GitHub Actions permissions;
- analysis scripts that unexpectedly transmit local files, credentials or unpublished data;
- repository-boundary regressions that publish raw/local artifacts the project explicitly excludes.

Methodological disagreements, statistical interpretation, source criticism and ordinary research corrections should use normal issues or pull requests rather than the security channel.

## Reporting

Use GitHub private vulnerability reporting for security-sensitive findings. Do not attach credentials, personal records, unpublished case material or restricted third-party data to a public issue.

The latest `main` branch receives security fixes.

## Repository boundary

CI and gitleaks enforce the public-tree boundary. In particular, the repository should not contain:

- API credentials or private authentication material;
- machine-local absolute home paths;
- private agent/handoff/strategy notes;
- raw NetCDF/zip downloads excluded by `.gitignore`;
- personal mailbox identifiers in archived telemetry metadata.

A narrowly scoped gitleaks allowlist exists for the published Spelthorne Idox `keyVal` page locator documented in `documentation/construction_timeline_sources.md`; it is not a general secret-scanning exemption.

## Scientific dependencies

A dependency update can be security-relevant and methodologically relevant at the same time. Scientific-library upgrades are therefore reviewed against the reproducibility policy rather than auto-merged solely because installation succeeds.

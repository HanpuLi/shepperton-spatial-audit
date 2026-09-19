# Reproducibility and dependency policy

This repository contains a historical spatial/remote-sensing audit whose reported numerical results depend on versioned local inputs, fixed methodological choices, remote Google Earth Engine collections, and a pinned OpenStreetMap snapshot.

## Fixed evidence boundaries

- The Overpass query in `scripts/01_osm_extraction.ql` is pinned to `2026-03-03T00:00:00Z`.
- Google Earth Engine scripts identify the collections, regions and temporal splits used by the analysis.
- Exported telemetry and archived outputs are evidence for the reported results; they must not be silently regenerated from a different date, sensor collection or dependency stack.
- CI verifies that the tracked Python analysis stack still installs/imports and that repository/methodological boundaries remain intact. It does **not** prove that a new scientific-library version reproduces every archived number.

## Python environment

The supported environment is Python 3.10+ with the compatibility ranges in `requirements.txt`. These `~=` constraints are intentional reproducibility bounds rather than a signal that routine version upgrades should be merged automatically.

Routine Dependabot version-update pull requests for scientific Python libraries are disabled. Dependabot vulnerability alerts and security updates remain enabled at repository level.

## Reviewing a dependency upgrade

Before widening a scientific dependency range:

1. record the old and proposed package versions;
2. run all locally reproducible non-GEE stages;
3. rerun affected GEE/export-dependent analyses against the same saved inputs or re-export from the same named collections/time windows;
4. compare headline coefficients, p-values, sample sizes and figures with the archived baseline;
5. document any numerical drift in the pull request and update the methodological boundary if the result changes.

An import-only green CI run is necessary but not sufficient evidence for a scientific dependency upgrade.

## Remote-service caveat

Earth Engine and Overpass are external services. Even when the repository pins dates/collection IDs, provider-side catalogue corrections or processing changes may affect a future rerun. Preserve exported evidence and record service/library versions when regenerating publication-facing results.

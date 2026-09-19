# Contributing

This repository is an assessed spatial-audit and reproducibility project. Contributions should improve the reproducible measurement pipeline, documentation or robustness checks without changing the stated evidential scope by accident.

Before opening a pull request:

```sh
python3 -m compileall -q analysis scripts tools
python3 tools/check_repository.py
```

CI additionally installs the pinned-compatible analysis stack from `requirements.txt` and imports the core packages.

Repository boundaries are deliberate:

- keep the Overpass extraction date pinned unless a change explicitly documents a new snapshot;
- do not commit raw NetCDF downloads, zip archives, machine-local paths, private handoff/strategy notes or editor metadata;
- do not convert a non-significant/null result into a stronger claim in documentation;
- code that needs Google Earth Engine authentication should remain import/compile-safe without credentials in CI.

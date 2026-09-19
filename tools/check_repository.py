#!/usr/bin/env python3
from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tracked = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
errors: list[str] = []

private_name = re.compile(
    r"(^|/)(?:_agent_memory_snapshot_|_HANDOFF_STATE_|_PHD_SEED_FRAMING_|_ARGUMENT_ALIGNMENT_|"
    r"_CURRENT_STATE_SUMMARY_|_RIGOROUS_AUDIT_|_METHODOLOGY_|_OPUS_|"
    r"_PROJECT_MINDMAP_|walkthrough_TIER2_)"
)
for rel in tracked:
    if private_name.search(rel):
        errors.append(f"private strategy/handoff file is tracked: {rel}")
    if Path(rel).suffix.lower() in {".nc", ".zip"} or Path(rel).name == ".DS_Store":
        errors.append(f"raw/generated local artifact is tracked: {rel}")

home_markers = ("/" + "Users/", "/" + "home/")
for rel in tracked:
    path = ROOT / rel
    if path.suffix.lower() in {".pdf", ".pptx", ".png", ".jpg", ".jpeg", ".gif"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue
    if any(marker in text for marker in home_markers):
        errors.append(f"machine-local absolute home path in tracked text: {rel}")
    if rel.startswith("data/raw_telemetry/") and Path(rel).suffix.lower() == ".json":
        if re.search(r"[A-Za-z0-9._%+-]+@(gmail|outlook|hotmail|icloud)\.[A-Za-z]{2,}", text, re.I):
            errors.append(f"personal mailbox leaked in tracked telemetry metadata: {rel}")

query = (ROOT / "scripts/01_osm_extraction.ql").read_text()
snapshot = '[date:"2026-03-03T00:00:00Z"]'
if snapshot not in query:
    errors.append(f"OSM extraction snapshot must remain pinned to {snapshot}")

readme = (ROOT / "README.md").read_text()
for marker in ("Shepperton Spatial Audit:", "Scope statement.", "2021-06-01", "Longcross", "REPRODUCIBILITY.md", "v2026.09.19"):
    if marker not in readme:
        errors.append(f"README lost methodological boundary: {marker}")

repro = ROOT / "REPRODUCIBILITY.md"
if not repro.is_file():
    errors.append("missing REPRODUCIBILITY.md dependency/evidence boundary")

for required in ("VERSION", "CHANGELOG.md", "CITATION.cff", "REPRODUCIBILITY.md", "LICENSE"):
    if not (ROOT / required).is_file():
        errors.append(f"missing public release/reproducibility file: {required}")

citation = (ROOT / "CITATION.cff").read_text()
if "Shepperton Spatial Audit:" not in citation:
    errors.append("CITATION.cff title does not match the renamed repository")
version = (ROOT / "VERSION").read_text().strip() if (ROOT / "VERSION").exists() else None
if version != "2026.09.19":
    errors.append(f"unexpected release snapshot version: {version!r}")
if f'version: "{version}"' not in citation or 'date-released: "2026-09-19"' not in citation:
    errors.append("CITATION.cff release metadata does not match VERSION/release date")

if errors:
    raise SystemExit("\n".join(errors))
print(
    f"repository check: {len(tracked)} tracked files; "
    "private/raw boundaries clean; OSM snapshot and methodological anchors fixed"
)

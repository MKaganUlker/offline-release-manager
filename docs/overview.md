# Offline Release System – Overview

This project implements a **developer-controlled, offline-first release and launch system**
designed for environments where end users must not install, modify, or publish software.

The system enforces a strict separation between:
- **Release creation (developer only)**
- **Release consumption (end user only)**

End users can only run a launcher.  
They cannot drop files, modify versions, or publish releases.

---

## High-Level Concept

DEV publishes releases → Launcher imports & verifies → User runs app

All releases are:
- Immutable
- Versioned
- Integrity-checked
- Selected deterministically

---

## Roles & Responsibilities

### Developer
- Builds `app.exe`
- Publishes releases using `publish_release.py`
- Controls version metadata and release notes
- Ships the release bundle together with the launcher

### End User
- Runs the launcher
- Never creates or installs releases manually
- Never edits configuration or JSON files
- Never modifies executables

---

## Project Structure

### Developer Side

dev/
├─ publish_release.py
└─ release_input/
├─ app.exe
└─ release.json


The developer publishes releases by running a single script.

Output:

release_bundle/
├─ releases.json
└─ packages/
└─ app_<version>.zip

---

### Runtime (End User Side)

runtime/
├─ launcher.py
├─ bootstrap.py
├─ installer.py
├─ release_index.py
├─ verifier.py
├─ paths.py
└─ logger.py


The runtime:
- Imports the release bundle automatically
- Installs selected versions into a private cache
- Verifies integrity before execution
- Launches exactly one version

---

## Execution Flow

1. User runs the launcher
2. Runtime bootstraps the release bundle into user space
3. Available releases are loaded from `releases.json`
4. One release is selected deterministically
5. Cached versions are cleaned to avoid stale execution
6. Selected version is installed and verified
7. `app.exe` is launched

---

## Key Guarantees

- End users cannot publish releases
- Old versions cannot be executed silently
- Corrupted artifacts are never launched
- Only one version runs at a time
- No manual setup steps are required

---

## Intended Use Cases

- Offline or air-gapped systems
- Lab / industrial software
- Controlled internal tools
- Regulated environments

This system intentionally prioritizes **safety, determinism, and clarity**
over convenience or automation.


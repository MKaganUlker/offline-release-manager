# Offline Release System

A **developer-controlled, offline-first release and launch system**
for distributing and running versioned executables in controlled environments.
End users can execute approved software versions but **cannot install, modify, or publish releases**.

---

## Problem Statement

In environments such as laboratories, internal tooling, or regulated systems:

- Users must not install or update software manually
- Multiple application versions may need to coexist
- Rollback must be immediate and reliable
- Systems may operate without network access
- Human error must be actively prevented

This project addresses these constraints by enforcing a strict separation between:
- **Release creation** — performed exclusively by developers
- **Release execution** — performed exclusively through a controlled launcher

---

## Design Principles

- End users interact only with a launcher
- Developers are the sole publishers of releases
- All releases are immutable and explicitly versioned
- Executables are integrity-verified before launch
- Stale or unintended versions cannot execute silently

---

## Repository Layout

- dev/ Developer-only release tooling
- runtime/ End-user launcher runtime
- release_bundle/ Published release artifacts (generated, read-only)
- docs/ System design and behavior documentation


---

## Developer Workflow

1. Place the final executable at:

- dev/release_input/app.exe


3. Publish the release:

```bash
python dev/publish_release.py

This generates a release bundle:

release_bundle/
├─ releases.json
└─ packages/
   └─ app_<version>.zip

The resulting bundle is distributed together with the launcher.


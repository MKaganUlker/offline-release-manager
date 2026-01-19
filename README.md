# Offline Release System

A **developer-controlled, offline-first release and launcher system**
designed to safely distribute and run versioned executables
without giving end users any ability to install or modify software.

---

## Problem This Solves

In many environments (labs, internal tools, regulated systems):

- Users must not install software
- Multiple versions may need to coexist
- Rollback must be safe and immediate
- Systems may be fully offline
- Human error must be minimized

This project solves those problems by separating:
- **Release creation** (developer only)
- **Release execution** (launcher only)

---

## Core Principles

- End users only run a launcher
- Developers are the only publishers
- Releases are immutable and versioned
- Integrity is verified before execution
- Old or stale versions cannot run silently

---

## Repository Structure

dev/ Developer-only release tooling
runtime/ End-user launcher runtime
release_bundle/ Published releases (read-only)
docs/ Design and behavior documentation

---

## Developer Workflow

1. Place the final executable in:

dev/release_input/app.exe


2. Edit release metadata:


3. Publish the release:

```bash
python dev/publish_release.py

release_bundle/
├─ releases.json
└─ packages/
   └─ app_<version>.zip

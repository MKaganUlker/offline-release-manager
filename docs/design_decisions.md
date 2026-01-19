# Design Decisions

This document records key architectural decisions and their rationale.

---

## Launcher-Based Architecture

**Decision**
Use a stable launcher to control application execution.

**Rationale**
- Enables version coexistence
- Prevents in-place upgrades
- Simplifies rollback

---

## Offline-First Constraint

**Decision**
No runtime network access.

**Rationale**
- Supports air-gapped environments
- Eliminates update-related uncertainty
- Reduces operational dependencies

---

## Immutable Version Storage

**Decision**
Installed versions are never modified.

**Rationale**
- Enables safe rollback
- Simplifies auditing
- Prevents state drift

---

## Manifest-Driven Policy

**Decision**
Externalize version selection rules into a manifest file.

**Rationale**
- Human-readable
- Offline-editable
- Decouples policy from code

---

## No Silent Fallbacks

**Decision**
Abort execution on ambiguity or failure.

**Rationale**
- Prevents undefined behavior
- Encourages explicit resolution
- Aligns with safety-critical practices

---

## Minimal Dependency Footprint

**Decision**
Use standard library where possible.

**Rationale**
- Easier packaging
- Lower maintenance
- Reduced attack surface

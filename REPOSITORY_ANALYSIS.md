# Repository Analysis Journal

This document tracks ongoing architectural reviews of the rhiza-core repository.

---

## 2026-02-22 — Analysis Entry

### Summary
Rhiza-core is a template framework repository providing language-agnostic infrastructure for project templates (Python, Go, etc.). The codebase is modular, well-documented, and follows a clean separation of concerns. It provides shared Makefile infrastructure, GitHub Actions workflows, and documentation templates. The repository demonstrates mature design patterns with a clear inheritance model for downstream language-specific templates. Recent commits show active migration away from GitLab CI toward GitHub Actions and cleanup of Python-specific components.

### Strengths
- **Clear architectural separation**: Language-agnostic core (`.rhiza/make.d/*.mk`, 448 total lines) cleanly separated from language-specific concerns through template bundle system (`.rhiza/template-bundles.yml`).
- **Comprehensive documentation**: 19 markdown files totaling ~5600 lines covering architecture, customization, template development, dependencies, and more (`docs/ARCHITECTURE.md`, `docs/TEMPLATE_DEVELOPMENT.md`, `docs/EXTENDING_RHIZA.md`).
- **Modular Makefile design**: 8 standalone makefiles for distinct concerns: agentic workflows (71 lines), book generation (129 lines), docker (31 lines), GitHub CLI (70 lines), LFS (76 lines), releasing (50 lines), plus custom hooks.
- **AI-first development**: Built-in support for GitHub Copilot and Claude Code agents (`.rhiza/make.d/agentic.mk`, `.github/agents/`, `.github/hooks/hooks.json`) with session lifecycle management.
- **Template bundle system**: Well-defined bundle architecture allowing fine-grained inheritance (core, github, docker, lfs, legal, renovate, book, release bundles in `template-bundles.yml`).
- **Hook-based extensibility**: Pre/post hooks for install, sync, validate, bump, release operations using double-colon Make syntax (`rhiza.mk` lines 83-88).
- **Consistent automation**: Renovate integration, GitHub Actions workflows for validation and sync, quality gates via session hooks.
- **Version management**: Single source of truth for rhiza version (`.rhiza/.rhiza-version` = 0.11.0) and Python version (`.python-version` = 3.13).

### Weaknesses
- **No source code**: Repository contains only infrastructure templates—no implementation code. This makes it difficult to assess correctness or test coverage of the framework itself beyond Makefile syntax.
- **Missing pyproject.toml**: Despite being a Python-ecosystem tool, rhiza-core itself has no `pyproject.toml` (removed in recent commits per git diff). This creates ambiguity about how to run/test the framework locally.
- **Sparse testing**: `.rhiza/tests` directory not found. `rhiza-test` target in `rhiza.mk` (line 113) warns if tests are missing but provides no baseline test suite.
- **No CI for core workflows**: While validation workflows exist for downstream templates, rhiza-core's own Makefiles lack direct unit or integration tests. Relies on downstream template usage for validation.
- **Template materialization not self-contained**: Depends on external `rhiza>=0.11.0` PyPI package via `uvx` for core operations (sync, validate, materialize). No vendored fallback if package unavailable.
- **Incomplete migration**: Recent commits show removal of `.gitlab-ci.yml` and `.gitlab/` (3000+ lines deleted per git diff). Migration to GitHub Actions appears recent; potential for incomplete edge cases.
- **Stale branches**: Multiple patch branches (`origin/tschm-patch-10` through `origin/tschm-patch-14`, `origin/tschm-patch13`) suggest incomplete cleanup of merged work.

### Risks / Technical Debt
- **External dependency fragility**: Core functionality relies on `uvx` installing `rhiza>=0.11.0` from PyPI. Network issues, package unavailability, or version mismatches could break all downstream templates.
- **No schema validation for bundles**: `template-bundles.yml` defines bundle structure but lacks formal schema validation. Typos or structural errors would fail silently or at runtime.
- **Session hook robustness**: `.github/hooks/session-start.sh` and `session-end.sh` referenced in `hooks.json` but not examined. Failure modes (timeouts, missing binaries) could degrade agent experience.
- **Documentation-code drift**: Extensive documentation (5600 lines) with no automated checks for outdated examples or broken references. Architecture diagrams in `ARCHITECTURE.md` use hardcoded line counts that may drift.
- **No versioning strategy for bundles**: `template-bundles.yml` has `version: "0.1.0"` but no documented upgrade path or backward compatibility guarantees for bundle schema changes.
- **Make target explosion**: 8 `.mk` files with custom hooks and optional includes (`local.mk`, `.rhiza/make.d/*.mk`) create complex dependency graphs. No visualization or conflict detection.
- **Missing examples**: No example repository or reference implementation demonstrating complete template inheritance flow from rhiza-core to language-specific template to end-user project.

### Score
**7/10** — Solid, production-ready foundation with minor concerns.

**Rationale**: 
- Strong architectural design and documentation (+2)
- Modular, extensible infrastructure suitable for multi-language templates (+2)
- AI-first tooling and automation workflows (+1)
- Active maintenance with thoughtful migrations (+1)
- Lacks self-contained tests and has external dependency risks (-2)
- Documentation-code synchronization not automated (-1)
- No reference implementation or schema validation (-1)

The repository demonstrates excellent infrastructure design patterns but falls short of exemplary due to testing gaps and external dependencies that could impact reliability. Suitable for production use with understanding of its constraints.

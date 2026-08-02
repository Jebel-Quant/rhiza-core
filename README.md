<div align="center">

# <img src=".rhiza/assets/rhiza-logo.svg" alt="Rhiza Logo" width="30" style="vertical-align: middle;"> Rhiza Core

[![Status: retired](https://img.shields.io/badge/status-retired-lightgrey)](#-this-repository-is-retired)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Successor: jebel-quant/rhiza](https://img.shields.io/badge/successor-jebel--quant%2Frhiza-2FA4A9)](https://github.com/jebel-quant/rhiza)

In the original Greek, spelt **ῥίζα**, pronounced *ree-ZAH*, and having the literal meaning **root**.

</div>

## ⚠️ This repository is retired

**`rhiza-core` is no longer maintained and will be archived.**

It was created to become a language-agnostic foundation that the language-specific
templates — `jebel-quant/rhiza` (Python) and `jebel-quant/rhiza-go` (Go) — would inherit
from. That three-tier model was never completed. Instead, **Python, Go and Rust support
was consolidated directly into [`jebel-quant/rhiza`](https://github.com/jebel-quant/rhiza)**,
which is now the single template repository.

### What this means for you

| If you… | Do this |
|---|---|
| Want to use Rhiza in a project | Point `.rhiza/template.yml` at `jebel-quant/rhiza` |
| Already use Rhiza | Nothing — no repository ever pinned `rhiza-core`, and it published no releases |
| Are looking for a file that used to be here | Check `jebel-quant/rhiza`, or this repository's git history |

Nothing depends on this repository: it has no releases, no forks, and no consumer
declares it as an upstream template. Removing it breaks nothing.

### What was removed on the way out

The Marimo, book, presentation, Docker, DevContainer, Git LFS and tutorial subsystems
have been deleted, along with their Makefile modules, workflows, tests and template
bundles. What remains is the core: the Makefile API, GitHub Actions CI, and the test
suite — enough for the repository to stay internally consistent and green until it is
archived. All of it remains in git history.

---

## 🌟 What Rhiza is

**Unlike traditional project templates** (like cookiecutter or copier) that generate a
one-time snapshot of configuration files, **Rhiza provides living templates** that evolve
with your project. Classic templates help you start a project, but once generated, your
configuration drifts away from the template as best practices change. Rhiza takes a
different approach: it enables **continuous synchronization**, allowing you to selectively
pull template updates into your project over time through automated workflows. This means
you can benefit from improvements to CI/CD workflows, linting rules, and development
tooling without manually tracking upstream changes.

### How It Works

Rhiza uses a simple configuration file (`.rhiza/template.yml`) to control which templates
sync to your project:

```yaml
# .rhiza/template.yml
repository: jebel-quant/rhiza
ref: v1.2.5

include: |
  .github/workflows/*.yml
  .pre-commit-config.yaml
  ruff.toml
  pytest.ini
  Makefile

exclude: |
  .rhiza/customisations/*
```

**What you're seeing:**
- **`repository`** - The upstream template source (**can be any repository, not just Rhiza!**)
- **`ref`** - Which version tag/branch to sync from (e.g., `v1.2.5` or `main`)
- **`include`** - File patterns to pull from the template (CI workflows, linting configs, etc.)
- **`exclude`** - Paths to skip, protecting your customisations

> **💡 Automated Updates:** When using a version tag (e.g., `v1.2.5`) instead of a branch
> name, Renovate will automatically create pull requests to update the `ref` field when new
> versions are released. To enable this in your project, copy the
> [`customManagers` configuration](renovate.json) from this repository's `renovate.json`
> into your own Renovate configuration.

When you run `uvx rhiza materialize` or trigger the automated sync workflow, Rhiza fetches
only the files matching your `include` patterns, skips anything in `exclude`, and creates a
clean diff for you to review. You stay in control of what updates and when.

## 🚀 Quick Start

Use [`jebel-quant/rhiza`](https://github.com/jebel-quant/rhiza), not this repository:

```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialise Rhiza configuration
uvx rhiza init

# Edit .rhiza/template.yml — point `repository` at jebel-quant/rhiza
# Then materialize the templates
uvx rhiza materialize
```

## ✨ What remains here

### Templates

#### 🌱 Core Project Configuration
- **.gitignore** - Sensible defaults for Python projects
- **.editorconfig** - Editor configuration to enforce consistent coding standards
- **ruff.toml** - Configuration for the Ruff linter and formatter
- **pytest.ini** - Configuration for the `pytest` testing framework
- **Makefile** - Task automation for common development workflows
- **CODE_OF_CONDUCT.md** - Code of conduct for open-source projects
- **CONTRIBUTING.md** - Contributing guidelines

#### 🔧 Developer Experience
- **.pre-commit-config.yaml** - Pre-commit hooks for code quality
- **.rhiza/completions/** - Bash and Zsh completion for make targets

#### 🚀 CI/CD & Automation
- **.github/** - GitHub Actions workflows for CI, pre-commit, deptry, security, CodeQL,
  release, sync and validation

### Template Bundles

`.rhiza/template-bundles.yml` defines five bundles: `core`, `github`, `tests`, `renovate`
and `legal`.

## 📋 Available Tasks

The project uses a [Makefile](Makefile) as the primary entry point for all tasks, powered
by [uv](https://github.com/astral-sh/uv) for fast Python package management.

### Key Commands

```bash
make install         # Install dependencies and setup environment
make test            # Run test suite with coverage
make fmt             # Format and lint code
make sync            # Sync with template repository
make release         # Create and publish a new release
make docs            # Generate API documentation with pdoc
```

Run `make help` for a complete list of available targets.

<details>
<summary>Show all available targets</summary>

```makefile
  ____  _     _
 |  _ \| |__ (_)______ _
 | |_) | '_ \| |_  / _\`|
 |  _ <| | | | |/ / (_| |
 |_| \_\_| |_|_/___\__,_|

Usage:
  make <target>

Targets:

Rhiza Workflows
  sync                  sync with template repository as defined in .rhiza/template.yml
  summarise-sync        summarise differences created by sync with template repository
  rhiza-test            run rhiza's own tests (if any)
  validate              validate project structure against template repository as defined in .rhiza/template.yml
  readme                update README.md with current Makefile help output

Meta
  help                  Display this help message
  version-matrix        Emit the list of supported Python versions from pyproject.toml

Agentic Workflows
  copilot               open interactive prompt for copilot
  claude                open interactive prompt for claude code
  install-copilot       checks for copilot and prompts to install
  install-claude        checks for claude and prompts to install

Bootstrap
  install-uv            ensure uv/uvx is installed
  install               install
  clean                 Clean project artifacts and stale local branches

Custom Tasks
  hello-rhiza           a custom greeting task
  post-install          run custom logic after core install

Documentation
  docs                  create documentation with pdoc
  mkdocs-build          build MkDocs documentation site
  mkdocs-serve          serve MkDocs site with live reload
  mkdocs                alias for mkdocs-serve

GitHub Helpers
  gh-install            check for gh cli existence and install extensions
  view-prs              list open pull requests
  view-issues           list open issues
  failed-workflows      list recent failing workflow runs
  whoami                check github auth status
  workflow-status       show recent runs for the release workflow
  latest-release        show information about the latest GitHub release

Quality and Formatting
  all                   run all CI targets locally
  deptry                Run deptry
  fmt                   check the pre-commit hooks and the linting

Releasing and Versioning
  bump                  bump version of the project (supports DRY_RUN=1)
  release               create tag and push to remote repository triggering release workflow (supports DRY_RUN=1)
  publish               bump version, create tag and push in one step (supports DRY_RUN=1)
  release-status        show release workflow status and latest release information

Development and Testing
  test                  run all tests
  typecheck             run ty type checking
  security              run security scans (pip-audit and bandit)
  docs-coverage         check documentation coverage with interrogate
  hypothesis-test       run property-based tests with Hypothesis
```

</details>

> **Note:** The help output is automatically generated from the Makefile.
> When you modify Makefile targets, run `make readme` to update this section,
> or the pre-commit hook will update it automatically.

## 🎯 Advanced Topics

### Documentation Examples

README code blocks can be tested when tests are configured.

```python
# Example code block
import math
print("Hello, World!")
print(1 + 1)
print(round(math.pi, 2))
print(round(math.cos(math.pi/4.0), 2))
```

```result
Hello, World!
2
3.14
0.71
```

### Python Version Management

The `.python-version` file specifies the default Python version for local development.
Tools like `uv` and `pyenv` automatically use this version. Simply update this file to
change your local Python version.

### Makefile Customisation

Rhiza uses a modular Makefile system with extension points (hooks) for customisation. See
[.rhiza/make.d/README.md](.rhiza/make.d/README.md) for the complete guide including:
- Extension points and hooks
- Custom target creation
- Module ordering conventions

### Private GitHub Packages

Rhiza's template workflows automatically support private GitHub packages from the same
organization. Simply add them to your `pyproject.toml`:

```toml
[tool.uv.sources]
my-package = { git = "https://github.com/jebel-quant/my-package.git", rev = "v1.0.0" }
```

**Git authentication is already configured** in all Rhiza workflows (CI, release, etc.)
using the default `GITHUB_TOKEN`, which automatically provides read access to repositories
in the same organization.

## 🛠️ Contributing

This repository is retired and accepts no further contributions. Please contribute to
[`jebel-quant/rhiza`](https://github.com/jebel-quant/rhiza) instead. See
[CONTRIBUTING.md](CONTRIBUTING.md) for the general guidelines that repository follows.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [GitHub Actions](https://github.com/features/actions) - For CI/CD capabilities
- [UV](https://github.com/astral-sh/uv) - For fast Python package operations
- [Ruff](https://github.com/astral-sh/ruff) - For Python linting and formatting

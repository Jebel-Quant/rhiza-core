<div align="center">

# <img src=".rhiza/assets/rhiza-logo.svg" alt="Rhiza Logo" width="30" style="vertical-align: middle;"> Rhiza Core

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/jebel-quant/rhiza-core)

# Strong roots
The foundational layer for language-agnostic Rhiza templates.

A collection of shared, reusable configuration templates and infrastructure
that powers modern project templates across multiple programming languages.

![Last Updated](https://img.shields.io/github/last-commit/jebel-quant/rhiza-core/main?label=Last%20updated&color=blue)

In the original Greek, spelt **ῥίζα**, pronounced *ree-ZAH*, and having the literal meaning **root**.

</div>

## 🌟 Why Rhiza Core?

**Rhiza Core** is the foundational layer that powers language-specific Rhiza templates. Instead of duplicating common infrastructure across [rhiza](https://github.com/Jebel-Quant/rhiza) (Python), [rhiza-go](https://github.com/Jebel-Quant/rhiza-go) (Go), and future language templates, Rhiza Core provides:

- **Shared Makefile Infrastructure** - Language-agnostic build automation
- **GitHub Actions Workflows** - CI/CD templates that work across languages
- **Development Tools** - Common developer experience configurations
- **Release Automation** - Version management and release workflows
- **Documentation Templates** - Standardized project documentation

Language-specific templates inherit from Rhiza Core and add their own language-specific tooling (like `uv` for Python or `go` toolchain for Go). This separation enables:

- **Consistency** across all language templates
- **Reduced duplication** of common infrastructure
- **Centralized improvements** that benefit all language templates
- **Faster template development** for new languages

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Rhiza Core                             │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Language-Agnostic Components                        │   │
│  │  • Makefile infrastructure (.rhiza/make.d/)          │   │
│  │  • GitHub Actions workflows (.github/workflows/)     │   │
│  │  • Development configs (.editorconfig, etc.)         │   │
│  │  • Documentation templates                           │   │
│  │  • Release automation scripts                        │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ inherits from
                  ┌───────────┴───────────┐
                  │                       │
      ┌───────────▼──────────┐ ┌─────────▼──────────┐
      │    rhiza (Python)    │ │   rhiza-go (Go)    │
      │  ┌────────────────┐  │ │  ┌──────────────┐  │
      │  │ Python-specific│  │ │  │ Go-specific  │  │
      │  │ • uv/pip       │  │ │  │ • go tooling │  │
      │  │ • ruff/pytest  │  │ │  │ • golangci   │  │
      │  │ • pdoc         │  │ │  │ • goreleaser │  │
      │  └────────────────┘  │ │  └──────────────┘  │
      └──────────────────────┘ └────────────────────┘
```

### How It Works

Rhiza uses a simple configuration file (`.rhiza/template.yml`) to control which templates sync to your project:

```yaml
# .rhiza/template.yml
repository: Jebel-Quant/rhiza-core
ref: v0.1.0

include: |
  .rhiza/make.d/github.mk
  .rhiza/make.d/docker.mk
  .github/workflows/*.yml
  .editorconfig
  
exclude: |
  .rhiza/scripts/customisations/*
```

**What you're seeing:**
- **`repository`** - The upstream template source (rhiza-core for shared components)
- **`ref`** - Which version tag/branch to sync from (e.g., `v0.1.0` or `main`)
- **`include`** - File patterns to pull from the template
- **`exclude`** - Paths to skip, protecting your customisations

## 📚 Table of Contents

- [Why Rhiza Core?](#-why-rhiza-core)
- [Architecture](#architecture)
- [What's Included](#-whats-included)
- [For Template Developers](#-for-template-developers)
- [For End Users](#-for-end-users)
- [Available Components](#-available-components)
- [Contributing](#-contributing)

## ✨ What's Included

Rhiza Core provides the following language-agnostic components:

### Makefile Infrastructure (`.rhiza/make.d/`)

Modular Makefile fragments that compose together:
- **`agentic.mk`** - AI agent workflows (GitHub Copilot, Claude)
- **`github.mk`** - GitHub CLI helpers (PRs, issues, workflows)
- **`lfs.mk`** - Git LFS support
- **`docker.mk`** - Docker build and run targets
- **`custom-env.mk`** - Environment variable customization
- **`custom-task.mk`** - Custom task hooks
- **`releasing.mk`** - Release automation framework
- **`book.mk`** - Documentation book building (via minibook)

### Configuration Files

Universal editor and project settings:
- **`.editorconfig`** - Cross-editor formatting rules
- **`CODE_OF_CONDUCT.md`** - Community guidelines
- **`CONTRIBUTING.md`** - Contribution guidelines
- **`LICENSE`** - MIT License
- **Core `.gitignore`** - Common ignore patterns

### GitHub Actions Workflows

CI/CD templates (in `.github/workflows/`):
- Template sync automation
- Validation workflows
- Release workflows (base)
- Pre-commit check workflows

### Documentation Templates

- README structure and examples
- Integration guides
- Customization documentation

## 🔧 For Template Developers

If you're creating a new language-specific Rhiza template (like `rhiza-rust` or `rhiza-typescript`):

1. **Create your language template repository**
   ```bash
   # Create new repo based on rhiza-core structure
   git clone https://github.com/Jebel-Quant/rhiza-core.git rhiza-<language>
   cd rhiza-<language>
   ```

2. **Configure to inherit from rhiza-core**
   
   Create `.rhiza/template.yml`:
   ```yaml
   repository: Jebel-Quant/rhiza-core
   ref: v0.1.0
   
   templates:
     - core
     - github
     - docker
   ```

3. **Add language-specific components**
   - Package manager integration
   - Language-specific linters/formatters
   - Testing frameworks
   - Build tooling

4. **Customize the bootstrap process**
   
   Override `.rhiza/make.d/bootstrap.mk` with language-specific setup

See [docs/TEMPLATE_DEVELOPMENT.md](docs/TEMPLATE_DEVELOPMENT.md) for detailed guidance.

## 👤 For End Users

If you want to use Rhiza templates in your project:

1. **Choose your language template:**
   - Python: [rhiza](https://github.com/Jebel-Quant/rhiza)
   - Go: [rhiza-go](https://github.com/Jebel-Quant/rhiza-go)

2. **Follow the language-specific quickstart guide**

You typically won't need to reference rhiza-core directly unless you're building custom templates or contributing improvements.

## 📋 Available Components

The project uses a modular Makefile system with language-agnostic targets. Language-specific templates inherit these and add their own tooling.

### Core Make Targets (`.rhiza/make.d/`)

```bash
# GitHub helpers
make view-prs              # List open pull requests
make view-issues           # List open issues
make failed-workflows      # Show recent CI failures
make whoami                # Check GitHub auth status

# AI Agent workflows
make analyse-repo          # Run repository analyzer
make summarise-changes     # Summarize changes since last release

# Docker support
make docker-build          # Build Docker image
make docker-run            # Run Docker container

# Documentation
make book                  # Build documentation book

# Release automation
make bump                  # Bump version
make release               # Create and publish release
```

Run `make help` in a language-specific template for the complete list of available targets.

## 🛠️ Contributing

Contributions to Rhiza Core are welcome! This repository provides the foundation for all language-specific templates.
### To Contribute:

1. Fork the repository
2. Clone and setup:
   ```bash
   git clone https://github.com/your-username/rhiza-core.git
   cd rhiza-core
   make install
   ```
3. Create your feature branch (`git checkout -b feature/amazing-feature`)
4. Make your changes and test
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- **[rhiza](https://github.com/Jebel-Quant/rhiza)** - Python template built on rhiza-core
- **[rhiza-go](https://github.com/Jebel-Quant/rhiza-go)** - Go template built on rhiza-core
- **[rhiza-cli](https://github.com/Jebel-Quant/rhiza-cli)** - CLI tool for Rhiza template management

## 🙏 Acknowledgments

- [GitHub Actions](https://github.com/features/actions) - For CI/CD capabilities
- [uv](https://github.com/astral-sh/uv) - For fast Python package operations
- The open-source community for inspiration and best practices


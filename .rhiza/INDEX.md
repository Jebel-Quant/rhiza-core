# Rhiza Index

> **Retired.** `rhiza-core` is no longer maintained — see [`jebel-quant/rhiza`](https://github.com/jebel-quant/rhiza).

Quick reference to all utilities, makefiles, and resources in the `.rhiza/` directory.

## 📁 Directory Structure

```
.rhiza/
├── rhiza.mk              # Core makefile logic
├── .rhiza-version        # Current Rhiza version
├── .cfg.toml             # Configuration file
├── .env                  # Environment variables
├── template-bundles.yml  # Template bundle definitions
├── make.d/               # Makefile extensions (auto-loaded)
├── completions/          # Shell completion scripts
├── tests/                # Test suite
└── assets/               # Static assets
```

## 🔧 Makefiles (`.rhiza/make.d/`)

| File | Purpose | Section |
|------|---------|---------|
| `agentic.mk` | AI agent integrations (copilot, claude) | Agentic Workflows |
| `bootstrap.mk` | Installation and environment setup | Bootstrap |
| `custom-env.mk` | Example environment customizations | - |
| `custom-task.mk` | Example custom tasks | Custom Tasks |
| `docs.mk` | Documentation generation (pdoc, MkDocs) | Documentation |
| `github.mk` | GitHub CLI integrations | GitHub Helpers |
| `quality.mk` | Code quality and formatting | Quality and Formatting |
| `releasing.mk` | Release and versioning | Releasing and Versioning |
| `test.mk` | Testing infrastructure | Development and Testing |

**Total**: 9 makefiles

## 🧪 Test Suite (`.rhiza/tests/`)

| Directory | Purpose |
|-----------|---------|
| `api/` | Makefile target validation (dry-run tests) |
| `deps/` | Dependency health checks |
| `integration/` | End-to-end workflow tests |
| `structure/` | Static project structure assertions |
| `sync/` | Template sync and content validation |
| `utils/` | Test infrastructure utilities |

See [tests/README.md](tests/README.md) for details.

## 🎨 Assets (`.rhiza/assets/`)

- `rhiza-logo.svg` - Rhiza logo graphic

## 🔌 Template Bundles

Defined in `template-bundles.yml`:

| Bundle | Description | Files |
|--------|-------------|-------|
| `core` | Core Rhiza infrastructure | Makefile, rhiza.mk, make.d, root configs |
| `github` | GitHub Actions workflows | CI/CD |
| `tests` | Testing infrastructure | pytest, coverage |
| `renovate` | Automated dependency updates | renovate.json |
| `legal` | Legal documentation | LICENSE, CODE_OF_CONDUCT |

## 🎯 Key Make Targets

### Bootstrap
- `make install` - Install dependencies
- `make install-uv` - Ensure uv/uvx is installed
- `make clean` - Clean artifacts and stale branches

### Development
- `make test` - Run test suite
- `make fmt` - Format code
- `make docs` - Generate documentation

### AI Agents
- `make copilot` - GitHub Copilot interactive prompt
- `make claude` - Claude Code interactive prompt

### Documentation
- `make docs` - Generate API documentation with pdoc
- `make mkdocs` - Serve the MkDocs site with live reload

### GitHub
- `make view-prs` - List open pull requests
- `make view-issues` - List open issues
- `make failed-workflows` - List failing workflows

### Quality
- `make fmt` - Format code with ruff
- `make lint` - Lint code
- `make deptry` - Check dependencies

### Releasing
- `make release` - Create a release
- `make bump` - Bump version

## 🔗 Related Documentation

- [Makefile Cookbook](make.d/README.md) - Common patterns and recipes
- [Test Suite Guide](tests/README.md) - Testing conventions

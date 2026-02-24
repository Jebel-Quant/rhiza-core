# Migration Guide: rhiza and rhiza-go to rhiza-core Inheritance

This guide explains how to migrate existing `rhiza` (Python) and `rhiza-go` (Go) templates to inherit from `rhiza-core`.

## Overview

Previously, `rhiza` and `rhiza-go` were standalone template repositories containing both language-specific and language-agnostic components. With the introduction of `rhiza-core`, the shared infrastructure has been extracted into a common foundation.

### Before (Standalone)

```
rhiza/
├── .rhiza/make.d/
│   ├── github.mk      # Duplicated in rhiza-go
│   ├── docker.mk      # Duplicated in rhiza-go
│   ├── lfs.mk         # Duplicated in rhiza-go
│   ├── bootstrap.mk   # Python-specific
│   ├── test.mk        # Python-specific
│   └── quality.mk     # Python-specific
└── ...

rhiza-go/
├── .rhiza/make.d/
│   ├── github.mk      # Duplicated from rhiza
│   ├── docker.mk      # Duplicated from rhiza
│   ├── lfs.mk         # Duplicated from rhiza
│   ├── bootstrap.mk   # Go-specific
│   ├── test.mk        # Go-specific
│   └── quality.mk     # Go-specific
└── ...
```

### After (With Inheritance)

```
rhiza-core/
├── .rhiza/make.d/
│   ├── github.mk      # Shared infrastructure
│   ├── docker.mk      # Shared framework
│   ├── lfs.mk         # Shared infrastructure
│   ├── agentic.mk     # Shared infrastructure
│   ├── book.mk        # Shared framework
│   └── releasing.mk   # Shared framework
└── ...

rhiza/
├── .rhiza/
│   ├── template.yml   # Points to rhiza-core
│   └── make.d/
│       ├── bootstrap.mk   # Python-specific (overrides)
│       ├── test.mk        # Python-specific (overrides)
│       └── quality.mk     # Python-specific (overrides)
└── ...

rhiza-go/
├── .rhiza/
│   ├── template.yml   # Points to rhiza-core
│   └── make.d/
│       ├── bootstrap.mk   # Go-specific (overrides)
│       ├── test.mk        # Go-specific (overrides)
│       └── quality.mk     # Go-specific (overrides)
└── ...
```

## Migration Steps

### For rhiza (Python Template)

#### 1. Create `.rhiza/template.yml`

```yaml
# .rhiza/template.yml
repository: Jebel-Quant/rhiza-core
ref: v0.1.0

templates:
  - core
  - github
  - docker
  - lfs
  - legal
  - renovate
  - book
  - release

exclude: |
  # Keep Python-specific overrides
  .rhiza/make.d/bootstrap.mk
  .rhiza/make.d/test.mk
  .rhiza/make.d/quality.mk
  .rhiza/make.d/marimo.mk
  .rhiza/make.d/presentation.mk
  .rhiza/make.d/tutorial.mk
  
  # Keep Python-specific configurations
  .python-version
  pyproject.toml
  pytest.ini
  ruff.toml
  .pre-commit-config.yaml
  
  # Keep Python-specific CI workflows
  .github/workflows/rhiza_ci.yml
  .github/workflows/rhiza_pre-commit.yml
  .github/workflows/rhiza_deptry.yml
  .github/workflows/rhiza_marimo.yml
  .github/workflows/rhiza_benchmarks.yml
  .github/workflows/rhiza_codeql.yml
  .github/workflows/rhiza_security.yml
  
  # Keep Python-specific requirements
  .rhiza/requirements/
```

#### 2. Remove Duplicate Files

After configuring template inheritance, remove files that will come from rhiza-core:

```bash
# Remove shared makefiles (will come from rhiza-core)
git rm .rhiza/make.d/github.mk
git rm .rhiza/make.d/docker.mk
git rm .rhiza/make.d/lfs.mk
git rm .rhiza/make.d/agentic.mk
git rm .rhiza/make.d/custom-env.mk
git rm .rhiza/make.d/custom-task.mk

# Remove shared GitHub Actions (will come from rhiza-core)
git rm .github/workflows/copilot-setup-steps.yml
git rm .github/workflows/rhiza_validate.yml
git rm .github/workflows/rhiza_sync.yml
git rm .github/actions/configure-git-auth -r

# Keep .editorconfig, LICENSE, CODE_OF_CONDUCT.md, CONTRIBUTING.md
# as they may have Python-specific customizations
```

#### 3. Update Template Bundles

Update `.rhiza/template-bundles.yml` to only include Python-specific bundles:

```yaml
version: "0.8.0"

bundles:
  # Python-specific bundles only
  tests:
    description: "Python testing with pytest"
    files:
      - .rhiza/make.d/test.mk
      - pytest.ini
      - .rhiza/requirements/tests.txt
      - .github/workflows/rhiza_ci.yml
      - .github/workflows/rhiza_codeql.yml
      - .github/workflows/rhiza_security.yml
  
  marimo:
    description: "Marimo notebooks for Python"
    files:
      - .rhiza/make.d/marimo.mk
      - .rhiza/requirements/marimo.txt
      - .github/workflows/rhiza_marimo.yml
  
  # ... other Python-specific bundles
```

#### 4. Test the Migration

```bash
# Sync from rhiza-core
uvx rhiza materialize

# Verify shared files came from rhiza-core
git status

# Test that everything still works
make install
make test
make lint
```

### For rhiza-go (Go Template)

#### 1. Create `.rhiza/template.yml`

```yaml
# .rhiza/template.yml
repository: Jebel-Quant/rhiza-core
ref: v0.1.0

templates:
  - core
  - github
  - docker
  - lfs
  - legal
  - renovate
  - book
  - release

exclude: |
  # Keep Go-specific overrides
  .rhiza/make.d/bootstrap.mk
  .rhiza/make.d/test.mk
  .rhiza/make.d/quality.mk
  .rhiza/make.d/security.mk
  
  # Keep Go-specific configurations
  .go-version
  go.mod
  go.sum
  .golangci.yml
  .goreleaser.yml
  .pre-commit-config.yaml
  
  # Keep Go-specific CI workflows
  .github/workflows/rhiza_ci.yml
  .github/workflows/rhiza_pre-commit.yml
  .github/workflows/rhiza_release.yml
  .github/workflows/rhiza_security.yml
  
  # Keep Go-specific scripts
  install.sh
  uninstall.sh
```

#### 2. Remove Duplicate Files

```bash
# Remove shared makefiles (will come from rhiza-core)
git rm .rhiza/make.d/github.mk
git rm .rhiza/make.d/docker.mk
git rm .rhiza/make.d/lfs.mk
git rm .rhiza/make.d/agentic.mk
git rm .rhiza/make.d/custom-env.mk
git rm .rhiza/make.d/custom-task.mk

# Remove shared GitHub Actions (will come from rhiza-core)
git rm .github/workflows/copilot-setup-steps.yml
git rm .github/workflows/rhiza_validate.yml
git rm .github/workflows/rhiza_sync.yml
git rm .github/actions/configure-git-auth -r
```

#### 3. Update Template Bundles

Update `.rhiza/template-bundles.yml` to only include Go-specific bundles:

```yaml
version: "0.2.0"

bundles:
  # Go-specific bundles only
  tests:
    description: "Go testing with go test"
    files:
      - .rhiza/make.d/test.mk
      - .github/workflows/rhiza_ci.yml
  
  security:
    description: "Go security scanning with gosec"
    files:
      - .rhiza/make.d/security.mk
      - .github/workflows/rhiza_security.yml
  
  # ... other Go-specific bundles
```

#### 4. Test the Migration

```bash
# Sync from rhiza-core
uvx rhiza materialize

# Verify shared files came from rhiza-core
git status

# Test that everything still works
make install
make test
make fmt
```

## Validation Checklist

After migration, verify:

- [ ] `.rhiza/template.yml` points to `rhiza-core`
- [ ] Shared makefiles are removed from your repo
- [ ] Language-specific makefiles remain (bootstrap.mk, test.mk, quality.mk)
- [ ] `make install` works correctly
- [ ] `make test` works correctly
- [ ] `make fmt` works correctly
- [ ] CI workflows pass
- [ ] `uvx rhiza materialize` successfully syncs from rhiza-core
- [ ] `uvx rhiza validate` passes

## Benefits After Migration

1. **Reduced Duplication**: Shared infrastructure is maintained in one place
2. **Easier Updates**: Bug fixes and improvements to shared components automatically available
3. **Consistency**: All language templates use the same GitHub helpers, Docker targets, etc.
4. **Faster Development**: New language templates can be created more quickly
5. **Clearer Separation**: Language-specific vs. language-agnostic concerns are clearly separated

## Troubleshooting

### Problem: Conflicts during sync

**Solution**: Check your `exclude` patterns in `.rhiza/template.yml`. Ensure you're excluding files you want to keep.

### Problem: Missing files after migration

**Solution**: Verify the `templates` list in `.rhiza/template.yml` includes the bundles you need (e.g., `github`, `docker`).

### Problem: CI workflows failing

**Solution**: Ensure you've kept language-specific CI workflows in your exclude list. Check that language-specific dependencies are still configured correctly.

### Problem: Make targets not working

**Solution**: Verify that language-specific makefiles (bootstrap.mk, test.mk, quality.mk) are excluded and still present in your repository.

## Getting Help

- Check the [rhiza-core README](../README.md)
- Review [TEMPLATE_DEVELOPMENT.md](../docs/TEMPLATE_DEVELOPMENT.md)
- Open an issue in [rhiza-core issues](https://github.com/Jebel-Quant/rhiza-core/issues)
- See existing language templates for examples

## Timeline

**Recommended Migration Schedule:**

1. **Week 1**: Create `.rhiza/template.yml` and test sync
2. **Week 2**: Remove duplicate files gradually, test after each change
3. **Week 3**: Update template-bundles.yml
4. **Week 4**: Final testing and validation

Take your time and test thoroughly at each step. The migration can be done gradually without breaking existing functionality.

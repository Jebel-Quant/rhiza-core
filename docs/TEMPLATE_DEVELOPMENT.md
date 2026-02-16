# Template Development Guide

This guide explains how to create a new language-specific Rhiza template that inherits from rhiza-core.

## Overview

Rhiza Core provides the language-agnostic foundation for all Rhiza templates. When creating a new language template (e.g., `rhiza-rust`, `rhiza-typescript`), you'll inherit the core infrastructure and add language-specific tooling.

## Architecture

```
rhiza-core (language-agnostic)
├── .rhiza/make.d/          # Shared Makefile infrastructure
├── .github/workflows/      # Base CI/CD workflows
├── .editorconfig           # Editor configuration
├── CODE_OF_CONDUCT.md      # Community guidelines
└── CONTRIBUTING.md         # Contribution guide

rhiza-<language> (language-specific)
├── .rhiza/
│   ├── template.yml        # Inherits from rhiza-core
│   └── make.d/
│       ├── bootstrap.mk    # Language-specific setup (override)
│       ├── quality.mk      # Language-specific linting (override)
│       └── test.mk         # Language-specific testing (override)
├── .github/workflows/      # Language-specific CI workflows
└── <language-specific files>
```

## Step-by-Step Guide

### 1. Create Your Template Repository

```bash
# Clone rhiza-core as starting point
git clone https://github.com/Jebel-Quant/rhiza-core.git rhiza-<language>
cd rhiza-<language>

# Set up as new repository
rm -rf .git
git init
git remote add origin https://github.com/<your-org>/rhiza-<language>.git
```

### 2. Configure Template Inheritance

Create or update `.rhiza/template.yml`:

```yaml
# .rhiza/template.yml
repository: Jebel-Quant/rhiza-core
ref: v0.1.0

# Select which core bundles to include
templates:
  - core         # Core infrastructure (required)
  - github       # GitHub helpers
  - docker       # Docker support
  - lfs          # Git LFS support

# Fine-grained file inclusion
include: |
  .rhiza/make.d/github.mk
  .rhiza/make.d/docker.mk
  .rhiza/make.d/lfs.mk
  .rhiza/make.d/agentic.mk
  .rhiza/make.d/book.mk
  .editorconfig
  CODE_OF_CONDUCT.md
  CONTRIBUTING.md

# Exclude files you'll override
exclude: |
  .rhiza/make.d/bootstrap.mk
  .rhiza/make.d/quality.mk
  .rhiza/make.d/test.mk
```

### 3. Override Language-Specific Makefiles

#### Bootstrap (``.rhiza/make.d/bootstrap.mk`)

Override with your language-specific setup:

```makefile
## bootstrap.mk - Language-specific installation and setup

.PHONY: install clean

##@ Bootstrap

install: ## Install dependencies
	@printf "${BLUE}[INFO] Installing <language> dependencies...${RESET}\n"
	# Example for Rust
	@cargo build
	# Example for TypeScript
	@npm install
	# Example for Java
	@mvn clean install

clean: ## Clean build artifacts
	@printf "${BLUE}[INFO] Cleaning <language> artifacts...${RESET}\n"
	# Example for Rust
	@cargo clean
	# Example for TypeScript
	@rm -rf node_modules dist
```

#### Quality (``.rhiza/make.d/quality.mk`)

Override with your language-specific linting:

```makefile
## quality.mk - Language-specific code quality checks

.PHONY: fmt lint

##@ Quality and Formatting

fmt: ## Format and lint code
	@printf "${BLUE}[INFO] Formatting <language> code...${RESET}\n"
	# Example for Rust
	@cargo fmt
	@cargo clippy --fix --allow-dirty
	# Example for TypeScript
	@npm run lint:fix
	# Example for Go
	@gofmt -w .
	@golangci-lint run --fix

lint: ## Run linter (check-only)
	@printf "${BLUE}[INFO] Linting <language> code...${RESET}\n"
	# Example for Rust
	@cargo clippy -- -D warnings
	# Example for TypeScript
	@npm run lint
```

#### Testing (`.rhiza/make.d/test.mk`)

Override with your language-specific testing:

```makefile
## test.mk - Language-specific testing

.PHONY: test test-unit test-integration

##@ Development and Testing

test: ## Run all tests
	@printf "${BLUE}[INFO] Running <language> tests...${RESET}\n"
	# Example for Rust
	@cargo test
	# Example for TypeScript
	@npm test
	# Example for Go
	@go test ./...

test-unit: ## Run unit tests only
	# Language-specific implementation

test-integration: ## Run integration tests only
	# Language-specific implementation
```

### 4. Add Language-Specific Configuration Files

Add the configuration files specific to your language:

**For Rust:**
- `Cargo.toml`
- `Cargo.lock`
- `rust-toolchain.toml`
- `.rustfmt.toml`
- `clippy.toml`

**For TypeScript/JavaScript:**
- `package.json`
- `tsconfig.json`
- `.eslintrc.js`
- `.prettierrc`

**For Go:**
- `go.mod`
- `go.sum`
- `.go-version`
- `.golangci.yml`

**For Java:**
- `pom.xml` or `build.gradle`
- `checkstyle.xml`
- `.java-version`

### 5. Create Language-Specific GitHub Actions

Create CI workflows in `.github/workflows/`:

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      # Language-specific setup
      - name: Setup <Language>
        uses: actions/setup-<language>@v4
        with:
          <language>-version: '<version>'
      
      - name: Install dependencies
        run: make install
      
      - name: Run linter
        run: make lint
      
      - name: Run tests
        run: make test
```

### 6. Update README

Customize the README for your language:

```markdown
# Rhiza <Language>

A collection of reusable configuration templates for modern <Language> projects.

## Features

- <Language>-specific tooling integration
- CI/CD workflows for <Language>
- Testing framework setup
- Linting and formatting
- Inherits language-agnostic infrastructure from rhiza-core

## Quick Start

\`\`\`bash
cd /path/to/your/<language>-project
uvx rhiza init
# Edit .rhiza/template.yml to point to rhiza-<language>
uvx rhiza materialize
\`\`\`

## What's Included

- **<Language> Build System** - [Tool name] configuration
- **Testing** - [Test framework] setup
- **Linting** - [Linter] configuration
- **Formatting** - [Formatter] setup
- **CI/CD** - GitHub Actions for <Language>

Inherits from [rhiza-core](https://github.com/Jebel-Quant/rhiza-core):
- GitHub helpers
- Docker support
- Release automation
- Documentation tooling
```

### 7. Create Template Bundles

Define template bundles in `.rhiza/template-bundles.yml`:

```yaml
version: "0.1.0"

bundles:
  # Core language infrastructure
  core:
    description: "Core <Language> infrastructure"
    required: true
    files:
      - .rhiza/make.d/bootstrap.mk
      - .rhiza/make.d/quality.mk
      - .rhiza/make.d/test.mk
      - <language-config-file>
      
  # Testing infrastructure
  tests:
    description: "<Language> testing setup"
    files:
      - .rhiza/make.d/test.mk
      - tests/
      
  # Language-specific features
  <feature>:
    description: "<Feature> support"
    files:
      - <feature-files>
```

### 8. Testing Your Template

1. **Create a test project:**
   ```bash
   mkdir /tmp/test-<language>-template
   cd /tmp/test-<language>-template
   git init
   ```

2. **Configure to use your template:**
   ```yaml
   # .rhiza/template.yml
   repository: <your-org>/rhiza-<language>
   ref: main
   
   templates:
     - core
     - tests
   ```

3. **Materialize and test:**
   ```bash
   uvx rhiza materialize
   make install
   make test
   make lint
   ```

## Best Practices

### 1. Maintain Language-Agnostic Core

Keep core infrastructure (GitHub helpers, Docker, etc.) in rhiza-core. Only override when absolutely necessary.

### 2. Follow Naming Conventions

- Use consistent target names: `install`, `test`, `lint`, `fmt`
- Keep make targets language-agnostic where possible
- Document all custom targets in help text

### 3. Provide Good Defaults

Configure sensible defaults for:
- Linting rules
- Testing frameworks
- CI/CD workflows
- Editor configurations

### 4. Document Dependencies

Clearly document:
- Required language version
- Build tool versions
- System dependencies
- Installation instructions

### 5. Test Thoroughly

- Test on multiple OS (Linux, macOS, Windows if applicable)
- Test with different language versions
- Validate CI/CD workflows
- Check template synchronization

## Examples

See existing templates:
- **[rhiza](https://github.com/Jebel-Quant/rhiza)** - Python template
- **[rhiza-go](https://github.com/Jebel-Quant/rhiza-go)** - Go template

## Getting Help

- Open an issue in [rhiza-core](https://github.com/Jebel-Quant/rhiza-core/issues)
- Check the [rhiza-core README](../README.md)
- Review existing language templates for patterns

## Contributing

When you've created a new language template:

1. Add it to the [rhiza-core README](../README.md) under "Related Projects"
2. Consider contributing improvements back to rhiza-core
3. Share your template with the community!

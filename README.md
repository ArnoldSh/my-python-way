# My Way Python project (Java switcher in da house)

A production-style Python project created for learning modern Python
development practices.\
The goal of this repository is to practice building a clean,
maintainable, and well-tested Python application using industry-standard
tools and workflows.

## Project Goals

-   Learn how to structure a real-world Python project
-   Use modern dependency management
-   Implement automated testing
-   Apply code quality and formatting tools
-   Configure CI pipelines
-   Practice good Git and documentation practices

------------------------------------------------------------------------

# Project Stack

This project uses the following tools:

-   Python
-   Poetry (dependency management)
-   pytest (testing)
-   Ruff (linting)
-   Black (code formatting)
-   mypy (static typing)
-   pre-commit (git hooks)
-   GitHub Actions (CI)

------------------------------------------------------------------------

# Project Structure

    project-name/
    │
    ├─ src/
    │  └─ project_name/
    │     ├─ __init__.py
    │     ├─ main.py
    │     └─ ...
    │
    ├─ tests/
    │  ├─ __init__.py
    │  └─ test_*.py
    │
    ├─ pyproject.toml
    ├─ README.md
    ├─ LICENSE
    ├─ .gitignore
    ├─ .env.example
    │
    └─ .github/
       └─ workflows/
          └─ ci.yml

The project uses the **src layout**, which is a common practice for
preventing import issues and improving packaging reliability.

------------------------------------------------------------------------

# Installation

### Clone the repository

``` bash
git clone https://github.com/yourusername/project-name.git
cd project-name
```

### Install dependencies

``` bash
poetry install
```

### Activate virtual environment

``` bash
poetry shell
```

------------------------------------------------------------------------

# Running Tests

Tests are written using `pytest`.

``` bash
pytest
```

Run tests with coverage:

``` bash
pytest --cov
```

------------------------------------------------------------------------

# Code Quality

This project enforces code quality using the following tools:

### Formatting

``` bash
black .
```

### Linting

``` bash
ruff check .
```

### Type Checking

``` bash
mypy src
```

------------------------------------------------------------------------

# Pre-commit Hooks

Pre-commit hooks ensure that code quality checks run automatically
before each commit.

Install hooks:

``` bash
pre-commit install
```

------------------------------------------------------------------------

# Continuous Integration

The project uses **GitHub Actions** for CI.

The pipeline runs automatically on every push and pull request and
includes:

-   dependency installation
-   linting
-   type checking
-   running tests
-   coverage reporting

------------------------------------------------------------------------

# Environment Variables

Configuration is managed using environment variables.

Create a `.env` file based on the example:

    .env.example

Never commit sensitive data to the repository.

------------------------------------------------------------------------

# Logging

The project includes structured logging with configurable log levels:

-   DEBUG
-   INFO
-   WARNING
-   ERROR

Logs can be configured to output to both console and file.

------------------------------------------------------------------------

# CLI Interface (Optional)

If the project exposes command line functionality, it will provide a CLI
interface.

Typical commands may include:

    project-name run
    project-name init
    project-name status

------------------------------------------------------------------------

# Versioning

The project follows **Semantic Versioning**.

Version information is stored in:

    pyproject.toml

------------------------------------------------------------------------

# Development Roadmap

## Project Setup

-   [ ] initialize repository
-   [ ] configure Poetry
-   [ ] create project structure
-   [ ] configure `.gitignore`
-   [ ] add license
-   [ ] create README

## Dependency Management

-   [ ] configure `pyproject.toml`
-   [ ] separate dev dependencies
-   [ ] lock dependency versions

## Testing

-   [ ] configure pytest
-   [ ] create basic tests
-   [ ] add fixtures
-   [ ] add parametrized tests
-   [ ] configure test coverage

## Code Quality

-   [ ] configure Ruff
-   [ ] configure Black
-   [ ] configure mypy
-   [ ] integrate pre-commit hooks

## Continuous Integration

-   [ ] create GitHub Actions workflow
-   [ ] run linting in CI
-   [ ] run tests in CI
-   [ ] add coverage reporting

## Configuration

-   [ ] implement environment configuration
-   [ ] create `.env.example`
-   [ ] validate environment variables

## Logging

-   [ ] configure logging system
-   [ ] add log formatting
-   [ ] support file logging

## Documentation

-   [ ] improve README
-   [ ] add usage examples
-   [ ] document architecture

## Optional Improvements

-   [ ] CLI interface
-   [ ] API layer
-   [ ] packaging and distribution
-   [ ] containerization (Docker)

------------------------------------------------------------------------

# License

This project is licensed under the MIT License.

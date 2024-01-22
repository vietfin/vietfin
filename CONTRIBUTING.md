# Contributing Guidelines

Thanks for taking the time to contribute.

The following is a set of guidelines for contributing to VietFin. These are mostly guidelines, not rules.

## Code style

Guidance on code style

- Use [ruff](https://docs.astral.sh/ruff/) to format code following the [PEP 8](https://peps.python.org/pep-0008/) style guide, configured in `pyproject.toml`. For example:
    - Use 4 spaces per indentation level
    - Use `snake_case` for variable and function names
    - Use `PascalCase` for class names
    - Use `ALL_CAPS` for constants
    - Use double-quoted strings
    - Limit all lines to a maximum of 80 characters
- Use [numpy style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard)
- Use [Type Hints](https://peps.python.org/pep-0484/) for functions and classes

## Branch strategy

This project uses a two-layer branch model.

- `dev` is the main branch. All new features and bug fixes are made on this branch.
- `main` is the stable branch. This branch is updated only when a new release is made.

![branching-strategy](https://miro.medium.com/v2/resize:fit:700/1*2YagIpX6LuauC3ASpwHekg.png) Credit: [yfinance](https://github.com/ranaroussi/yfinance/discussions/1084)

## Contributing to the codebase

### Work on an issue

Pick or suggest an issue, by going through the issue tracker, which you would like to work on. 

Setup your local development environment. Then start coding.

### Setup local development environment

I use the combination of [conda](https://docs.conda.io/en/latest/) to manage virtual environments and [poetry](https://python-poetry.org/) to manage dependencies.

- Clone the `dev` branch of the VietFin repository. E.g. `git clone -b dev https://github.com/h7b/vietfin.git`
- Install [conda](https://docs.conda.io/en/latest/miniconda.html)
- Create a new conda environment named `dev-vietfin` with `Python 3.10`. E.g. `conda create -n dev-vietfin python=3.10`
- Activate the environment. E.g. `conda activate dev-vietfin`
- Install poetry. E.g. `conda install poetry`
- Install dependencies with optional dependency group `dev` for developement purposes. E.g. `poetry install --with dev`

### Open a Pull Request

When you have resolved your issue, open a pull request (PR) in the VietFin repository. Please adhere to the following guidelines:

- Make sure your branch is up to date with the `dev` branch of VietFin repository
- Start your PR title with a [conventional commit](https://www.conventionalcommits.org/en/) tag. We use the [Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#type) and follow this [guideline for git commits](https://deepsource.com/blog/git-best-practices)
- In the PR description, link to the issue you were working on

### Git Process

- Ensure that your branch is up to date with the `dev` branch of VietFin repository. E.g. `git pull upstream dev`
- Create a new git branch for your feature. E.g. `git checkout -b feat/AmazingFeature`
- Check the files you have touched using `git status`
- Stage the files you want to commit. E.g. `git add src/vietfin/funds/funds.py`
- Write a concise commit message under 50 characters. E.g. `git commit -m "feat: add AmazingFeature"`
- Push your changes to the appropriate branch in your fork. E.g. `git push origin feat/AmazingFeature`
- Go to your GitHub, then open a PR in the VietFin repository

## Contributing to documentation

<!-- TODO: Add documentation guidelines -->

## Test suite

The `./tests` folder contains the main VietFin test suite.

At the moment, the test suite contains only unit tests. These tests are intended to make sure all VietFin functionality work as intended.

## Versioning

VietFin adheres to the [semantic versioning](https://semver.org/) specification.

<!-- TODO: for future. If we decide to introduce a breaking change, the existing behavior will be deprecated. The deprecated functionality is removed two breaking releases after the deprecation happens. For example, a function deprecated in version `0.18.3` will be removed in version `0.20.0`. -->
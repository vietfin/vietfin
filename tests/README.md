# 1. VietFin Unit Testing

This document is an annex of the VietFin Contributing Guidelines.

It provides the necessary information to build, run and maintain Unit Tests for VietFin.

## 2. Run `unit tests`

In this section we will explain everything you need to run the `unit tests` on the VietFin project.

## 2.1. How to install tests dependencies?

To run the tests you will need first to install the [`pytest` package](https://docs.pytest.org/en/7.1.x/index.html). For example, we use `poetry` to manage our python dependencies.

```bash
poetry add pytest
```

### 2.2. How to run `tests`:

#### By `module`

You can run tests on a specific module by specifying the path of this module, as follows:

```bash
pytest tests/test_some_module.py
```

#### By test `name`

You can run tests by their name with the argument `-k`. Read more about this argument [here](https://docs.pytest.org/en/7.1.x/example/markers.html#using-k-expr-to-select-tests-based-on-their-name)

```bash
pytest tests/test_some_module.py -k test_function_name
```

## 3. How to build `unit tests`

When you contribute a new feature to the VietFin project, it's important that `tests` are added for this particular feature.

All the `unit tests` should be insides the `tests` folder. There should be at most one `test module` for each `module`/`package` of the VietFin project.

Each `test module` should follow the same naming pattern of the `module`/`package` that it is `testing`. For instance,

- in order to test the following module `src/vietfin/funds/funds.py`
- a `test module` should be added here: `tests/test_funds.py`
# get_secret_or_env_var

[![CircleCI](https://img.shields.io/circleci/build/gh/greenape/get_secret_or_env_var.svg?logo=CircleCI&style=flat-square)](https://circleci.com/gh/greenape/get_secret_or_env_var) [![codecov](https://img.shields.io/codecov/c/github/greenape/get_secret_or_env_var.svg?logo=Codecov&style=flat-square)](https://codecov.io/gh/greenape/get_secret_or_env_var)  [![License: MIT](https://img.shields.io/github/license/greenape/get_secret_or_env_var.svg?style=flat-square)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/python/black)

A docker-secrets aware wrapper for Python's os.getenv and os.environ.

Supplies:

- `getenv`
- `getenvb`
- `environ`
- `environb`

Which behave exactly like their stdlib equivalents, but will look for a file in `/run/secrets` and return the contents in preference to any environment variables.

Setting values on `environ` or `environb` will set the values in their `os.` equivalent.
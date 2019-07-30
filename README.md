# _get_secret_or_env_var

A docker-secrets aware wrapper for Python's os.getenv and os.environ.

Supplies:

- `getenv`
- `getenvb`
- `environ`
- `environb`

Which behave exactly like their stdlib equivalents, but will look for a file in `/run/secrets` and return the contents in preference to any environment variables.

Setting values on `environ` or `environb` will set the values in their `os.` equivalent.
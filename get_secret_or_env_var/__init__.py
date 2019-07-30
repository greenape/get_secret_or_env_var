import os
from collections import ChainMap
from pathlib import Path
from typing import Optional, Union

DOCKER_SECRETS_PATH = Path("/run/secrets")


def _get_secret_or_env_var(key: str, default: Optional[str] = None) -> str:
    """
    Get a value from docker secrets (i.e. read it from a file in
    /run/secrets) or from the environment variable with the same
    name, or return the default if neither is found.

    Parameters
    ----------
    key : str
        Name of the secret / environment variable.
    default : str, optional
        Optionally specify a value to return if neither is set.

    Returns
    -------
    str
        Value in the file, or value of the environment variable, or default if defined.
        If default is not specified, returns None.
    """
    try:
        return environ[key]
    except KeyError:
        return default


def _get_secret_or_env_varb(key: bytes, default: Optional[bytes] = None) -> bytes:
    """
    Get a value from docker secrets (i.e. read it from a file in
    /run/secrets) or from the environment variable with the same
    name, or return the default if neither is found.

    Parameters
    ----------
    key : bytes
        Name of the secret / environment variable.
    default : bytes, optional
        Optionally specify a value to return if neither is set.

    Returns
    -------
    str
        Value in the file, or value of the environment variable, or default if defined.
        If default is not specified, returns None.
    """
    try:
        return environb[key]
    except KeyError:
        return default


class _DockerSecretsDict:
    def __init__(self, *, mode):
        if mode not in ("r", "rb"):
            raise ValueError(f"Mode must be one of 'r' or 'rb', but got {mode}.")
        self.mode = mode

    def __getitem__(self, item: Union[bytes, str]) -> Union[bytes, str]:
        try:
            item = item.decode()
        except AttributeError:
            pass  # Not bytes
        try:
            with open(DOCKER_SECRETS_PATH / item, self.mode) as fin:
                return fin.read().strip()
        except FileNotFoundError:
            raise KeyError


class _SecretEnviron:
    """
    Wrapper for os.environ which tries to find a secret first.
    """

    def __init__(self, *, mode: str, base_environ: os._Environ):
        self.__class__ = type(
            base_environ.__class__.__name__,
            (self.__class__, base_environ.__class__),
            {},
        )
        self.__dict__ = base_environ.__dict__
        self._secrets_data = ChainMap(_DockerSecretsDict(mode=mode), base_environ)

    def __getitem__(self, item: Union[str, bytes]) -> Union[str, bytes]:
        return self._secrets_data[item]


environ = _SecretEnviron(mode="r", base_environ=os.environ)
environb = _SecretEnviron(mode="rb", base_environ=os.environb)
getenv = _get_secret_or_env_var
getenvb = _get_secret_or_env_varb

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

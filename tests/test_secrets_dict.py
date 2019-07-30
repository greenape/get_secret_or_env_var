import pytest

from get_secret_or_env_var import _DockerSecretsDict


def test_mode_error():
    with pytest.raises(ValueError):
        _DockerSecretsDict(mode="NOT_A_MODE")
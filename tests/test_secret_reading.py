import pytest

from get_secret_or_env_var import *


@pytest.mark.parametrize(
    "func, secret, expected",
    [(getenv, "TEST_SECRET", "TEST_VALUE"), (getenvb, b"TEST_SECRET", b"TEST_VALUE")],
)
def test_read_secret(func, secret, expected, monkeypatch, tmpdir):
    monkeypatch.setattr("get_secret_or_env_var.DOCKER_SECRETS_PATH", tmpdir)
    with open(tmpdir / "TEST_SECRET", "w") as fout:
        fout.write("TEST_VALUE")
    assert func(secret) == expected


@pytest.mark.parametrize(
    "func, secret, expected",
    [(environ, "TEST_SECRET", "TEST_VALUE"), (environb, b"TEST_SECRET", b"TEST_VALUE")],
)
def test_environ_reads_secret(func, secret, expected, monkeypatch, tmpdir):
    monkeypatch.setattr("get_secret_or_env_var.DOCKER_SECRETS_PATH", tmpdir)
    with open(tmpdir / "TEST_SECRET", "w") as fout:
        fout.write("TEST_VALUE")
    assert func[secret] == expected


@pytest.mark.parametrize(
    "func, secret, expected",
    [(getenv, "TEST_SECRET", "TEST_VALUE"), (getenvb, b"TEST_SECRET", b"TEST_VALUE")],
)
def test_read_secret_not_found(func, secret, expected, monkeypatch, tmpdir):
    assert func(secret, expected) == expected


@pytest.mark.parametrize(
    "func, secret", [(environ, "TEST_SECRET"), (environb, b"TEST_SECRET")]
)
def test_environ_raises_key_error_if_secret_not_found(
    func, secret, monkeypatch, tmpdir
):
    with pytest.raises(KeyError):
        func[secret]

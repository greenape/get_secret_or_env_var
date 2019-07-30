import io

from setuptools import find_packages, setup

import versioneer


with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name="get_secret_or_env_var",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="http://github.com/greenape/get_secret_or_env_var",
    license="MIT",
    maintainer="greenape",
    maintainer_email="jono@nanosheep.net",
    description="Docker secrets aware alternative to os.getenv and os.environ",
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    python_requires=">3.5.2",
    extras_require={"test": ["pytest", "pytest-cov"]},
)

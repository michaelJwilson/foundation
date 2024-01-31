> cache login credentials for longer
git config --global credential.helper "cache --timeout 7200"

> set mamba as the conda solver?
conda config --set solver libmamba

> create a python virtual environment
mkdir pudev

virtualenv pudev

source ~/software/pudev/bin/activate

> pip install poetry, pre-commit, etc.
pip install poetry
pip install pre-commit
pip install polars
pip install pytest-cov
pip install sphinx
pip install line_profiler
pip install pipx
pip install furo

> pipx installs
pipx install poetry

> install maturin
> https://github.com/PyO3/maturin
> https://github.com/PyO3/pyo3
pipx install maturin

> install ruff
> see https://github.com/astral-sh/ruff
pip install ruff

> rust-clippy
> https://github.com/rust-lang/rust-clippy

> apptainer / singularity
https://apptainer.org/docs/user/latest/quick_start.html

> pytest
> https://docs.pytest.org/en/7.4.x/how-to/fixtures.html
pip install pytest

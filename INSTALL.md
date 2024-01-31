> create a python virtual environment
mkdir pudev

virtualenv pudev

source ~/software/pudev/bin/activate

> set mamba as the conda solver?
conda config --set solver libmamba

> install poetry
pip install poetry

> install pre-commit
pip install pre-commit

> install maturin
> https://github.com/PyO3/maturin
> https://github.com/PyO3/pyo3
pipx install maturin

> install ruff + polars
> see https://github.com/astral-sh/ruff
pip install ruff
pip install polars

> rust-clippy
> https://github.com/rust-lang/rust-clippy

> apptainer / singularity
> https://apptainer.org/docs/user/main/quick_start.html#downloading-images

> pytest
> https://docs.pytest.org/en/7.4.x/how-to/fixtures.html
pip install pytest

> pytest-cov
pip install pytest-cov

> sphinx
pip install sphinx

> cache login credentials for longer
git config --global credential.helper "cache --timeout 7200"

> load python modules on princeton clusters
module load anaconda3/2023.9

> set mamba as the conda solver?
conda config --set solver libmamba

> create a python virtual environment
mkdir ~/software/pudev

python3 -m venv "/home/mw9568/software/pudev"

source /home/mw9568/software/pudev/bin/activate

> pip install maturin
pip install -U pip maturin

> pip install poetry, pre-commit, etc.
pip install pre-commit sphinx pipx furo

> install ruff
> see https://github.com/astral-sh/ruff
pip install ruff

> pytest
> https://docs.pytest.org/en/7.4.x/how-to/fixtures.html
pip install pytest

> optional
pip install line_profiler
pip install polars
pip install pytest-cov

> pipx installs
pipx install poetry

> install maturin
> https://github.com/PyO3/maturin
> https://github.com/PyO3/pyo3
pipx install maturin

> rust-clippy
> https://github.com/rust-lang/rust-clippy

> apptainer / singularity
https://apptainer.org/docs/user/latest/quick_start.html

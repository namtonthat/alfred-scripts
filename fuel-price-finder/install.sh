# Install dependencies and run the script
export PYTHON_VERSION=3.10.9
pyenv install $PYTHON_VERSION
pyenv local alfred-scripts-$PYTHON_VERSION

# Shell
poetry shell
poetry install --no-root
PYTHON_VERSION=$PYTHON_VERSION

pyenv virtualenv $PYTHON_VERSION alfred-scripts-$PYTHON_VERSION
poetry shell
poetry install
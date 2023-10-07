
# Set the default python version
PYTHON_VERSION=3.10.9

.PHONY: setup
setup: # Setup env and pass in the python version
	@echo "⌨️  Installing packages necessary for local development"
	@./local_setup/setup.sh $(PYTHON_VERSION)
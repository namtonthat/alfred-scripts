
# Set the default python version
PYTHON_VERSION=3.9.16

.PHONY: setup
setup: # Setup env and pass in the python version
	@echo "⌨️  Installing packages necessary for local development"
	@./local_setup/setup.sh $(PYTHON_VERSION)

fuel: # Run the fuel script
	@echo "🔥 Running fuel script"
	@sudo poetry run python3 ./fuel-price-finder/fuel-prices.py
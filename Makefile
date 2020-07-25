# Ugh! You can't write multiline comment blocks in a Makefile
# The following is a weak workaround
define Comment

Features
---------
- Python dependency management with pip-tools
- Python linters: Black, Flake8, Isort
- Python type checking with mypy

Usage
------
- Dependency Management:
	Make sure you've defined your dependencies in `requirements.txt` and
	`requirements-dev.txt`

	`make upgrade`

- Linting:
	`make lint`
	or, `make lint path="main.py" line=88`

- Type Checking:
	`make typecheck`

- Multiple:
	`make lint typecheck path="file0.py file1.py"`


Caveats
--------
- This only looks for venv in the root path.
- This only works with embedded venv, not virtualenv
	To create an embedded venv, run:
	`python3.8 -m venv venv`

endef

path := .	# working path; use quotes if multiple files, e.g. "f.py g.py"
line := 88 	# black and isort compatible line length
ignore := *env	# folder ignored by black


all:
	@echo


# checks if virtual environment is active
# raises error if not active
.PHONY: venvcheck
venvcheck:
ifeq ("$(VIRTUAL_ENV)","")
	@echo "Venv is not activated!"
	@echo "Activate venv first."
	@echo
	exit 1
endif


# checks if pip-tools is installed; otherwise installs it
# runs pip-tools specific commands like pip-compile and pip-sync
.PHONY: upgrade
upgrade: venvcheck
ifeq ("$(wildcard venv/bin/pip-compile)","")	# checks if pip-compile exists
	@echo "Installing Pip-tools..."
	@pip install pip-tools
endif

ifeq ("$(wildcard venv/bin/pip-sync)","")	# checks if pip-sync exists
	@echo "Installing Pip-tools..."
	@pip install pip-tools
endif

# runs pip-compile and pip-sync
	@pip-compile --upgrade requirements-dev.txt
	@pip-compile --upgrade requirements.txt
	@pip-sync requirements-dev.txt requirements.txt


# checks if black, flake8 and isort is installed; otherwise installs them
# runs black, isort and flake8 sequentially
.PHONY: lint
lint: venvcheck
ifeq ("$(wildcard venv/bin/black)","")		# checks if black exists
	@echo "Installing Black..."
	@pip install black
endif

ifeq ("$(wildcard venv/bin/flake8)","")		# checks if flake8 exists
	@echo "Installing flake8..."
	@pip install flake8
	@echo
endif

ifeq ("$(wildcard venv/bin/isort)","")		# checks if isort exists
	@echo "Installing Isort..."
	@pip install isort
endif

# runs black
	@echo "Applying Black"
	@echo "----------------"
	@echo
	@black --line-length $(line) --exclude $(ignore) $(path)
	@echo

# runs flake8
	@echo "Applying Flake8"
	@echo "----------------"
	@echo
	@flake8 --max-line-length "$(line)" \
			--max-complexity "18" \
			--select "B,C,E,F,W,T4,B9" \
			--ignore "E203,E266,E501,W503,F403,F401,E402" \
			--exclude ".git,__pycache__,old, build, \
						dist, venv" $(path)

# runs isort
	@echo "Applying Isort"
	@echo "----------------"
	@echo
	@isort --atomic --profile black $(path)
	@echo


# check if mypy is installed; otherwise install it
# run mypy
.PHONY: typecheck
typecheck: venvcheck
ifeq ("$(wildcard venv/bin/mypy)","")		# checks if mypy exists
	@echo "Installing Mypy..."
	@pip install mypy
endif

# run mypy
	@echo "Applying MyPy"
	@echo "----------------"
	@echo
	@mypy $(path) --warn-redundant-casts --allow-redefinition --pretty \
				--warn-unused-ignores --ignore-missing-imports
	@echo


# Django specific
.PHONY: django_migrate
django_migrate: venvcheck
	python django_projects/locallibrary/manage.py makemigrations
	python django_projects/locallibrary/manage.py migrate

.PHONY: django_run
django_run: django_migrate
	python django_projects/locallibrary/manage.py runserver

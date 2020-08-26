

## Run

### Development Environment

* Go to the project level `settings.py` and change the `environ.Env.read_env(".env.prod")` line to `environ.Env.read_env(".env.dev")
* From the project's root folder (where `manage.py` lives), run:

```bash
chmod +x scripts/run_dev.sh
./scripts/run_dev.sh
```

### Production Environment

* Go to the project level `settings.py` and change the `environ.Env.read_env(".env.dev")` line to `environ.Env.read_env(".env.prod")
* From the project's root folder (where `manage.py` lives), run:

```bash
chmod +x scripts/run_prod.sh
./scripts/run_prod.sh
```

## Deployment Notes

### Configuration Management

This uses [django-environ](https://django-environ.readthedocs.io/en/latest/#) to manage development and production configurations.

There are 3 dotenv files associated with the management system:

* `.env.example` - dummy dotenv file (should be in VCS)
* `.env.dev` - dev environment variables (shouldn't be in VCS)
* `.env.prod` - prod environment variables (shouldn't be in VCS)

Install django-environ via pip and use it in the project's `setting.py`:

```python
# settings.py
import environ

# Reading the dotenv file
environ.Env.read_env(".env.prod")

# Env variable type casting
# Type casting is only required if a variable has a specific type other
# than string
env = environ.Env(DEBUG=(bool, False))

# Getting the value from the dotenv file
DEBUG = env("DEBUG")
```

<div class="container">
  <div class="center"><h1>Project Bookstore</h1></div>
</div>

## Description
A complete example of a demo Django application with Heroku deployment.
This application features:

* Config management via `django-environ` that aligns with the best practices mentioned in the 12-factor-app guideline
* Decoupled `docker-compose` files for development and production environment
* Production ready `settings.py`
* Pinned dependencies in the `requirements.txt` and `requirements-dev.txt` for better reproducibility
* A single command to reproduce everything locally via Docker

## Run

### Development Environment

* Make sure you've got Docker installed in your development machine
* Go to the project level `settings.py` and change the `environ.Env.read_env(".env.prod")` line to `environ.Env.read_env(".env.dev")
* From the project's root folder (where `manage.py` lives), run:

```bash
chmod +x scripts/run_dev.sh
./scripts/run_dev.sh
```

### Production Environment

This should only be executed in an SSL configured production machine or a PaaS like Heroku. If you run this locally, chances are your browser will try to establish an HTTPS connection over the localhost and you won't be able to access the site.

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

Install `django-environ` via pip and use it in the project's `setting.py`:

```python
# settings.py
import environ

# Env variable type casting
# Typecasting is only required if a variable has a specific type other
# than string
env = environ.Env(DEBUG=(bool, False))

# Reading the dotenv file
environ.Env.read_env(".env.prod")

# Getting the value from the dotenv file
DEBUG = env("DEBUG")
```

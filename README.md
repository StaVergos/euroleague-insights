# euroleague-insights

An app that provides insights for Euroleague

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: Apache Software License 2.0

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      uv run python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    uv run mypy euroleague_insights

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    uv run coverage run -m pytest
    uv run coverage html
    uv run open htmlcov/index.html

#### Running tests with pytest

    uv run pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html#using-webpack-or-gulp).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd euroleague_insights
uv run celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd euroleague_insights
uv run celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd euroleague_insights
uv run celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).


1. export COMPOSE_FILE=local.yml
    1. otherwise use -f local.yml on docker-compose.
    2. example: docker compose -f docker-compose.local.yml build --no-cache
2. docker-compose down --rmi all --volumes
3. docker compose -f docker-compose.local.yml up -d
4. docker-compose run django sh
5. python manage.py shell
6. docker compose -f docker-compose.local.yml run --rm django python manage.py shell
    1. Opens a shell inside django container
7. docker compose -f docker-compose.local.yml run --rm django python manage.py showmigrations
    1. Shows all the migrations that apply
    2. It has a box [] for each migration made
    3. It has a checked box [x] for each migration applied
8. docker compose -f docker-compose.local.yml run --rm django python manage.py makemigrations
    1. Mades the migration
9. docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
    1. Applies the migration
10. docker-compose -f local.yml logs --tail=100  django
    1. to read the 100 last lines of django logs
11. docker-compose -f local.yml logs --tail=100 -f django
    1. to run the logs live
12. docker-compose -f local.yml logs --tail=100 -f celeryworker
13. docker-compose run django python manage.py create_init_users
14. docker-compose exec postgres psql -U "username"
15. docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
16. docker-compose run django bash + pytest -W ignore
# alembic/env.py
from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

# Import your app config and models
import sys
from pathlib import Path

# Ensure project root is on sys.path so "src" imports work
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.core.config import config as app_config
from src.db.base import Base  # your single Base class
import src.db.models  # import models so they register on Base

alembic_config = context.config

# Set URL on the alembic config
alembic_config.set_main_option(
    "sqlalchemy.url",
    f"postgresql+psycopg2://{app_config.POSTGRES_USER}:{app_config.POSTGRES_PASSWORD}"
    f"@{app_config.POSTGRES_HOST}:{app_config.POSTGRES_PORT}/{app_config.POSTGRES_DB}",
)

if alembic_config.config_file_name is not None:
    fileConfig(alembic_config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    url = alembic_config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    # NOTE: use prefix="sqlalchemy." here
    connectable = engine_from_config(
        alembic_config.get_section(alembic_config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

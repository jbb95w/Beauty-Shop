import sys
from os.path import abspath, dirname, join
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# 1. ALWAYS DO THIS FIRST: Add Backend folder to Python path
# This allows 'from app...' imports to work
sys.path.insert(0, dirname(dirname(abspath(__file__))))

# 2. NOW you can safely import your app modules
from app.db.base import Base 
from app.models.user import User
from app.models.product import Product
from app.models.category import Category
from app.models.order import Order
from app.models.order_item import Order_item # Ensure this matches your class name

# 3. Standard Alembic setup
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Link Alembic to your models
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    # This reads the [alembic] section of your .ini file
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
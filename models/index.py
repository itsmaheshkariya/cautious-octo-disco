from importlib.metadata import metadata
from models.user import users
from conn.db import engine, meta

meta.create_all(engine)
# db.py
from databases import Database
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/mydatabase")
database = Database(DATABASE_URL)

from sqlalchemy.orm import sessionmaker
from app.database.engine import engine


SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine,
)

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings

args = {"check_same_thread": False} if "sqlite" in settings.DATABASE_URL else None

engine = create_engine(settings.DATABASE_URL, connect_args=args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

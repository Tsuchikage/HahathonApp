from typing import Any, AsyncGenerator

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base


engine = create_async_engine(f"postgresql+asyncpg://user:password@postgres:5432/database")
SessionLocal = async_sessionmaker(bind=engine)
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, Any]:
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()


async def database_health(db: AsyncSession) -> bool:
    try:
        await db.execute(select(1))
        return True
    except Exception:
        return False


import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from config import Settings

# Инициализация настроек из файла конфигурации
settings = Settings()

# Создание асинхронного двигателя (engine) для базы данных PostgreSQL
async_engine = create_async_engine(settings.DATABASE_URL_asyncpg, echo=True)

# Создание фабрики асинхронных сессий
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)

# Создание всех таблиц в базе данных
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Инициализация базы данных
asyncio.run(init_db())

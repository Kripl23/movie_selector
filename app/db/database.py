from sqlalchemy.ext.asyncio import create_async_engine

from config import settings

create_async_engine(settings.database_url)

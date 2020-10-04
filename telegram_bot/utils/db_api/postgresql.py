import asyncio

import asyncpg
from data import config


class Database:

    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncpg.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                database=config.PGDATABASE,
                host=config.ip
                )
            )

    async def select_all_lessons(self):
        sql = """ SELECT * FROM core_lesson """
        return await self.pool.fetch(sql)

    async def select_all_lessons_like_name(self, text):
        sql = """ SELECT * FROM core_lesson WHERE name LIKE $1 """
        return await self.pool.fetch(sql, f'%{text}%')

    async def select_lesson(self, lesson_id):
        sql = """ SELECT * FROM core_lesson WHERE id=$1 """
        return await self.pool.fetch(sql, lesson_id)

    async def select_task(self, task_id):
        sql = """ SELECT * FROM core_task WHERE id=$1 """
        return await self.pool.fetch(sql, task_id)
        
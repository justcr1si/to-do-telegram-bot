from os import getenv

import aiosqlite


DB_NAME = getenv('DB_NAME')


async def create_db() -> None:
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            '''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                task_text TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        await db.commit()


async def add_task(user_id: int, task_text: str) -> None:
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            'INSERT INTO tasks (user_id, task_text) VALUES (?, ?)',
            (user_id, task_text),
        )
        await db.commit()


async def get_tasks(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute(
            'SELECT id, task_text FROM tasks WHERE user_id = ?', (user_id,)
        )
        return await cursor.fetchall()


async def clear_tasks(user_id: int) -> None:
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('DELETE FROM tasks WHERE user_id = ?', (user_id,))
        await db.commit()

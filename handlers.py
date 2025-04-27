from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database import add_task, get_tasks, clear_tasks
from states import TaskStates

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'Привет! 👋\n'
        'Я бот для управления задачами.\n\n'
        'Доступные команды:\n'
        '/add - добавить задачу\n'
        '/list - посмотреть задачи\n'
        '/clear - удалить все задачи'
    )


@router.message(Command('add'))
async def cmd_add(message: Message, state: FSMContext):
    await message.answer('Напиши текст задачи:')
    await state.set_state(TaskStates.waiting_for_task)


@router.message(TaskStates.waiting_for_task, F.text)
async def process_task(message: Message, state: FSMContext):
    await add_task(message.from_user.id, message.text)
    await message.answer('✅ Задача добавлена!')
    await state.clear()


@router.message(Command('list'))
async def cmd_list(message: Message):
    tasks = await get_tasks(message.from_user.id)
    if not tasks:
        await message.answer('У тебя пока нет задач 😌')
    else:
        text = '\n'.join(f'{idx+1}. {task[1]}' for idx, task in enumerate(tasks))
        await message.answer(f'📋 Твои задачи:\n{text}')


@router.message(Command('clear'))
async def cmd_clear(message: Message):
    await clear_tasks(message.from_user.id)
    await message.answer('🗑️ Все задачи удалены!')


@router.message()
async def fallback(message: Message):
    await message.answer(
        '❗ Я не понимаю это сообщение.\nИспользуй команды: /add, /list, /clear'
    )

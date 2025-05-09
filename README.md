# 📝 Todo Telegram Bot

Простой и понятный Telegram-бот для управления личными задачами.  
Разработан на `aiogram` с использованием `SQLite` для хранения данных.

---

## 📦 Функционал

- `/start` — приветственное сообщение и список команд
- `/add` — добавить новую задачу
- `/list` — посмотреть список своих задач
- `/clear` — удалить все свои задачи

Все задачи сохраняются в базе данных, поэтому не теряются при перезапуске бота.

---

## 🚀 Быстрый старт

### 1. Клонируй проект

```bash
git clone git@github.com:justcr1si/to-do-telegram-bot.git
cd to-do-telegram-bot
```

### 2. Установи зависимости
```bash
pip install -r requirements.txt
```

### 3. Добавь свой BOT_TOKEN и DB_NAME в .env

### 4. Запусти бота
```bash
python bot.py
```
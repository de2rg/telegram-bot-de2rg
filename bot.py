
import telebot
from telebot import types
import sqlite3
import schedule
import time
import threading
from datetime import datetime, timedelta, date
import json
import re
import os

# Получаем токен из переменных окружения (для безопасности)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7960648611:AAG_eOK7wr6udWzRYO7FAOp2bERSKUBFa6A")
bot = telebot.TeleBot(BOT_TOKEN)

# Глобальный словарь для состояний пользователей
user_states = {}

class UserState:
    IDLE = "idle"
    ADDING_TASK = "adding_task"
    ADDING_RECURRING_TASK = "adding_recurring_task"
    UPLOADING_SCHEDULE = "uploading_schedule"
    SELECTING_DATE = "selecting_date"

# [Весь код бота остается тот же, только заменяем токен на переменную окружения]
# ... (здесь весь код из предыдущей версии)

# В конце добавляем для Railway:
if __name__ == "__main__":
    print("🚀 Инициализация бота на Railway...")
    init_db()
    print("💾 База данных подготовлена")

    # Запуск планировщика в отдельном потоке
    schedule_thread = threading.Thread(target=run_schedule)
    schedule_thread.daemon = True
    schedule_thread.start()
    print("⏰ Планировщик запущен")

    print("✅ Бот запущен на Railway и готов к работе!")
    print("🌅 Утренние уведомления будут приходить в 6:00")
    print("📱 Бот доступен 24/7 БЕСПЛАТНО на Railway!")

    # Для Railway используем infinity_polling вместо polling
    bot.infinity_polling(none_stop=True, interval=0, timeout=20)

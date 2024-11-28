from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import asyncio

# Укажите токен вашего бота
TOKEN = "7845488739:AAE9bKH6VI_CSx02H-QJlIwAAGMWYrEwQ8Q"

# Информация о студенте
STUDENT_INFO = {
    "name": "Футьянов Михаил Владимирович",
    "group": "РСБО-02-23",
    "profile_url": "https://t.me/mikefdsg"
}

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создание клавиатуры
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/info")],
        [KeyboardButton(text="/profile")]
    ],
    resize_keyboard=True
)

# Обработчик команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    welcome_text = (
        "Добро пожаловать в бота!\n"
        "Используйте кнопки ниже:\n"
        "/info - Информация о студенте\n"
        "/profile - Ссылка на страницу студента"
    )
    await message.answer(welcome_text, reply_markup=keyboard)

# Обработчик команды /info
@dp.message(Command("info"))
async def send_info(message: types.Message):
    info_text = (
        f"ФИО: {STUDENT_INFO['name']}\n"
        f"Группа: {STUDENT_INFO['group']}"
    )
    await message.answer(info_text)

# Обработчик команды /profile
@dp.message(Command("profile"))
async def send_profile(message: types.Message):
    await message.answer(f"Страница студента: {STUDENT_INFO['profile_url']}")

# Эхо-бот (отвечает тем же текстом)
@dp.message()
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("""Здравствуйте. Это бот для психологической помощи людям, пострадавшим в результате войны.

Тут Вы можете написать свой вопрос. Он будет передан психологам анонимно.

Сформулируйте Ваш вопрос в одно сообщение. Вопрос можно задать не чаще, чем 1 раз в 8 часов. 

Ответы на часто задаваемые вопросы публикуются в канале: https://t.me/dushevniy2022

Чтобы задать вопрос просто введите его ниже".
""")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")

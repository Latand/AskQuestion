# Хендлеры, которые принимают нажатие на кнопку "Задать вопрос"
# и с помощью FSMContext переходит в состояние "Задать вопрос"
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.config import Config
from tgbot.keyboards.reply import confirm_keyboard, cancel_keyboard


async def ask_question(message: types.Message, state: FSMContext, config: Config):
    """
    Обработчик нажатия на кнопку "Отмена"
    """

    last_question_asked = (await state.get_data()).get("last_question_asked")
    if last_question_asked:
        delta_hours = (datetime.datetime.now() - last_question_asked).seconds / 3600
        if delta_hours < 8:
            await message.answer(f"Вы можете задать вопрос только раз в {config.misc.MIN_TIME_BETWEEN_QUESTIONS} часов."
                                 f"\n\n"
                                 f"Осталось {config.misc.MIN_TIME_BETWEEN_QUESTIONS - delta_hours:.0f} часов")
            if message.from_user.id in config.tg_bot.admin_ids:
                await message.answer("Вы можете задать вопрос в любое время, если вы администратор",
                                     reply_markup=types.ReplyKeyboardRemove())
            else:
                return

    await message.reply("Вы действительно хотите задать этот вопрос?", reply_markup=confirm_keyboard())
    await state.update_data({"question": message.text})
    await state.set_state("confirm_question")


async def process_question(message: types.Message, state: FSMContext, config: Config):
    """
    Обработчик ввода вопроса
    """
    question = (await state.get_data()).get("question")

    await state.finish()

    if message.text == "Да":
        await message.answer("Ваш вопрос отправлен в разработку. "
                             "\n\n"
                             "Следующий вопрос вы сможете задать не ранее чем через 8 часов",
                             reply_markup=types.ReplyKeyboardRemove())

        await message.bot.send_message(chat_id=config.tg_bot.group_id,
                                       text=question + "\n\n" + '#Вопрос')
        await state.update_data(last_question_asked=datetime.datetime.now())
        return
    elif message.text == "Нет":
        await message.answer('Вопрос не был задан, Введите новый вопрос, чтобы его задать',
                             reply_markup=types.ReplyKeyboardRemove())


def register_question_handlers(dp):
    """
    Регистрация обработчиков нажатия на кнопку "Задать вопрос"
    """
    dp.register_message_handler(ask_question)
    dp.register_message_handler(process_question, state="confirm_question")

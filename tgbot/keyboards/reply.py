from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def ask_question_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Задать вопрос")
            ]
        ],
        resize_keyboard=True,
    )


def confirm_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Да"),
                KeyboardButton(text="Нет")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder='Подтвердите действие'
    )


def cancel_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Отмена")
            ]
        ],
        resize_keyboard=True,
        input_field_placeholder="Введите вопрос или нажмите на кнопку отмены"
    )

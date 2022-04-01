from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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

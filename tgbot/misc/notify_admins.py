from tgbot.misc.broadcaster import broadcast


async def start_notify(bot, admin_ids):
    await broadcast(bot, admin_ids, 'Бот запущен!')

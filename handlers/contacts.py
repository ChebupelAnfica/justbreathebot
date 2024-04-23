from aiogram import F, types

import keyboards.inline.close
from loader import dp, bot
import logging


@dp.message(F.text == 'Служба заботы 🫂')
async def contact(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await message.answer("При любых трудностях о вас всегда позаботятся тут @koskoangelina",
                             reply_markup=keyboards.inline.close.close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
        pass

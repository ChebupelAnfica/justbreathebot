from aiogram import F, types

import keyboards.inline.close
from loader import dp, bot
import logging

photo_id = "AgACAgIAAxkBAAIDC2YEiOyDMSaYXxs-btBJrsvFC10cAAKy3DEbdUshSCpckghQJG_tAQADAgADcwADNAQ"

text_about = f"""<b>Давайте познакомимся поближе🫂</b>
Меня зовут Ангелина Кошко - я специалист по здоровой работе с телом и движением более 13 лет.
⠀
С чего все началось?
С 7 лет я занималась профессиональным спортом, но когда я в первый раз попала на фитнес, внутри меня - вот оно, то чем хочу заниматься.
⠀
Закончила спортивный вуз, проходила разные мировые семинары, мастер-классы по современному подходу к движению у гуру в фитнесе.
⠀
Когда горишь своим делом, останавливаться не хочется! Особенно, когда в твоем теле поменялось все на 180 градусов.
⠀
Когда живот не нужно втягивать, он сам остаётся подтянутым, благодаря осанке, ягодицы могут гореть огнем даже лёжа на спине, а гулять можно хоть по 15 км в день и никакой боли в спине и усталости.
⠀
<u>И эту радость свободного и легкого движения я хочу подарить вам</u>💖
⠀
Возможность быть активными на долгие годы без болей, ограничений, с красивым упругим телом, жить полноценной жизнью!
⠀
И только так я строю свои тренировки - с заботой и вниманием к вашему телу в онлайн клубе «Just Breathe»✨"""


@dp.message(F.text == "Обо мне 🧘‍♀️")
async def send_photo(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await bot.send_photo(message.chat.id, photo_id, caption=text_about,
                             reply_markup=keyboards.inline.close.close_inline_keyboard)
    except Exception as ex:
        logging.error(ex)
        pass

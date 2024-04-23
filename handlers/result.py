from aiogram import F, types
from aiogram.types import InputMediaPhoto

import keyboards
from loader import dp, bot
import logging
from aiogram.fsm.context import FSMContext

text_about = f'''О клубе и его направлениях 

Клуб - это то самое место, где люди со всего мира получают результат >>> подтянутое, гибкое и функциональное тело, уйму удовольствия и кайфа во время и после тренировок.

Всего за 35-40 минут в день мы улучшаем осанку, убираем выпирающий живот, округляем ягодицы и повышаем уверенность в себе✨

▫️здесь можно заниматься в любое время
▫️в абонементе доступны более 70 тренировок 
▫️новые тренировки выходят 3 раза в неделю 
▫️от меня ты получишь поддержку по любым вопросам 
▫️тренировка в прямом эфире для корректной техники упражнений раз в неделю 
💔бонусы короткие зарядки от зажимов и отеков в теле, вебинары от нутрициолога, психолога, книга рецептов

Направления клуба:

🌿В понедельник тебя ждёт функциональная работа для прокачки ягодиц, мышц пресса, и улучшения выносливости всего тела 

🌿В среду тренировка для включения мышц живота, улучшаем функцию дыхания, работаем с подвижностью позвоночника, мышцами тазового дна

🌿В пятницу функциональная тренировка на осанку, где уделяем внимание спине, плечам, лопаткам и мышцами живота 

Всегда использую комплексный подход в теле и разные техники: силовая, растяжка, йога, пилатес, мфр, функциональные

*Пробное занятие
*Ежемесячная подписка👇🏻

🌿Выбери тарифный план 

▫️1 месяц 130BYN/40$
▫️3 месяца 275 BYN/85$
▫️6 месяцев 535 BYN/165$

Выберите необходимый, нажав на соответствующую кнопку👇🏻'''

photo_id1 = "AgACAgIAAxkBAAMvZft4ybXIbZEYaWGyb90TMOOPQlUAAqTbMRuSO9lLJWZct9-uDZQBAAMCAANzAAM0BA"
photo_id2 = "AgACAgIAAxkBAAMxZft42D94GdoXMeRzlcKxVAH4WKoAAqPbMRuSO9lLrpm0V_MAAQmTAQADAgADcwADNAQ"
photo_id3 = "AgACAgIAAxkBAAMzZft46WfVJ1aIBybo-hjLMi1KkLUAAqLbMRuSO9lLELVivGmKyvIBAAMCAANzAAM0BA"
photo_id4 = "AgACAgIAAxkBAAM1Zft49lj2wfAzH727RFKBAjTmEV0AAqHbMRuSO9lLqHrF82zZAAHqAQADAgADcwADNAQ"
photo_id5 = "AgACAgIAAxkBAAM3Zft5BGwAAXvh4bOQ1fiydlKK9FVwAAKg2zEbkjvZSxRvyKNaRExcAQADAgADcwADNAQ"


@dp.message(F.text == "Результаты")
async def reviews(message: types.Message):
    media = [
        InputMediaPhoto(media=photo_id1),
        InputMediaPhoto(media=photo_id2),
        InputMediaPhoto(media=photo_id3),
        InputMediaPhoto(media=photo_id4),
        InputMediaPhoto(media=photo_id5)
    ]
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await bot.send_media_group(message.chat.id, media)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await bot.send_message(message.chat.id,
                               text="''Так же если впечетлены проделанной работай и хотите присоедиться к нам⤵️''",
                               reply_markup=keyboards.inline.result.connection)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'connection')
async def process_callback1(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(
                text_about,
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                reply_markup=keyboards.inline.pay.pay
            )
    except Exception as ex:
        logging.error(ex)
        pass

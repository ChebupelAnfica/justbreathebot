from aiogram import F, types
from loader import dp, bot
import logging
import keyboards

text_about_club = f"""Клуб - это то самое место, где люди со всего мира получают результат >>> <u>подтянутое, гибкое и функциональное тело, уйму удовольствия и кайфа во время и после тренировок.</u>

Всего за 35-40 минут в день мы улучшаем осанку, убираем выпирающий живот, округляем ягодицы и повышаем уверенность в себе✨

🔸здесь можно заниматься в любое время
🔸в абонементе уже доступны более 70 тренировок 
🔸новые тренировки выходят 3 раза в неделю 
🔸от меня ты получишь поддержку по любым вопросам 
🔸тренировка в прямом эфире для корректной техники упражнений раз в неделю 
💔бонусы: короткие зарядки от зажимов и отеков в теле, вебинары от нутрициолога, психолога, книга рецептов.

Направления клуба:

🌿В понедельник тебя ждёт функциональная работа для прокачки ягодиц, мышц пресса, и улучшения выносливости всего тела 

🌿В среду тренировка для включения мышц живота, улучшаем функцию дыхания, работаем с подвижностью позвоночника, мышцами тазового дна

🌿В пятницу функциональная тренировка на осанку, где уделяем внимание спине, плечам, лопаткам и мышцами живота 

<u>Всегда использую комплексный подход в теле и разные техники: силовая, растяжка, йога, пилатес, мфр, функциональные</u>

🌿Выбери тарифный план 

🔸1 месяц 130BYN/40$
🔸3 месяца 275 BYN/85$
🔸6 месяцев 535 BYN/165$

Если оплата не белорусской и российской картой, напишите мне 

Выберите необходимый, нажав на соответствующую кнопку👇🏻"""


@dp.message(F.text == "О клубе и направлениях🌿")
async def contact(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await message.answer(text_about_club,
                             reply_markup=keyboards.inline.pay.pay)
    except Exception as ex:
        logging.error(ex)
        pass

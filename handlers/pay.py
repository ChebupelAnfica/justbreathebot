import keyboards
from aiogram import F, types
import keyboards.inline.questions
from loader import dp, bot
from aiogram.fsm.context import FSMContext
import logging


@dp.callback_query(F.data == 'level1')
async def pay1(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(
                text='''1 месяц 130BYN/40$''',
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                reply_markup=keyboards.inline.pay.pay_button
            )
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'level2')
async def pay2(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(
                text=f'''3 месяца 275 BYN/85$''',
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                reply_markup=keyboards.inline.pay.pay_button
            )
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'level3')
async def pay3(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(
                text=f'''6 месяцев 535 BYN/165$''',
                chat_id=call.from_user.id,
                message_id=call.message.message_id,
                reply_markup=keyboards.inline.pay.pay_button
            )
    except Exception as ex:
        logging.error(ex)
        pass

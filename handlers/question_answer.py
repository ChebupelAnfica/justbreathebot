from aiogram import F, types

import keyboards.inline.questions

from loader import dp, bot
from aiogram.fsm.context import FSMContext
import logging


@dp.message(F.text == "Ответы на вопросы🧠")
async def question(message: types.Message):
    try:
        await bot.delete_message(message.from_user.id, message.message_id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await message.answer(f"""Часто задаваемые вопросы и ответы на них""",
                             reply_markup=keyboards.inline.questions.questions)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions1')
async def process_callback1(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(text=f'''Какой уровень?

Подойдет новичкам и опытным! Я предлагаю разные уровни сложности. Поверьте, будет интересно, понятно и доступно.''',
                                        chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=keyboards.inline.questions.back_to_questions)
    except Exception as ex:
        logging.error(ex)
        pass


@dp.callback_query(F.data == 'questions2')
async def process_callback2(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(text=f'''Сколько стоит?

▫️1 месяц 130BYN/40$
▫️3 месяца 275 BYN/85$
▫️6 месяцев 535 BYN/165$''', chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=keyboards.inline.questions.back_to_questions)
    except Exception as ex:
        logging.error(ex)


@dp.callback_query(F.data == 'questions3')
async def process_callback3(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(text=f'''Что мне нужно для тренировок?

<b>В клубе много тренировок без оборудования, но все-таки стоит приобрести:</b> пенный ролл, 2 теннисных мяча, мяч для пилатеса 25-30 см, фитнес лента для пилатеса, фитнес 
резинки, гантели 2 кг.

<u>Длительность тренировок:</u> занятия идут не более 45 минут, есть короткие тренировки по 15-20 минут.''',
                                        chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=keyboards.inline.questions.back_to_questions)
    except Exception as ex:
        logging.error(ex)


@dp.callback_query(F.data == 'questions4')
async def process_callback4(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(text=f'''Как ориентироваться в канале?

В канале есть хэштеги («руки»,«ноги» и т.д.), чтобы вам было удобно сориентироваться и приветственное видео, где я еще раз подробно все рассказываю. Вы точно не потеряетесь.''',
                                        chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=keyboards.inline.questions.back_to_questions)
    except Exception as ex:
        logging.error(ex)


@dp.callback_query(F.data == 'questions5')
async def process_callback5(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        if call.message:
            await bot.edit_message_text(text=f'''Что за тренировка в прямом эфире?

Тренировку провожу раз в неделю, чтобы улучшить технику и вы более увереннее себя чувствовали, когда тренируетесь в записи❤️
''',
                                        chat_id=call.from_user.id,
                                        message_id=call.message.message_id,
                                        reply_markup=keyboards.inline.questions.back_to_questions)
    except Exception as ex:
        logging.error(ex)


@dp.callback_query(F.data == 'back_to_all_questions')
async def process_back(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    try:
        await bot.answer_callback_query(call.id)
    except Exception as ex:
        logging.error(ex)
        pass
    try:
        await bot.edit_message_text(f"Часто задаваемые вопросы и ответы на них",
                                    call.from_user.id,
                                    call.message.message_id,
                                    reply_markup=keyboards.inline.questions.questions)
    except Exception as ex:
        logging.error(ex)

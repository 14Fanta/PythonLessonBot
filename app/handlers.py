from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import Bot,Dispatcher,Router, F
import sqlite3 as s

import app.keyboard as kb
from util import *
from app.state import *
from config import TOKEN_TG

Channel = "@Chernovikck"

bot = Bot(token=TOKEN_TG)
dp = Dispatcher()

db = s.connect("users.db")
cur = db.cursor()

user_router = Router()

questions = [
         {
             "question_1": "What is a variable in programming?",
             "answers_1": [
                 "1. A variable is a function that performs operations.",
                 "2. A variable is a named memory location that stores a value.",
                 "3. A variable is a data type used in programming languages.",
                 "4. A variable is a syntax construct for creating loops."
             ]
         },
         {
             "question_2": "What is a data type in programming?",
             "answers_2": [
                 "1. A data type is a method for sorting data.",
                 "2. A data type is a function that processes data.",
                 "3. A data type is a classification that specifies the type of data a variable can hold.",
                 "4. A data type is a syntax error in code."
             ]
         },
        {
    "question_3": "What is an array in programming?",
    "answers_3": [
        "1. An array is a collection of variables of different types.",
        "2. An array is a sequence of characters forming a string.",
        "3. An array is a fixed-size sequential collection of elements of the same type.",
        "4. An array is a special kind of loop structure."
    ]
},
{
    "question_4": "What is a loop in programming?",
    "answers_4": [
        "1. A loop is a way to store data temporarily.",
        "2. A loop is a control flow statement that allows code to be executed repeatedly based on a given condition.",
        "3. A loop is a function that returns a single value.",
        "4. A loop is a data structure used to organize complex data."
    ]
},
{
    "question_5": "What is a function in programming?",
    "answers_5": [
        "1. A function is a block of code designed to perform a specific task and optionally return a result.",
        "2. A function is a set of rules for formatting code.",
        "3. A function is a special type of comment in source code.",
        "4. A function is a way to declare global variables."
    ]
},
{
    "question_6": "What is a conditional statement in programming?",
    "answers_6": [
        "1. A conditional statement is a command to start or stop a program execution.",
        "2. A conditional statement is a piece of code that executes only if a certain condition is met.",
        "3. A conditional statement is a syntax error that causes compilation failure.",
        "4. A conditional statement is a method for organizing data into tables."
    ]
},
{
    "question_7": "What is a class in object-oriented programming?",
    "answers_7": [
        "1. A class is a blueprint or template from which objects are created.",
        "2. A class is a collection of unrelated functions grouped together.",
        "3. A class is a special type of loop structure.",
        "4. A class is a type of syntax error."
    ]
},
{
    "question_8": "What is inheritance in object-oriented programming?",
    "answers_8": [
        "1. Inheritance is a mechanism where one class acquires the properties and behaviors of another class.",
        "2. Inheritance is a way to define new data types.",
        "3. Inheritance is a feature that allows multiple programs to run simultaneously.",
        "4. Inheritance is a debugging tool used to find errors in code."
    ]
},
{
    "question_9": "What is polymorphism in object-oriented programming?",
    "answers_9": [
        "1. Polymorphism is the ability of an object to take on many forms.",
        "2. Polymorphism is a technique for optimizing code performance.",
        "3. Polymorphism is a way to prevent unauthorized access to data.",
        "4. Polymorphism is a method for converting data types."
    ]
},
{
    "question_10": "What is encapsulation in object-oriented programming?",
    "answers_10": [
        "1. Encapsulation is the bundling of data with methods that operate on that data, restricting direct access to them.",
        "2. Encapsulation is a process of compiling and linking code.",
        "3. Encapsulation is a form of encryption used to secure data.",
        "4. Encapsulation is a method for removing duplicate code."
    ]
}

     ]

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, last_name TEXT,user_id INTEGER, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, lesson INTEGER)")

@user_router.message(Command("help"))
async def cmd_help(message: Message)->None:
    help_message = (
        "<b>Help - List of commands:</b>\n"
        "/start - Start the bot\n"
        "/help - Get help\n"
        "/ask - FAQ\n"
        "/materials - Video materials📹"
    )
    await message.answer(help_message, parse_mode='HTML')

@user_router.message(Command("ask"))
async def cmd_ask(message:Message)->None:
    await message.answer("Here are the most frequently asked questions in Python:",
                          reply_markup=kb.FAQ_OF_Python())

@user_router.message(CommandStart())
async def cmd_start(message:Message)->None:
    user = cur.execute(f"""SELECT user_id FROM users WHERE user_id = ? """,
                        (message.from_user.id,)).fetchone()
    if not user:
        cur.execute(
            "INSERT INTO users (username,first_name,last_name, user_id, created_at) VALUES (?,?,?,?,?)",
        (   message.from_user.username,message.from_user.first_name,
            message.from_user.last_name,message.from_user.id,message.date,
        )
         )
        db.commit()
        hello_message = "<b>Hello! I'm a bot</b>\n"
        hello_message += "If you want to get a list of commands and to begin learning IT Python you need to subscribe my channel\n"
        await bot.send_message(
            message.from_user.id, hello_message, parse_mode='HTML',
            reply_markup=kb.check_subscription()
        )
    elif user:
        user_subscription = await bot.get_chat_member(chat_id= Channel, user_id=message.from_user.id)
        if user_subscription.status != 'left':
            text = "<b>Hello! I'm a bot</b> ✅\n/help - Get help\n/start - Start the bot\n/ask - FAQ\n/materials - video materials\nYou are subscribed to the channel. You can use all commands and to begin learning Python "
            await bot.send_message(message.from_user.id, text= text,parse_mode= "HTML", reply_markup=kb.learning())
        else:
            text = "You aren't subscribed to the channel. For continue you need to subscribe👀"
            await bot.send_message(message.from_user.id, text= text,
                                reply_markup= kb.Subscribe())

@user_router.callback_query(F.data == 'follow_check')
async def subscribe_check(callback:CallbackQuery)->None:
    await callback.answer("сhecking subscription")
    user = cur.execute(f"""SELECT user_id FROM users WHERE user_id = ? """,
                        (callback.message.from_user.id,)).fetchone()
    user_subscription = await bot.get_chat_member(chat_id= Channel, user_id=callback.from_user.id)
    if user_subscription.status != 'left':
        text = "<b>Hello! I'm a bot</b> ✅\n/help - Get help\n/start - Start the bot\n/ask - FAQ\n/materials - video materials\nYou are subscribed to the channel. You can use all commands and to begin learning Python "
        await bot.send_message(callback.from_user.id, text= text,parse_mode= "HTML", reply_markup=kb.learning())
    else:
        text = "You aren't subscribed to the channel. For continue you need to subscribe👀"
        await bot.send_message(callback.from_user.id, text= text,
                             reply_markup= kb.Subscribe())

@user_router.callback_query(F.data == "Lesson_1")
async def lsn_01(callback:CallbackQuery)->None:
    await callback.answer("Lesson 1")
    text = load_message("text")
    await callback.message.answer(text=text)

@user_router.message(F.text == "Begin lesson📘")
async def to_begin_first_lesson(message:Message,state:FSMContext) ->None:
    cur.execute(f"UPDATE users SET lesson = 1 WHERE user_id = {message.from_user.id}")
    db.commit()
    await message.answer("Okay! Let's start to learning Python.")
    photo_python ="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fit-blog.ru%2Fwp-content%2Fuploads%2F2020%2F05%2Fpython1.jpg&lr=35&pos=13&rpt=simage&text=photo%20Python"
    caption_python = "Lesson 1/10. Variables"
    await bot.send_photo(
                         message.from_user.id,
                         photo=photo_python,
                         caption=caption_python,
                         reply_markup=kb.LS_1() 
                         )

    
    await message.answer(
        "Take the quiz now)", 
        )
    
@user_router.callback_query(F.data == "Quiz_1")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    await callback.answer("Quiz")
    question_text = questions[0]["question_1"]
    answers = "\n".join(questions[0]["answers_1"])
    await callback.message.answer(f"{question_text}\n{answers}\nSelect the correct answer", parse_mode='HTML',reply_markup=kb.answer())
    await state.set_state(wait.wait_a_message)

@user_router.message(wait.wait_a_message)
async def answer_get(message: Message, state: FSMContext):
    print("1")
    await state.update_data(wait_a_message=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message')

    if answer in ['1', '3', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 2.\nTo continue, click 'I passed'",
            parse_mode="HTML",
            reply_markup=kb.passed()
        )
    elif answer == '2':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'I passed'",
            parse_mode="HTML",
            reply_markup=kb.passed()
        )
    else:
        await message.answer("Choose the right number.")
    await state.clear()
    
@user_router.message(F.text == "I passed")
async def passed(message:Message,state:FSMContext) -> None:
    cur.execute(f"UPDATE users SET lesson = 2 WHERE user_id = {message.from_user.id}")
    db.commit()
    await state.update_data(wait_a_message=message.text)
    await message.answer("Good job! Let's continue! ")    
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Ffikiwiki.com%2Fuploads%2Fposts%2F2022-02%2F1644837320_14-fikiwiki-com-p-kartinki-pitoni-14.jpg&lr=35&pos=7&rpt=simage&text=photo%20python" 
    caption_python = "Lesson 2/10. Data entry and types. "
    await bot.send_photo(
                         message.from_user.id,
                         photo=photo_python,
                         caption=caption_python,
                         reply_markup=kb.LS_2() 
                         )
    await bot.send_message(message.from_user.id, "The 'Lesson' tab contains both practice and theory. After do quiz")
    await message.answer(
        "Take the quiz now", 
        )
    
@user_router.callback_query(F.data == "Quiz_2")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):

    question_text = questions[1]["question_2"]
    answers = "\n".join(questions[1]["answers_2"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_answer)

@user_router.message(wait.wait_a_answer)
async def answer_get(message: Message, state: FSMContext):
    await state.update_data(wait_a_answer=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_answer')

    if answer in ['1', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_2()
        )
    elif answer == '3':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_2()
        )
    else:
        await message.answer("Choose the right number.")
    await state.clear()

@user_router.callback_query(F.data == "done_2")
async def done_task(callbackQuery:CallbackQuery,state:FSMContext)->None:
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 3 WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(callbackQuery.message.from_user.id)
    print(callbackQuery.from_user.id)
    await callbackQuery.message.answer("WOW! You're well done😲👍!")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fsabyna.ru%2Fwp-content%2Fuploads%2F2023%2F03%2F388.jpg&lr=35&pos=35&rpt=simage&text=photo%20python" 
    caption_python = "Lesson 3/10. Operators if-else. "
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,
                         reply_markup=kb.LS_3() 
                         )
    
@user_router.callback_query(F.data == "Quiz_3")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    question_text = questions[2]["question_3"]
    answers = "\n".join(questions[2]["answers_3"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message1)

@user_router.message(wait.wait_a_message1)
async def answer_get1(message: Message, state: FSMContext):
    print("3")
    await state.update_data(wait_a_message1=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message1')

    if answer in ['1', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_3()
        )
    elif answer == '3':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_3())      
    else:
        await message.answer("Choose the right number.")
    await state.clear()

@user_router.callback_query(F.data ==  "done_3")
async def done_task4(callbackQuery:CallbackQuery,state:FSMContext)->None:
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 4 WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("Next lesson!😀")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FCfWLtMPVIAEDaSQ.jpg&lr=35&pos=40&rpt=simage&text=code%20oython%27"
    caption_python = "Lesson 4/10. Conditional while loop."
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_4() 
                         )
    
@user_router.callback_query(F.data == "Quiz_4")
async def Quiz_4(callback:CallbackQuery,state:FSMContext):

    question_text = questions[3]["question_4"]
    answers = "\n".join(questions[3]["answers_4"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message2)

@user_router.message(wait.wait_a_message2)
async def answer_get1(message: Message, state: FSMContext):
    print("4")
    await state.update_data(wait_a_message2=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message2')

    if answer in ['1', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_4()
        )
    elif answer == '3':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_4())      
    else:
        await message.answer("Choose the right number.")
    await state.clear()

@user_router.callback_query(F.data ==  "done_4")
async def done_task3(callbackQuery:CallbackQuery,state:FSMContext):
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 5 WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("We continue!🙂")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fwww.malagasy.biz%2Fwp-content%2Fuploads%2F2018%2F11%2Fprogramming-code.jpg&lr=35&pos=29&rpt=simage&text=code%20oython%27"
    caption_python = "Lesson 5/10. Data types."
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_5() 
                         )
    
@user_router.callback_query(F.data == "Quiz_5")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    question_text = questions[4]["question_5"]
    answers = "\n".join(questions[4]["answers_5"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message3)

@user_router.message(wait.wait_a_message3)
async def answer_get1(message: Message, state: FSMContext):
    print("5")
    await state.update_data(wait_a_message3=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message3')

    if answer in ['3', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_5()
        )
    elif answer == '1':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_5())      
    else:
        await message.answer("Choose the right number.")
    await state.clear()

@user_router.callback_query(F.data ==  "done_5")
async def done_task5(callbackQuery:CallbackQuery,state:FSMContext):
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 6 WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("💛//...//💛")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fschtirlitz.ru%2F800%2F600%2Fhttp%2Fcf.ppt-online.org%2Ffiles%2Fslide%2Fq%2FQClKoDgJ4u0AjUydmp286YSrWEatnVs9cxGIfT%2Fslide-26.jpg&lr=35&p=1&pos=3&rpt=simage&text=cycle%20for%20python"
    caption_python = "Lesson 6/10. Cycle FOR."
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_6() 
                         )
    
@user_router.callback_query(F.data == "Quiz_6")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    question_text = questions[5]["question_6"]
    answers = "\n".join(questions[5]["answers_6"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message4)

@user_router.message(wait.wait_a_message4)
async def answer_get1(message: Message, state: FSMContext):
    print("6")
    await state.update_data(wait_a_message4=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message4')

    if answer in ['3', '1', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_6()
        )
    elif answer == '2':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_6())      
    else:
        await message.answer("Choose the right number.")
    await state.clear()


@user_router.callback_query(F.data ==  "done_6")
async def done_task6(callbackQuery:CallbackQuery,state:FSMContext):
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 7  WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("🌹//_//🌹")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fskilsful.com%2Fwp-content%2Fuploads%2F2021%2F03%2F1_RJMxLdTHqVBSijKmOO5MAg-2048x1219.jpeg&lr=35&pos=19&rpt=simage&text=photo%20Python%20"
    caption_python = "Lesson 7/10. Data processing"
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_7() 
                         )
    
@user_router.callback_query(F.data == "Quiz_7")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    question_text = questions[6]["question_7"]
    answers = "\n".join(questions[6]["answers_7"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message5)

@user_router.message(wait.wait_a_message5)
async def answer_get1(message: Message, state: FSMContext):
    print("6")
    await state.update_data(wait_a_message5=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message5')

    if answer in ['3', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_7()
        )
    elif answer == '1':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_7())    
    else:
        await message.answer("Choose the right number.")
    await state.clear()

@user_router.callback_query(F.data ==  "done_7")
async def done_task7(callbackQuery:CallbackQuery,state:FSMContext):
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 8  WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("There's not much left🥍 ")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fwww.levober.ru%2Fpub%2Fimg%2Fcourses%2F287%2Fpreview.png&lr=35&p=2&pos=2&rpt=simage&text=photo%20Python"
    caption_python = "Lesson 8/10. Functions"
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_8(),
                         parse_mode="HTML"
                         )
    
@user_router.callback_query(F.data == "Quiz_8")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    question_text = questions[7]["question_8"]
    answers = "\n".join(questions[7]["answers_8"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message6)

@user_router.message(wait.wait_a_message6)
async def answer_get1(message: Message, state: FSMContext):
    print("6")
    await state.update_data(wait_a_message6=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message6')

    if answer in ['3', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_8()
        )
    elif answer == '1':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_8())      
    else:
        await message.answer("Choose the right number.")
    await state.clear()

@user_router.callback_query(F.data ==  "done_8")
async def done_task8(callbackQuery:CallbackQuery,state:FSMContext):
    await callbackQuery.answer("Done✔️")
    cur.execute(f"UPDATE users SET lesson = 9  WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("The last lesson📚 ")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi.imgur.com%2FrOVqQv7.jpg&lr=35&p=2&pos=44&rpt=simage&text=photo%20Python%20modles%20lesson"
    caption_python = "Lesson 9/10. Modules"
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_9(),
                         parse_mode="HTML"
                         )
    
@user_router.callback_query(F.data == "Quiz_9")
async def Quiz_1(callback:CallbackQuery,state:FSMContext):
    question_text = questions[8]["question_9"]
    answers = "\n".join(questions[8]["answers_9"])
    await callback.message.answer(
                            f"{question_text}\n{answers}\nSelect the correct answer",
                            parse_mode='HTML',
                            reply_markup=kb.answer()
                          )
    await state.set_state(wait.wait_a_message7)

@user_router.message(wait.wait_a_message7)
async def answer_get1(message: Message, state: FSMContext):
    print("9")
    await state.update_data(wait_a_message7=message.text.strip())
    data = await state.get_data()
    answer = data.get('wait_a_message7')

    if answer in ['3', '2', '4']:
        await message.answer(
            "<b>The answer is wrong</b>\nRight answer is 3.\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_9()
        )
    elif answer == '1':
        await message.answer(
            "<b>The answer is correct</b>\nTo continue, click 'Done'",
            parse_mode="HTML",
            reply_markup=kb.Done_9())      
    else:
        await message.answer("Choose the right number.")
    await state.clear()


@user_router.callback_query(F.data ==  "done_9")
async def done_task9(callbackQuery:CallbackQuery,state:FSMContext):
    await callbackQuery.answer("Done✔️")
    text = load_message("conclusion")
    cur.execute(f"UPDATE users SET lesson = 10 WHERE user_id = {callbackQuery.from_user.id}")
    db.commit()
    print(f"{callbackQuery.message.from_user.id} - message.from_user.id")
    print(f"{callbackQuery.from_user.id} - from_user.id")
    await callbackQuery.message.answer("Hooray.🎊🎉 Have you completed all the lessons🎉")
    photo_python = "https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fi0.wp.com%2Fimg.artrabbit.com%2Fevents%2Fand-per-se-and-part-i-mark-wallinger-the-end%2Fimages%2Fr6QsbcMUHXUf%2F1500x1042%2FThe-End-2006-35mm-film-projection-12mins.jpg%3Fssl%3D1&lr=35&pos=3&rpt=simage&text=The%20end"
    caption_python = "Lesson 10/10. Conclusion"
    await bot.send_photo(
                         callbackQuery.from_user.id,
                         photo=photo_python,
                         caption=caption_python,                     
                         reply_markup=kb.LS_10(),
                         parse_mode="HTML"
                         )
    await callbackQuery.message.answer(text=text,parse_mode="HTML")
    await callbackQuery.message.answer(
    "<b>I hope that you have completed all the tasks that I have given you.</b>",parse_mode="HTML"
     )

@user_router.callback_query(F.data == "repeat")
async def to_begin_first_lesson(message:Message,state:FSMContext):
    cur.execute(f"UPDATE users SET lesson = 1 WHERE user_id = {message.from_user.id}")
    db.commit()
    await message.answer("Okay! Let's start to learning Python.")
    photo_python ="https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fit-blog.ru%2Fwp-content%2Fuploads%2F2020%2F05%2Fpython1.jpg&lr=35&pos=13&rpt=simage&text=photo%20Python"
    caption_python = "Lesson 1/10. Variables"
    await bot.send_photo(
                         message.from_user.id,
                         photo=photo_python,
                         caption=caption_python,
                         reply_markup=kb.LS_1() 
                         )
    await message.answer(
        "In the assignment department, complete the first 8 assignments and write to me 'I passed'.",
         reply_markup=kb.passed()
        )
    await state.set_state(wait.wait_a_message)

@user_router.callback_query(F.data == "lESSON_2")
async def lsn_02(callback:CallbackQuery):
    await callback.answer("Lesson 2")
    text = load_message("text1")
    await callback.message.answer(text=text)

@user_router.callback_query(F.data == "WTISPY")
async def WISPY(callback:CallbackQuery):
    await callback.answer("What is Python?")
    text = load_message("FAQ_1")
    await bot.send_message(chat_id=callback.from_user.id, text=text,reply_markup=kb.more_WTISPY())

@user_router.callback_query(F.data == "WTISPYSF")
async def WISPY(callback:CallbackQuery):
    text = load_message("FAQ_2")
    await callback.answer("What is the Python Software Foundation")
    await bot.send_message(chat_id=callback.from_user.id, text=text)

@user_router.callback_query(F.data == "ATHCORESONTHEUSEOPYTHON")
async def WISPY(callback:CallbackQuery):
    text = load_message("FAQ_3")
    await callback.answer("Are there copyright restrictions...?")
    await bot.send_message(
                           chat_id=callback.from_user.id,
                           text=text,
                           reply_markup=kb.more_ATHCORESONTHEUSEOPYTHON()
                           )
    
@user_router.callback_query(F.data == "FIRPLACE")
async def WISPY(callback:CallbackQuery):
    text = load_message("FAQ_4")
    await callback.answer("Why was Python created...?")
    await bot.send_message(
                           chat_id=callback.from_user.id,
                           text=text,
                           parse_mode="HTML"
                           )
    
@user_router.callback_query(F.data == "GOODFOR")
async def WISPY(callback:CallbackQuery):
    text = load_message("FAQ_5")
    await callback.answer("What is Python good for?")
    await bot.send_message(
                           chat_id=callback.from_user.id,
                           text=text,
                           parse_mode="HTML",
                           reply_markup=kb.more_GOODFOR()
                           )

@user_router.callback_query(F.data == "SCHEMEWORK")
async def WISPY(callbackQuery: CallbackQuery):
    text = load_message("FAQ_6")
    await callbackQuery.answer("How does the Python version numbered...?")
    await bot.send_message(
                           chat_id=callbackQuery.from_user.id,
                           text=text,
                           parse_mode="HTML",reply_markup=kb.SCHEMEWORK()
                           )
    
@user_router.callback_query(F.data == "OBTAIN")
async def WISPY(callbackQuery: CallbackQuery):
    text = load_message("FAQ_7")
    await callbackQuery.answer("How do I obtain a copy...?")
    await bot.send_message(
                           chat_id=callbackQuery.from_user.id,
                           text=text,
                           parse_mode="HTML",reply_markup=kb.OBTAIN()
                           )
    
@user_router.callback_query(F.data == "DOCS")
async def WISPY(callbackQuery: CallbackQuery):
    text = load_message("FAQ_8")
    await callbackQuery.answer("How do I get doc...?")
    await bot.send_message(
                           chat_id=callbackQuery.from_user.id,
                           text=text,
                           parse_mode="HTML",reply_markup=kb.DOCS()
                           )
    
@user_router.callback_query(F.data == "BOOKS")
async def WISPY(callbackQuery: CallbackQuery):
    text = load_message("FAQ_9")
    await callbackQuery.answer("Are there any books on Python")
    await bot.send_message(
                           chat_id=callbackQuery.from_user.id,
                           text=text,
                           parse_mode="HTML",reply_markup=kb.BOOKS()
                           )
    
@user_router.callback_query(F.data == "CALLEDPYTHON")
async def WISPY(callbackQuery: CallbackQuery):
    text = load_message("FAQ_10")
    await callbackQuery.answer("Why is it called Python")
    await bot.send_message(
                           chat_id=callbackQuery.from_user.id,
                           text=text,
                           parse_mode="HTML",reply_markup=kb.CALLEDPYTHON()
                           )
    
@user_router.message(Command("materials"))
async def cmd_exist(message:Message):
    text = "Video clip materials:\n<b>1. Websites</b>\n1.1 Sudoteach\n1.2 TeacherArmy\n<b>2. Books for Beginners</b>:\n2.1 Python Crash Course by Eric Matthes\n2.2 Head First Python\n2.3 Python Cookbook: Recipes for Mastering Python\n<b>3. Video:</b>\n3.1 10 tips for a novice ae developer\n3.2 Your own VPN in 7 minutes\n3.3 INSTALLING PYTHON AND PYCHARM"
    await message.answer(
                            text= text,
                            reply_markup= kb.Video_clip_materials(),
                            parse_mode="HTML"
                         )

@user_router.message(Command("projects"))
async def projects(message:Message):
    await bot.send_message(chat_id= message.from_user.id, text= "<b>The simple projects for doing with manual:</b>",
                            reply_markup=kb.Projects(),
                            parse_mode= "HTML")

@user_router.callback_query(F.data == "Gallow")
async def projects(callback: CallbackQuery):
    await callback.answer("Gallow")
    text = load_message("Gallow")
    await bot.send_message(chat_id=callback.from_user.id,text= text, parse_mode="HTML")

@user_router.callback_query(F.data == "Calculator")
async def projects(callback: CallbackQuery):
    await callback.answer("Calculator")
    text = load_message("Calculator")
    await bot.send_message(chat_id=callback.from_user.id,text= text, parse_mode="HTML")

@user_router.callback_query(F.data == "to-do")
async def projects(callback: CallbackQuery):
    await callback.answer("TO-DO")
    text = load_message("TO-DO")
    await bot.send_message(chat_id=callback.from_user.id,text= text, parse_mode="HTML")

@user_router.callback_query(F.data == "converting")
async def projects(callback: CallbackQuery):
    await callback.answer("Converting")
    text = load_message("converting")
    await bot.send_message(chat_id=callback.from_user.id,text= text, parse_mode="HTML")

@user_router.callback_query(F.data == "palindromes")
async def projects(callback: CallbackQuery):
    await callback.answer("Palindromes")
    text = load_message("palindromes")
    await bot.send_message(chat_id=callback.from_user.id,text= text, parse_mode="HTML")

@user_router.message()
async def cmd_exist(message:Message):
    await message.answer("Command doesn't exist. Use /start to get a list of commands")
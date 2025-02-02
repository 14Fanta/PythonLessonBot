from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder

def check_subscription():
    builder = InlineKeyboardBuilder()
    builder.button(text= "Check subscribe☑️", callback_data= "follow_check")
    return builder.adjust(1).as_markup()

def Subscribe():
    builder = InlineKeyboardBuilder()
    builder.button(text= "Subscribe☺️", url= "t.me/Chernovikck")
    return builder.adjust(1).as_markup()

def more_WTISPY():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="more info🔖",
          url= "https://docs.python.org/3/tutorial/index.html#tutorial-index"
          )
    builder.button(
        text="more info📑",
          url= "https://wiki.python.org/moin/BeginnersGuide"
          )
    return builder.as_markup()

def more_ATHCORESONTHEUSEOPYTHON():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="the license pag✅",
          url= "https://docs.python.org/3/license.html"
          )
    builder.button(
        text="the trademark usage policy💛",
          url= "https://www.python.org/psf/trademarks/"
          )
    return builder.as_markup()

def more_GOODFOR():
    builder = InlineKeyboardBuilder()
    builder.button(
        text=" the python standard library♥️",
          url= "https://docs.python.org/3/library/index.html#library-index"
          )
    builder.button(
        text="the python package index♥️",
          url= "https://pypi.org/"
          )
    return builder.as_markup()

def FAQ_OF_Python():
    builder = InlineKeyboardBuilder()
    builder.button(text= "What is Python? ",callback_data="WTISPY")
    builder.button(text= "What is the Python Software Foundation? ",callback_data="WTISPYSF")
    builder.button(
                   text= "Are there copyright restrictions on the use of Python? ",
                   callback_data="ATHCORESONTHEUSEOPYTHON"
                   )
    builder.button(text= "Why was Python created in the first place?",callback_data="FIRPLACE")
    builder.button(text= "What is Python good for?",callback_data="GOODFOR")
    builder.button(
                   text= "How does the Python version numbering scheme work?",
                   callback_data="SCHEMEWORK"
                   )
    builder.button(text= "How do I obtain a copy of the Python source?",callback_data="OBTAIN")
    builder.button(text= "How do I get documentation on Python?",callback_data="DOCS")
    builder.button(text= "Are there any books on Python? ",callback_data="BOOKS")
    builder.button(text= "Why is it called Python?",callback_data="CALLEDPYTHON")
    return builder.adjust(1).as_markup()

def CALLEDPYTHON():
    builder = InlineKeyboardBuilder()
    builder.button(
        text= " “Monty Python’s Flying Circus”",
          url= "https://en.wikipedia.org/wiki/Monty_Python"
          )
    return builder.adjust(1).as_markup()

def BOOKS():
    builder = InlineKeyboardBuilder()
    builder.button(
        text= "WIKKIPEDIA📰",
          url= "https://wiki.python.org/moin/PythonBooks"
          )
    return builder.adjust(1).as_markup()

def DOCS():
    builder = InlineKeyboardBuilder()
    builder.button(
        text= "the sphinx documentation tool🟨",
          url= "https://www.sphinx-doc.org/en/master/"
          )
    builder.button(
        text= "Python documentation🟢",
        url= "https://docs.python.org/3/"
        )
    builder.button(
        text= "Download Python 3.13 Documentation🔻",
        url= "https://docs.python.org/3/download.html"
        )
    return builder.adjust(1).as_markup()

def OBTAIN():
    builder = InlineKeyboardBuilder()
    builder.button(
        text= "download python↖️",
          url= "https://www.python.org/downloads/"
          )
    builder.button(
        text= "github🫂",
        url= "https://github.com/python/cpython/"
        )
    builder.button(
        text= " Getting Started section of the Python Developer’s Guide🔻",
        url= "https://devguide.python.org/getting-started/setup-building/index.html"
        )
    return builder.adjust(1).as_markup()


def SCHEMEWORK():
    builder = InlineKeyboardBuilder()
    builder.button(
                    text="Developer’s Guide",
                    url= "https://devguide.python.org/developer-workflow/development-cycle/"
                    )
    builder.button(
                    text="PEP 387 ",
                    url= "https://peps.python.org/pep-0387/"
                    )
    builder.button(
                    text="sys.version",
                    url= "https://docs.python.org/3/library/sys.html#sys.version"
                    )
    builder.button(
                    text="sys.hexversion",
                    url= "https://docs.python.org/3/library/sys.html#sys.hexversion"
                    )
    builder.button(
                    text="sys.version_info",
                    url= "https://docs.python.org/3/library/sys.html#sys.version_info"
                    )

def learning():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Begin lesson📘")
    return builder.adjust(1).as_markup(resize_keyboard= True)

def LS_1():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "1️⃣ Lesson",
                  callback_data="Lesson_1",
                   )
    builder.button(
        text= "📗 Task 📗",url="https://www.schoolsw3.com/python/python_variables_exercises.php"
    )
    builder.button(
        text= "▶Video▶",url="https://www.youtube.com/watch?v=MV-f4Sp571U"
    )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_1")
    return builder.adjust(1).as_markup()

def LS_2():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "2️⃣ Lesson",
                   url= "https://sudoteach.com/content/1/5",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_2")
    return builder.adjust(1).as_markup()

def LS_3():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "3️⃣ Lesson",
                   url= "https://sudoteach.com/content/1/10",
                   )
    builder.button(
                   text= "3.1 Lesson📖",
                   url= "https://sudoteach.com/content/1/14",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_3")
    return builder.adjust(1).as_markup()

def LS_4():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "4️⃣ Lesson",
                   url= "https://sudoteach.com/content/1/68",
                   )
    builder.button(
        text= "4.1 Lesson📒",
          url= "https://sudoteach.com/content/1/70"
          )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_4")
    return builder.adjust(1).as_markup()

def LS_5():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "4.1 The list(massive)",
                   url= "https://sudoteach.com/content/1/72",
                   )
    builder.button(
                   text= "4.2 The Tuple",
                   url= "https://sudoteach.com/content/1/73",
                   )
    builder.button(
                   text= "4.3 The dictionary",
                   url= "https://sudoteach.com/content/1/74",
                   )
    builder.button(
                   text= "4.4 Set(Frozenset)",
                   url= "https://sudoteach.com/content/1/75",
                   )
    builder.button(
                   text= "4.5 All types of data ",
                   url= "https://sudoteach.com/content/1/115",
                   )
    builder.button(
                   text= "Practice.",
                   url= "https://sudoteach.com/content/1/200",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_5")
    return builder.adjust(1).as_markup()

def LS_6():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "6️⃣ Lesson",
                   url= "https://sudoteach.com/content/1/76",
                   )
    builder.button(
                   text= "6.1 Lesson",
                   url= "https://sudoteach.com/content/1/78",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_6")
    return builder.adjust(1).as_markup()

def LS_7():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "7.1 Nested loops",
                   url= "https://sudoteach.com/content/1/116",
                   )
    builder.button(
                   text= "7.2 Processing numbers",
                   url= "https://sudoteach.com/content/1/118",
                   )
    builder.button(
                   text= "7.3 The ternary conditional operator",
                   url= "https://sudoteach.com/content/1/79",
                   )
    builder.button(
                   text= "7.4 Unpacking collections",
                   url= "https://sudoteach.com/content/1/80",
                   )
    builder.button(
                   text= "7.4 The try-except construction",
                   url= "https://sudoteach.com/content/1/119",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_7")
    return builder.adjust(1).as_markup()

def LS_8():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "8.1 Functions and value return",
                   url= "https://sudoteach.com/content/1/81",
                   )
    builder.button(
                   text= "8.2 Function parameters and arguments",
                   url= "https://sudoteach.com/content/1/120",
                   )
    builder.button(
                   text= "8.3 *args and **kwargs",
                   url= "https://sudoteach.com/content/1/121",
                   )
    builder.button(
                   text= "8.4 Lambda functions",
                   url= "https://sudoteach.com/content/1/122",
                   )
    builder.button(
                   text= "8.5 Decorators",
                   url= "https://sudoteach.com/content/1/123",
                   )
    builder.button(
                   text= "8.6 Programming paradigms",
                   url= "https://sudoteach.com/content/1/124",
                   )
    builder.button(
                   text= "8.7 Type annotations",
                   url= "https://sudoteach.com/content/1/125",
                   )
    builder.button(
                   text= "8.8 Sorting collections",
                   url= "https://sudoteach.com/content/1/126",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_8")
    return builder.adjust(1).as_markup()

def LS_9():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "9.1 The random module",
                   url= "https://sudoteach.com/content/1/127",
                   )
    builder.button(
                   text= "9.2 decimal, fractions, complex",
                   url= "https://sudoteach.com/content/1/128",
                   )
    builder.button(
                   text= "9.3 The turtle module",
                   url= "https://sudoteach.com/content/1/129",
                   )
    builder.button(text= "Quiz☔️", callback_data= "Quiz_9")
    return builder.adjust(1).as_markup()

def LS_10():
    builder = InlineKeyboardBuilder()
    builder.button(
                   text= "Repeat",
                   callback_data="repeat",
                   )
    return builder.adjust(1).as_markup()

def answer():
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text= "1")
    keyboard.button(text= "2")
    keyboard.button(text= "3")
    keyboard.button(text= "4")
    return keyboard.adjust(2).as_markup(resize_keyboard= True)

def Projects():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text= "The Gallows Game", callback_data="Gallow")
    keyboard.button(text= "Calculator", callback_data="Calculator")
    keyboard.button(text= "An application for making a to-do list", callback_data="to-do")
    keyboard.button(
            text= "An application for converting units of measurement",
            callback_data="converting"
        )
    keyboard.button(text= "A program for checking palindromes", callback_data="palindromes")
    return keyboard.adjust(1).as_markup()

def Done_1():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_1")
    return keyboard.adjust(1).as_markup()

def Done_2():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_2")
    return keyboard.adjust(1).as_markup()

def Done_3():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_3")
    return keyboard.adjust(1).as_markup()

def Done_4():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_4")
    return keyboard.adjust(1).as_markup()

def Done_5():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_5")
    return keyboard.adjust(1).as_markup()

def Done_6():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_6")
    return keyboard.adjust(1).as_markup()

def Done_7():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_7")
    return keyboard.adjust(1).as_markup()

def Done_8():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_8")
    return keyboard.adjust(1).as_markup()

def Done_9():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Done✔️", callback_data="done_9")
    return keyboard.adjust(1).as_markup()

def passed():
    builder = ReplyKeyboardBuilder()
    builder.button(text= "I passed")
    return builder.adjust(1).as_markup(resize_keyboard=True)

def Video_clip_materials():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(
                    text="10 TIPS FOR A NOVICE DEVELOPER📹",
                    url="https://www.youtube.com/watch?v=tv_sdmAn1uU"
                    )
    keyboard.button(
                    text="Your own VPN in 7 minutes",
                    url="https://www.youtube.com/watch?v=tv_sdmAn1uU"
                    )
    keyboard.button(
                    text="INSTALLING PYTHON AND PYCHARM",
                    url="https://www.youtube.com/watch?v=s96LZWg5lug"
                    )
    keyboard.button(
                    text="Sudoteach",
                    url="https://sudoteach.com/"
    )
    keyboard.button(
                    text="TeacherArmy",
                    url="https://teacher.army/intensive?utm_source=yandex&utm_medium=cpc&utm_campaign=113340752&utm_content=16384786469&utm_term=python%20обучение&yclid=10382288279868538879"
                    )
    return keyboard.adjust(1).as_markup()

def get_or_continue():
    builder = ReplyKeyboardBuilder()
    builder.button(
                    text="CONTINUE👉",
                    )  
    builder.button(
                    text="GET💎",
                    )  
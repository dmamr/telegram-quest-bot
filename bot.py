from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# замените на ваш токен от BotFather
TOKEN = '7238885317:AAFfJ3HwxxVCAGrH4hqUVtbjdTZXi1pjho0'

# словарь для хранения этапов прохождения квеста каждым пользователем
user_stage = {}

# правильный ответ для первого квеста
correct_answer_1 = ['джонс', 'нурмагомедов', 'махачев', 'кадыров']
correct_answer_2 = ['абай', 'абай кунанбаев', 'абай құнанбаев', 'құнанбаев', 'кунанбаев']
correct_answer_3 = ['любимый']
correct_answer_4 = ['120000']
correct_answer_5 = ['13']
correct_answer_6 = ['11']
correct_answer_7 = ['томас', 'томас шелби', 'шелби томас']
correct_answer_8 = ['сапар', 'sapar', 'дархан джузз - сапар', 'дархан джуз - сапар']


# стартовое приветствие
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_stage[user_id] = 1
    await update.message.reply_text(
        "я пошутив, пиши /quest, и тогда точно всё начнётся ыыы"
    )

# запуск первого квеста
async def quest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_stage[user_id] = 2
    await update.message.reply_text(
        "квест 1\n\n"
        "начнем с того, в чем ты один из лучших.. "
        "октагон, стратегия, сила — это твоё!\n\n"
        "вопрос: кого ты бы назвал величайшим бойцом в истории ufc?\n\n"
        "напиши только фамилию."
    )

# обработка ответа
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    text = update.message.text.strip().lower()
    stage = user_stage.get(user_id, 0)

    # проверка квеста 1
    if stage == 2:
        if text in correct_answer_1:
            user_stage[user_id] = 3
            await update.message.reply_text(
                "верно. ты знаешь свое дело!! <3\n"
                "держи — *лы*.\n"
                "запоминай, это тебе пригодится.\n\n"
                "готов ко второму квесту? пиши /next"
            )
        else:
            await update.message.reply_text(
                "не совсем...\n"
                "давай попробуем еще раз?\n"
                "вспомни: это имя гремит по всему миру! "
                "и ты сам когда-то мне о нем рассказывал."
            )
    # проверка квеста 2
    elif stage == 4:
        if text in correct_answer_2:
            user_stage[user_id] = 5
            await update.message.reply_text(
                "дәл таптың ❤️\n\n"
                "*е*\n"
                "жазып ал. алда тағы бар.\n\n"
                "кезекті квестке көшу үшін /next деп жаз"
            )
        else:
            await update.message.reply_text(
                "давай думай тағы. сен оны білесің.\n"
                "сөздері жүрекке сөйлейді."
            )

    # проверка квеста 3
    elif stage == 6:
        if text in correct_answer_3:
            user_stage[user_id] = 7
            await update.message.reply_text(
                "этот пост — про тебя и меня вместе. Глянь на фотки, какая я довольная?\n\n"
                "запоминай — *ны*\n"
                "и пиши /next, чтобы идти дальше."
            )
        else:
            await update.message.reply_text(
                "а ну смотри внимательнее!\n"
                "одно слово, очень важное."
            )

    # проверка квеста 4
    elif stage == 8:
        if text in correct_answer_4:
            user_stage[user_id] = 9
            await update.message.reply_text(
                "так точно ыхвхывхвых\n"
                "ну ладно, как-то слишком просто, да? Усложняем задание!\n\n"
                "а, чуть не забыла — *тал*\n"
                "запомнил? теперь пиши /next, чтобы идти дальше."
            )
        else:
            await update.message.reply_text(
                "мне кажется, ты не ту цифру посмотрел ыхвзхафзхыв\n"
                "введи точную цену в тенге, как на сайте!!!"
            )

    # проверка квеста 5
    elif stage == 10:
        if text in correct_answer_5:
            user_stage[user_id] = 11
            await update.message.reply_text(
                "инженерім ывхзфахзфыхз\n"
                "всё по делу, всё точно! вот и тебе по делу две буковки — *пе*\n\n"
                "вперёд? тогда пиши /next"
            )
        else:
            await update.message.reply_text(
                "не совсем. вспомни таблицу менделеева..."
            )

    # проверка квеста 6
    elif stage == 12:
        if text in correct_answer_6:
            user_stage[user_id] = 13
            await update.message.reply_text(
                "ну проста король логарифмов\n"
                "проста самая вышка. еще две буковки — *ме*\n\n"
                "мы почти у финала! Продолжаем? пиши /next"
            )
        else:
            await update.message.reply_text(
                "что-то не сходится... мико аға, проверьте правило логарифмов и попробуйте снова!"
            )

    # проверка квеста 7
    elif stage == 14:
        if text in correct_answer_7:
            user_stage[user_id] = 15
            await update.message.reply_text(
                "в точку! вот он сильный и молчаливый и о семьи благополучии переживает  \n"
                "как ты хыхыххы\n\n"
                "запоминаем *ре*, пишем /next, и двинемся к последнему квестику."
            )
        else:
            await update.message.reply_text(
                "вспомни, кто мог сказать это.  \n"
                "ты точно знаешь его."
            )
    # проверка квеста 8
    elif stage == 16:
        if text in correct_answer_8:
            user_stage[user_id] = 17
            await update.message.reply_text(
                "хихихихи\n"
                "она! ты ей открыл мне мир казахских песен, знаешь же, да?\n\n"
                "последний ключ — *ход*\n"
                "теперь у тебя есть все части к ответу... но что это были за буковки рандомные?\n\n"
                "пиши /final, чтобы приступить к последней разгадке!"
            )
        else:
            await update.message.reply_text(
                "почти. вспомни, это была первая песня, которую ты мне включил от него."
            )

    # проверка финальной фразы
    elif stage == 18:
        if text.replace(" ", "").lower() in ['переходныеметаллы']:
            user_stage[user_id] = 19
            await update.message.reply_text(
                "точно! ты собрал всё правильно 🧩\n\n"
                "фух, наконец последний шаг?\n"
                "помнишь где находятся переходные металлы в таблице Менделеева? загаданное слово - как раз таки один из этих металлов!\n\n"
                "напиши его название. хинт - ты и есть ключ к разгадке!"
            )
        else:
            await update.message.reply_text(
                "что-то не сходится. попробуй переставить слоги и составить 2 слова."
            )

    # финальный ответ
    elif stage == 19:
        if text.lower() in ['борий', 'bohrium']:
            user_stage[user_id] = 20
            await update.message.reply_text(
                "да!! это *борий*, элемент №107 🧪\n\n"
                "ты сам, как элемент: редкий, сильный, и незаменимый.\n\n"
                "ну тут уже я передаю слово человеческой госпоже Мамратовой!\n"
                "еще раз с днём защитника отечества, мой герой ❤️"
            )
        else:
            await update.message.reply_text(
                "почти. подумай о своем дне рождения!"
            )


    else:
        await update.message.reply_text("напиши /quest чтобы начать задание")

# запуск следующих квестов по очереди
async def next_step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    stage = user_stage.get(user_id, 0)

    if stage == 3:
        # квест 2
        user_stage[user_id] = 4
        await update.message.reply_text(
            "квест 2!\n\n"
            "сенің қазақ мәдениетімен қатынасы әрқашан бағалайтынмын -\n"
            "жай ғана біле алмайсың — сезіну керектігін білесің!\n"
            "осы тереңдігің — сенің күшің.\n\n"
            "бір ақыны:\n"
            "«Алланың өзі де рас, сөзі де рас,\n"
            "Рас сөз ешуақытта жалған болмас.» — деп жазды.\n\n"
            "оның аты кім болды? (толька за ашипки не бей...)\n"
        )

    elif stage == 5:
        # квест 3
        user_stage[user_id] = 6
        await update.message.reply_text(
            "квест 3!\n\n"
            "иногда важные вещи спрятаны на виду.  \n"
            "иногда — в сторис.  \n"
            "а иногда — в моих комментариях к тебе.\n\n"
            "я часто говорю тебе, что ты для меня не просто человек.  \n"
            "найди пост в инстаграме, в котором фотографии были сделаны тобой. как я назвала тебя в этом посте?\n\n"
            "напиши только одно слово."
        )

    elif stage == 7:
        # квест 4
        user_stage[user_id] = 8
        await update.message.reply_text(
            "квест 4.\n\n"
            "в тебе есть особый стиль.  \n"
            "не показной, а уверенный.  \n"
            "ты не следуешь трендам — ты задаёшь ритм.  \n"
            "и я всегда это замечаю.\n\n"
            "вопрос:  \n"
            "зайди на сайт massimo dutti.  \n"
            "найди, сколько стоит самое дорогое поло на момент сейчас.\n\n"
            "введи цену в тенге!"
        )

    elif stage == 9:
        # квест 5
        user_stage[user_id] = 10
        await update.message.reply_text(
            "квест 5 –\n\n"
            "ты всегда восхищал меня тем, как разбираешься в сложных вещах.  \n"
            "то, что пугает других, тебе даёт азарт. ты — как инженер для жизни!\n\n"
            "так вот, вопрос для инженера:  \n"
            "какой металл чаще всего используется в авиастроении из-за своей лёгкости и прочности?\n"
            "проверОчка! (дада я шутница)\n\n"
            "введи атомный номер этого элемента."
        )

    elif stage == 11:
        # квест 6
        user_stage[user_id] = 12
        await update.message.reply_text(
            "квест 6.\n\n"
            "иногда я думаю — у тебя в голове графики, формулы и бесконечные переменные. конечно, порой ты сам себе жизнь усложняешь, но ты будто создан, чтобы решать то, что не всем по зубам.\n"
            "точный и мощный.  \n"
            "я знаю, ты это решишь быстрее, чем успеешь прочитать.. да?\n\n"
            "log₂(2⁵) + log₃(√81) + log₁₀(10⁴) = ?\n\n"
        )

    elif stage == 13:
        # квест 7
        user_stage[user_id] = 14
        await update.message.reply_text(
            "квест 7:\n\n"
            "ты мой герой.  \n"
            "и в каждом сериале есть свой!\n\n"
            "давай вспомним один очень хороший сериал,  \n"
            "название которого я, конечно, говорить не буду ывхыхвхывхыв\n\n"
            "вопрос:  \n"
            "кто сказал:\n"
            "“you can change what you do, but you can’t change what you want.”\n\n"
            "напиши имя героя."
        )

    elif stage == 15:
        # квест 8
        user_stage[user_id] = 16
        await update.message.reply_text(
            "квест 8.\n\n"
            "ты хорошо помнишь детали.  \n"
            "и особенно — те, что связаны с нами.\n\n"
            "а помнишь, какой песней ты меня познакомил с Дарханом Джузз?\n\n"
            "напиши её название."
        )

    else:
        await update.message.reply_text("так, все по порядку! отвечаем на вопросикиии")

# финальный шаг
async def final_step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    stage = user_stage.get(user_id, 0)

    if stage == 17:
        user_stage[user_id] = 18
        await update.message.reply_text(
            "финал! ура-ура!\n\n"
            "так вот, эти буковки были на самом деле слогами одного словосочетания. у тебя есть 8 слогов:\n"
            "*лы, ме, ны, ход, пе, е, ре, тал* (я говорила запомнить, но так как сегодня твой праздник, я облегчу тебе задачу)\n\n"
            "теперь собери из них фразу.\n"
            "впиши её полностью (2 слова).\n"
            "если всё верно — получишь последнюю (честно!) подсказку."
        )
    elif stage > 17:
        await update.message.reply_text("ты уже прошёл эту часть — просто введи собранную фразу!")
    else:
        await update.message.reply_text("сначала пройди все квесты и собери подсказки, читер")

# запуск приложения
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quest", quest))
    app.add_handler(CommandHandler("next", next_step))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CommandHandler("final", final_step))

    print("бот запущен...")
    app.run_polling()

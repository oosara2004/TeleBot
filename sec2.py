import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start'])
def handle_start_help(message):
    start_message = "اهلا أنا بوت يعطي نبذة عن مجال الذكاء الاصطناعي الرجاء الاختيار من الآتي\n/sdaia لتعرف على سدايا\n/definition نبذة عن الذكاء الاصطناعي\n/jobs المسميات الوظيفية\n/different الفرق بين التعلم الآلي والعميق\n/AI فيديو توضيحي\n/Applications تطبيقات الذكاء الاصطناعي"
    bot.send_message(message.chat.id, start_message)

@bot.message_handler(commands=['sdaia'])
def handle_sdaya(message):
    linksdaya = "https://sdaia.gov.sa/ar/default.aspx"
    bot.send_message(message.chat.id, f"تعتبر سدايا اهم المراكز الوطنية لذكاء الاصطناعي, هذا الموقع الرسمي : \n{linksdaya}")

@bot.message_handler(commands=['definition'])
def handle_definition(message):
    x = "هو علم شامل للتطبيقات التي تؤدي مهام مُعقدة كانت تتطلب في الماضي إدخالات بشرية"
    bot.send_message(message.chat.id, x)

@bot.message_handler(commands=['jobs'])
def handle_jobs(message):
    jobs = "مهندس التعلم الآلي\nمهندس عالم بيانات\nمهندس خوارزميات\nمحلل بيانات\nعالم إحصاء\nمهندس أبحاث\nأخصائي ذكاء اصطناعي\nمطور ذكاء أعمال"
    bot.send_message(message.chat.id, jobs)

@bot.message_handler(commands=['different'])
def handle_different(message):
    y = "التعلم الآلي يعنى بكيفية تدريب وتقييم النماذج و اخذ القرارات الصحيحة والتوقع المنطقي"
    z = "يركز على الشبكات العصبية الاصطناعية وكيفية ربطها لآلة لتمييز الصور والأصوات وغيرها"
    bot.send_message(message.chat.id, y + "\n" + z)

@bot.message_handler(commands=['AI'])
def handle_AI(message):
    AI = "https://www.youtube.com/watch?v=ad79nYk2keg"
    bot.send_message(message.chat.id, f"نبذة أوسع عن مجال الذكاء الاصطناعي\n{AI}")

@bot.message_handler(commands=['Applications'])
def handle_applications(message):
    U = "يستخدم في العديد من القطاعات اهمها الصحة والعسكري و من بعض التطبيقات"
    chatgpt = "https://chat.openai.com/"
    deepdream = "https://deepdreamgenerator.com/"
    dungo = "https://www.aidungeon.io/"
    c = "https://www.clarifai.com/"
    bot.send_message(message.chat.id, U + "\n" + chatgpt + "\n" + deepdream + "\n" + dungo + "\n" + c)


@bot.message_handler(func=lambda message: True)
def handle_other_message(message):
    bot.send_message(message.chat.id, 'لرؤية الاوامر اكتب او اضغط على /start')

bot.polling()
from telegram.ext import Updater, CommandHandler, \
    CallbackContext, MessageHandler, Filters
from telegram import Update

questions = [{
    "q": "Из какой страны родом Джастин Бибер",
    "a": "Канада",
    "d": 2,
}, {
    "q": "Что являеться национальным животным Шотландии",
    "a": "Единорог",
    "d": 3,
}, {
    "q": "Какая страна производит больше всего кофе в мире",
    "a": "Бразилия",
    "d": 4,
},{
    "q": "Какой безалкогольный напиток первым был взят в космос",
    "a": "Кока-Кола",
    "d": 3,
},{
    "q": "Какая игрушка была первой которую рекламировали по телевидению",
    "a": "Мистер Картофельная Голова",
    "d": 4,
},{
    "q": "В какой стране находится Прага",
    "a": "Чехия",
    "d": 5,


}]


def set_question(questions, i):
    return f"Вопрос №{i + 1}: {questions[i]['q']}\n" \
           f"Сложность: {questions[i]['d']}/5"


def start(update=Update, context=CallbackContext):
    context.user_data['i'] = 0
    context.user_data['s'] = 0
    context.user_data['k'] = 1
    update.message.reply_text("Здравствуйте, Роман Романович!\n"
                              "Чекай викторинку!")
    update.message.reply_text(set_question(questions, context.user_data['i']))


def echo(update=Update, context=CallbackContext):
    if context.user_data.get("k") == 1:
        if update.message.text.lower() == questions[context.user_data['i']]['a'].lower():
            context.user_data['s'] += questions[context.user_data['i']]['d']
            update.message.reply_text('Правильно!')
        else:
            update.message.reply_text(f'Неправильно!\n'
                                      f'Правильный ответ: '
                                      f'{questions[context.user_data["i"]]["a"]}')
        context.user_data['i'] += 1
        if context.user_data['i'] == len(questions):
            context.user_data['k'] = 0
            update.message.reply_text(f"Лучший!\n"
                                      f"Ты набрал {context.user_data['s']} баллов")
        else:
            update.message.reply_text(set_question(questions, context.user_data['i']))

    else:
        update.message.reply_text("Введите старт!")



def main():
    updater = Updater("5855635613:AAGXUEztf-AmjzlJtVehG80FiFXnLKClLyk")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.
                                          text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


main()

import telebot
import markups as m

TOKEN = '689386115:AAFVkgOWcCKrbo0l8pbac3HcX-7rscNVAVc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_welcome(message):

        bot.send_message(message.chat.id,'Привет,\nЯ - Бот от МастерПиццы, где самая вкуснейшая пицца в Алматы.')
        chat_id = message.chat.id
        text = message.text
        msg = bot.send_message(chat_id, 'Как к Вам можно обратиться?')
        bot.register_next_step_handler(msg, askName)

def askName(message):
    chat_id = message.chat.id
    text = message.text
    msg = bot.send_message(chat_id,'Спасибо 😉,\n'+ text+', я хочу Вам показать какое у нас меню:', reply_markup=m.markup_menu)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'привет':
        bot.send_message(chat_id, 'Привет 😁,\nЯ помогу Вам совершить заказ или дать информацию которая Вас интересует 🤔')
    elif text == 'как дела?':
        bot.send_message(chat_id, 'У меня отлично 🤗,\nЯ рад с Вами поговорить и помочь Вам')
    elif text == 'сеты':
        bot.send_message(chat_id,'Проверка')
    else:
        bot.send_message(chat_id, 'Простите, я Вас не понял 😥')


bot.polling(none_stop=True)
import telebot
from telebot import types
from bot_functions import coin_toss, print_console_log,  make_a_joke

# Инициализация бота
bot = telebot.TeleBot('1870191909:AAEwEdf1oMqdoi3OjqUTmS1Z2he0EbIHa-s')

# message.handler - принятие сообщений. Если пользователь отправил команду старт:
@bot.message_handler(commands=['start'])
def handle_start(message):
    print_console_log(message)  # вывод логов сообщения в консоль, из которой запущен бот
    # отправка сообщения пользователю
    bot.send_message(message.from_user.id, 'Привет! \
                                            Я ботит-шпротик. Поиграем? \
                                            Введи /help или /menu, чтобы узнать обо мне побольше.')


# Если пользователь отправил команду menu, help
@bot.message_handler(commands=['menu', 'help'])
def handle_menu_help(message):
    # запись логов
    print_console_log(message)

    # Если пользователь ввёл help - дополнительно вывести
    if message.text == '/help':
        # вот это вот сообщение
        bot.send_message(message.from_user.id, """
Для помощи напиши свою проблему на @mileymileymil(в личные сообщения) 
""")

    # Инициализация клавиатуры. Говорим, что будет клавиатура
    keyboard = types.InlineKeyboardMarkup()
    # Инициализация кнопки в меню (на клаве) с её идентификатором
    # text - надпись на кнопке
    # callback_data - что-то типа id кнопки. Данные, которые кнопка мониторит
    key_coin = types.InlineKeyboardButton(text='Бросок монетки', callback_data='coin')
    key_joke = types.InlineKeyboardButton(text='Рассказать шутку?)', callback_data='joke')
    # Добавление кнопки на клавиатуру
    keyboard.add(key_coin)
    keyboard.add(key_joke)
    # Отправка сообщения с reply_markup, предложенной клавиатурой
    bot.send_message(message.from_user.id, 'Меню: ', reply_markup=keyboard)


# Мониторинг введёных кнопок. Берёт данные из кнопки и выполняет соотвествующую ветку цикла
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'coin':
        bot.send_message(call.message.chat.id, coin_toss())
    elif call.data == 'joke':
        bot.send_message(call.message.chat.id, make_a_joke())
    elif call.data == '':
        # TODO
        pass


# # Выборка всех остальных команд типа 'text'
@bot.message_handler(func=lambda message: True)


# Функция для отправки эхо-сообщений
def echo_message(message):
    print_console_log(message)
    bot.reply_to(message, message.text)
    bot.send_message(message.from_user.id, 'Введи /help или /menu, чтобы узнать обо мне побольше')


# Зацикливание бота. none_stop=True - работает без передышки.
bot.polling(none_stop=True)

import random


def coin_toss():
    """
    Функция, реализующая бросок монетки.
    :return: результат броска.
    """
    return random.choice(['Орёл!', 'Решка!'])

def make_a_joke():
    """
    Функция, выдающая шутку.
    :return:  шутка.
    """
    return random.choice(['мой папа молодец , он прошел две войны .Потом устал,выключил компьютер и лег спать',
                        'What did the ocean say to the beach?" "Nothing, it just waved','А вам не кажется несправедливым, что только одна компания выпускает игру "Монополия"?',
                          'Singing in the shower is fun until you get soap in your mouth. Then it is a soap opera.','Where do fruits go on vacation?" "Pear-is!'])

def print_console_log(message):
    """
    Функция вывода логов сообщения в консоль.
    :param message: сообщение, присланное пользователем.
    """
    print('Chat ID: ', message.chat.id)
    print('Username: ', message.chat.username)
    print('First name: ', message.chat.first_name)
    print('Last name: ', message.chat.last_name)
    print('Text: ', message.text)
    print('-' * 30)

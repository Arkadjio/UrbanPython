# Функция с 2-мя обычными и 1 именованным аргументами
def send_email(message, recipient, sender='university.help@gmail.com'):
    # данные для проверки на их наличие
    symb_dog = '@'
    ending_eml = '.com' or '.ru' or '.net'

    # проверка на совпадение аргументов функции
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')

    # Проверка recipient и sender на обязательные аргументы
    elif (recipient.find(symb_dog) == -1 or recipient.lower().find(ending_eml) == -1) and (
            sender.find(symb_dog) == -1 or sender.lower().find(ending_eml) == -1):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    # если все успешно и ни один оператор не сыграл
    else:
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Проверка связи', 'arkadjio@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

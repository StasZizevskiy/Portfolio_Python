'''
Шифр цезаря - шифр сдвига, в котором шифрование и дешифровка букв производятся
путем сложения и вычитания соответствующих чисел. Принимает от пользователя
ключ шифрования и текстовое сообщение, которое необходимо закодировать.
'''

import pyperclip

#playing = True
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_sumbols = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

#Спрашиваем у пользователя хочет он шифровать или расшифровывать
while True:
    global playing
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
    elif response.startswith('d'):
        mode = 'decrypt'
    else:
        print('Please, enter "e" or "d"')

    maxKey = len(symbols) - 1
    print('Please, enter the key (0 to {}) to use'.format(maxKey)) #Просим пользователя ввести ключ шифрования
    response = input('> ').upper()
    if not response.isdecimal():
        print('Неправильный ввод. Введите значение от 0 до {}'.format(maxKey))
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)

    print('Enter the message to {}'.format(mode)) #Просим пользователя ввести сообщение для шифрования/дешифровки
    message = input('> ')
    message = message.upper()  # программа примет сообщения только в верхнем регистре

    translated = ''  # для хранения зашифрованного/расшифрованного сообщения

    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)  # получаем числовое значение символа в списке symbols
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            if num >= len(symbols):  # Производим переход по кругу символов, если символ равняется последнему или больше
                num = num - len(symbols)
            elif num < 0:
                num = num + len(symbols)
            translated = translated + symbols[num]
        else:  # если символа нет в symbols переносим его в конечное сообщение без изменения
            translated = translated + symbol

    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full {}ed text copied to clipboard.'.format(mode))
    except:
        pass  # Если библиотека pyperclip не установлена ничего не делаем

    new_try = input('Хотите ещё раз? Нажмите "y"(es) или "n"(o)')
    if new_try[0].lower() == 'y':
        playing = True
    else:
        print('Всего хорошего!')
        break







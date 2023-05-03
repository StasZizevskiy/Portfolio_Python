'''
Шифр цезаря - шифр сдвига, в котором шифрование и дешифровка букв производятся
путем сложения и вычитания соответствующих чисел. Принимает от пользователя
ключ шифрования и текстовое сообщение, которое необходимо закодировать.
'''

import pyperclip

#playing = True
symbols = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

#Спрашиваем у пользователя хочет он шифровать или расшифровывать
while True:
    global playing
    print('Хотите зашифровать ("з") или расшифровать "р"')
    response = input('> ').lower()
    if response.startswith('з'):
        mode = 'для шифрования'
    elif response.startswith('р'):
        mode = 'для расшифровки'
    else:
        print('Введите "з" или "р"')

    maxKey = len(symbols) - 1
    print('Пожалуйста, введите ключ (от 0 до {}) для шифровки текста'.format(maxKey)) #Просим пользователя ввести ключ шифрования
    response = input('> ').upper()
    if not response.isdecimal():
        print('Неправильный ввод. Введите значение от 0 до {}'.format(maxKey))
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)

    print('Введите сообщение {}'.format(mode)) #Просим пользователя ввести сообщение для шифрования/дешифровки
    message = input('> ')
    message = message.upper()  # программа примет сообщения только в верхнем регистре

    translated = ''  # для хранения зашифрованного/расшифрованного сообщения

    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)  # получаем числовое значение символа в списке symbols
            if mode == 'для шифрования':
                num = num + key
            elif mode == 'для расшифровки':
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
        print('Текст {} скопирован в буфер обмена для дальнейшего использования.'.format(mode))
    except:
        pass  # Если библиотека pyperclip не установлена ничего не делаем

    print('Хотите ещё раз? Нажмите "да" или "нет"')
    new_try = input('> ')
    if new_try[0].lower() == 'д':
        playing = True
    else:
        print('Всего хорошего!')
        break







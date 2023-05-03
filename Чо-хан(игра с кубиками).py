'''
Чо-хан традиционная игра в феодальной Японии. Два шистигранных кубика выбрасываются из
чашки, игроки должны угадать будет сумма четной ("Чо") или нечетной ("Хан").
'''

import random, sys

japan_numbers = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                 4: 'SHI', 5: 'GO', 6: 'ROKU'}
playing = True
purse = 5000

while True:
    while True:
        print('У Вас {} монет. Сколько готовы поставить?'.format(purse))
        bet = input('> ')
        if not bet.isdecimal():
            print('Введите, пожалуйста, число')
        elif int(bet) > purse:
            print('Ваша ставка больше Вашего кошелька. У Вас есть {} монет'.format(purse))
        else:
            print('Спасибо за ставку {}'.format(bet))
            break
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('Дилер крутит чашку и вы слышите стук игральных костей')
    print('Дилер ударил чашку об стол, пока её не поднимал. На что ставите? Введите Cho (четное) или Han (нечетное)')
    while True:
        pot = input('> ').upper()
        if pot != 'CHO' and pot != 'HAN':
            print('Пожалуйста введите либо Cho либо Han')
            continue
        else:
            break
    print('Дилер поднимает чашку') #открываем результаты броска
    print('{}, {}'.format(japan_numbers[dice1], japan_numbers[dice2]))
    print(dice1, dice2)

    rollsIsEven = (dice1+dice2)%2==0
    if rollsIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = pot == correctBet

    if playerWon:
        print('Выигрыш! Красавчик! Ты забираешь {}'.format(bet))
        purse += int(bet) #прибавляем приз к кошельку
    else:
        purse -= int(bet)
        print('Ты не угадал. Сорян')
    if purse == 0:
        print('У тебя закончились деньги, амиго. Возвращайся ещё. Спасибо за игру!')
        sys.exit()
    else:
        new_game = input('Попробуем ещё? y или n')
        if new_game[0].lower() == 'y':
            playing = True
        else:
            print('Спасибо за игру, брат, в следующий раз повезёт больше')
            sys.exit()


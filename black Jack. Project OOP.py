import random

suits = ("Черви", "Трефы", "Вини", "Бубны")
ranks = ("Двойка", "Тройка", "Четверка", "Пятерка", "Шестёрка", "Семёрка", "Восьмерка", "Девятка", "Десятка", "Валет", "Дама", "Король", "Туз")
values = {"Двойка":2, "Тройка":3, "Четверка":4, "Пятерка":5, "Шестёрка":6, "Семёрка":7, "Восьмерка":8, "Девятка":9, "Десятка":10, "Валет":10, "Дама":10, "Король":10, "Туз":11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__ (self):
        return self.rank + ' ' + self.suit
    
class Deck:
    def __init__(self):
        self.deck = [] #начинаем с пустой колоды
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'В Колоде находятся карты: ' + deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []  #начинаем с пустой руки
        self.value = 0 # и нулевого значения очков
        self.aces = 0 # для добавления значений тузов
    
    def add_card(self, card):
        # card - это объект взятый из объекта Deck, поэтому это Card из объекта Deck.deal() -> Card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]
        
        # тузы
        if card.rank == 'Туз':
            self.aces += 1
            
    def adjust_for_ace(self):
        
        # если сумма больше 21 и есть тузы, считаем туз как 1, вместо 11
        while self.value>21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total = 500): # значение по умолчанию 500
        self.total = total
        self.bet = 0

    def balance(self):
        return self.total

    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        print('Банк {}'.format(self.total))
        
def take_bet(chips):
    while True:    
        try:
            if chips.bet < 0:
                print('Ставка не может меньше нуля, Амиго. Попробуй, ещё раз')
            else:
                print('Твоя ставка?')
                chips.bet = int(input('> '))
        except:
            print('Извините, введите, пожалуйста, число')
        else:
            if chips.bet > chips.total:
                print('У тебя не хватает денег, Амиго. Твой Банк {}'.format(chips.total))
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    print(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    
    while True:
        print('Возьмёшь ещё карту (hit) или тебе хватит (stand)? Введите h или s?')
        x = input('> ')
        
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Игрок остаётся при текущих картах. Ход дилера')
            playing = False
        else:
            print('Извини, я не понял. Введите h или s')
            continue
        break

def player_busts(player,deck, hand):
    print('Перебор! Превышение суммы 21 для игрока!')
    chips.lose_bet()
    
def player_wins(player,deck, hand):
    print('Победа, брат! Поздравляю')
    chips.win_bet()
    
def dealer_busts(player,deck, hand):
    print('Ты победил, брат! Дилер перебрал за 21')
    chips.win_bet()

def dealer_wins(player,deck, hand):
    print('Ахтунг, Амиго! У дилера больше. Следующий раз повезёт')
    chips.lose_bet()
    
def push(player, dealer):
    print('Ничья! Делим пополам')

def show_some(player, dealer):
    print("Твои карты:", *player.cards)
    print("Карты дилера:", *dealer.cards)

player_chips = Chips() # выдаем фишки игроку (по умолчанию 500)

while True:


    # пишем приветственное сообщение
    print('Добро пожаловать, Амиго. Твой баланс {}'.format(player_chips.balance()))

    take_bet(player_chips) # спрашиваем ставку

    deck = Deck() # Создать и перемешать колоду карт.
    deck.shuffle()
    
    player_hand = Hand() #Игрок получает карты
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand() #дилер получает карты
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #показываем карты
    show_some(player_hand, dealer_hand)
    print(player_hand.value)
    print(dealer_hand.value)

    while playing:  # переменная из функции hit or stand
        
        hit_or_stand(deck, player_hand) #предлагаем игроку взять ещё одну карту или оставить как есть
        
        show_some(player_hand, dealer_hand) #показываем карты
        print(player_hand.value)
        print(dealer_hand.value)

        # Если карт у игрока больше 21 запускаем player_busts и закрываем цикл break
        if player_hand.value>21:
            print('Перебор брат! Сорян')
            player_chips.lose_bet()
            break
        
        # если не превысили 21, то переходим к картам дилера. берём карты до суммы >=17.
    while dealer_hand.value<17:
            hit(deck, dealer_hand)
            
        # выполняем различные варианты игры
    if dealer_hand.value > 21:
        print('Превышение суммы 21 для дилера! Игрок выиграл')
        player_chips.win_bet()
    elif dealer_hand.value<player_hand.value:
        print('Игрок выиграл!')
        player_chips.win_bet()
    elif dealer_hand.value>player_hand.value:
        print('Дилер выиграл!')
        player_chips.lose_bet()
    else:
        print('Ничья!')

        # показываем количество фишек игрока

    print('Player chips: {}'.format(player_chips.total))
        
        #спрашиваем хочет ли игрок сыграть снова
        
    print('Ещё партию, брат? y или n?')
    new_game = input('> ')
    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Спасибо за игру, Амиго!')
        break


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
    def __init__(self, total = 100): # значение по умолчанию 100
        self.total = total
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet 
        
def take_bet(chips):
    while True:    
        try:
            chips.bet = int(input('Сколько вы хотите поставить?'))
        except:
            print('Извините, введите, пожалуйста, число')
        else:
            if chips.bet > chips.total:
                print('Сумма больше Вашего банка. Банк составляет {}'.format(chips.total))
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
        x = input('Взять дополнительную карту (hit) или оставить как есть (stand)? Введите h или s')
        
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Игрок остаётся при текущих картах. Ход дилера')
            playing = False
        else:
            print('Извините, ответ не ясен. Введите h или s')
            continue
        break

def player_busts(player,deck, hand):
    print('Превышение суммы 21 для игрока!')
    chips.lose_bet()
    
def player_wins(player,deck, hand):
    print('Игрок выиграл!')
    chips.win_bet()
    
def dealer_busts(player,deck, hand):
    print('Игрок выиграл! Дилер превысил сумму 21')
    chips.win_bet()

def dealer_wins(player,deck, hand):
    print('Дилер выиграл!')
    chips.lose_bet()
    
def push(player, dealer):
    print('Ничья!')

def show_some(player, dealer):
    print("Player cards:", *player.cards)
    print("Dealer cards:", *dealer.cards)

while True:
    # пишем приветственное сообщение
    print('Добро пожаловать в игру')
    
    
    deck = Deck() # Создать и перемешать колоду карт. 
    deck.shuffle()
    
    player_hand = Hand() #Выдать каждому игроку по две карты
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    print(player_hand.value)
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    print(dealer_hand.value)
    
    #выдаем фишки игроку (по умолчанию 100)
    player_chips = Chips(500)
    
    #спрашиваем ставку
    
    take_bet(player_chips)
    
    #показываем карты 
    
    show_some(player_hand, dealer_hand)
    
    
    while playing:  # переменная из функции hit or stand
        
        hit_or_stand(deck, player_hand) #предлагаем игроку взять ещё одну карту или оставить как есть
        
        show_some(player_hand, dealer_hand) #показываем карты, но оставляем одну из карт дилеа скрытой
        
        # Если карт у игрока больше 21 запускаем player_busts и закрываем цикл break
        if player_hand.value>21:
            print('Превышение суммы 21 для игрока!')
            player_chips.lose_bet()
            break
        
        # если не превысили 21, то переходим к картам дилера. берём карты до суммы >=17.
        
    while dealer_hand.value<17:
            hit(deck, dealer_hand)
            
        # выполняем различные варианты игры
    if player_hand.value>21:
        print('Превышение суммы 21 для игрока!')
        player_chips.lose_bet()
    elif dealer_hand.value > 21:
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
        
    new_game = input('Хотите начать новую игру? y или n')
    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Спасибо за игру!')
        break


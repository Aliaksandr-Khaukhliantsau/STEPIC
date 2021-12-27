# A poker deck contains 52 cards. Each card has a suit of either clubs, diamonds, hearts, or spades (denoted C, D, H,
# S). Each card also has a value of either 2 through 10, jack, queen, king, or ace (denoted 2, 3, 4, 5, 6, 7, 8, 9,
# 10, J, Q, K, A). For scoring purposes card values are ordered as above, with 2 having the lowest and ace the
# highest value. The suit has no impact on value.
#
# A poker hand consists of five cards. Poker hands are ranked by the following partial order from lowest to highest.
#
#
#
# High Card
# Hands which do not fit any higher category are ranked by the value of their highest card.
#
# Pair
# Two of the five cards in the hand have the same value.
#
# Two Pairs
# The hand contains two different pairs.
#
# Three of a Kind
# Three of the cards in the hand have the same value.
#
# Straight
# Hand contains five cards with consecutive values.
#
# Flush
# Hand contains five cards of the same suit.
#
#
# Full House
# Three cards of the same value, with the remaining two cards forming a pair.
#
# Four of a Kind
# Four cards with the same value.
#
# Straight Flush
# Five cards of the same suit in numerical order.
#
#
# Royal Flush
# Consists of the ace, king, queen, jack and ten of a suit.
#
#
# Напишите программу, которая получает на вход пять карт и выводит старшую покерную комбинацию, которая образуется
# этими картами.
#
# Формат ввода:
# Одна строка, на которой указаны пять карт в формате <value><suit>, записанные через пробел.
#
# Формат вывода:
# Название старшей комбинации, сформировавшейся на пришедшем наборе.
#
# Sample Input:
#
# 10C JC QC KC AC
# Sample Output:
#
# Royal Flush

def func():
    # my_cards = input().split()
    my_cards = ['10C', 'JC', 'QC', 'KC', 'AC']

    order_value = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    suit = ('C', 'D', 'H', 'S')

    my_cards_value = ()  # or []
    my_cards_suit = ()  # or []

    for card in my_cards:
        my_cards_value.append(card[:-1])
        my_cards_suit.append(card[-1])

    my_cards_dict = dict(zip(my_cards_value, my_cards_suit))

    my_cards_value_set = set(my_cards_value)
    my_cards_suit_set = set(my_cards_suit)


    print(f'{my_cards_dict}\n{my_cards_value}\n{my_cards_suit}\n{my_cards_value_set}\n{my_cards_suit_set}')

    for k, v in my_cards_dict.items():
        pass

    if len(my_cards_suit_set) == 1:
        pass




func()
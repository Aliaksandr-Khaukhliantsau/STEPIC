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

import collections

def func():
    # my_cards = input().split()
    # my_cards = ['10C', 'JC', 'QC', 'KC', 'AC']
    # my_cards = ['4C', '5C', '6C', '7C', '8C']
    # my_cards = ['10C', '10D', '10H', '10S', 'AC']
    # my_cards = ['10C', '10H', '10D', 'KC', 'KS']
    # my_cards = ['2C', 'JC', '8C', '4C', 'AC']
    # my_cards = ['10C', 'JC', 'QD', 'KH', 'AS']
    # my_cards = ['10C', '10H', '10D', 'KC', '2C']
    # my_cards = ['10C', '10H', 'QC', 'QD', 'AC']
    # my_cards = ['10C', '10H', 'QH', 'KD', 'AS']
    # my_cards = ['10C', '9H', 'QH', '2D', 'AS']


    my_cards = ['5S', '3H', '6C', '7C', '4S']



    order_value_tuple = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    order_value_str = (''.join(order_value_tuple))
    suit = ('C', 'D', 'H', 'S')

    my_cards_value_list = []
    my_cards_suit_list = []




    for card in my_cards:
        my_cards_value_list.append(card[:-1])
        my_cards_suit_list.append(card[-1])

    my_cards_value_str = (''.join(my_cards_value_list))
    my_cards_suit_str = (''.join(my_cards_suit_list))
    my_cards_dict = dict(zip(my_cards_value_list, my_cards_suit_list))
    my_cards_value_set = set(my_cards_value_list)
    my_cards_suit_set = set(my_cards_suit_list)

    for i in range(len(my_cards_value_list)):
        if my_cards_value_list[i].isdigit():
            my_cards_value_list[i] = int(my_cards_value_list[i])
        elif my_cards_value_list[i] == 'J':
            my_cards_value_list[i] = 11
        elif my_cards_value_list[i] == 'Q':
            my_cards_value_list[i] = 12
        elif my_cards_value_list[i] == 'K':
            my_cards_value_list[i] = 13
        elif my_cards_value_list[i] == 'A':
            my_cards_value_list[i] = 14

    my_cards_value_list.sort()



    print(f'{my_cards_dict}\n{my_cards_value_list}\n{my_cards_suit_list}\n{my_cards_value_set}\n{my_cards_suit_set}')


    m_k_v_c = collections.Counter(my_cards_value_list)
    m_k_s_c = collections.Counter(my_cards_suit_list)


    print(m_k_v_c)
    print(m_k_s_c)
    #
    print(m_k_v_c.values())
    print(m_k_s_c.values())

    if len(m_k_s_c) == 1:
        if my_cards_value_list == ['10', 'J', 'Q', 'K', 'A']:
            print('Royal Flush')
        elif my_cards_value_str in order_value_str:
            print('Straight Flush')
        elif len(my_cards_value_set) == 5:
            print('Flush')

    else:
        if my_cards_value_str in order_value_str:
            print('Straight')
        elif set(m_k_v_c.values()) == {4, 1}:
            print('Four of a Kind')
        elif set(m_k_v_c.values()) == {3, 2}:
            print('Full House')
        elif set(m_k_v_c.values()) == {3, 1}:
            print('Three of a Kind')
        elif list(m_k_v_c.values()).count(2) == 2:
            print('Two Pairs')
        elif list(m_k_v_c.values()).count(1) == 3:
            print('Pair')
        else:
            print('High Card')



func()
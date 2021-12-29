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

from collections import Counter


def func():
    hand = input().split()
    val_str = '234567891011121314'
    hand_val = []
    hand_suit = []
    hand_val_str = ''

    for card in hand:
        hand_val.append(card[:-1])
        hand_suit.append(card[-1])

    for i in range(len(hand_val)):
        if hand_val[i].isdigit():
            hand_val[i] = int(hand_val[i])
        elif hand_val[i] == 'J':
            hand_val[i] = 11
        elif hand_val[i] == 'Q':
            hand_val[i] = 12
        elif hand_val[i] == 'K':
            hand_val[i] = 13
        elif hand_val[i] == 'A':
            hand_val[i] = 14

    hand_val.sort()

    for val in hand_val:
        hand_val_str += str(val)

    if len(set(hand_suit)) == 1:
        if hand_val == [10, 11, 12, 13, 14]:
            print('Royal Flush')
        elif hand_val_str in val_str:
            print('Straight Flush')
        elif len(set(hand_val)) == 5:
            print('Flush')

    else:
        if hand_val_str in val_str:
            print('Straight')
        elif set(Counter(hand_val).values()) == {4, 1}:
            print('Four of a Kind')
        elif set(Counter(hand_val).values()) == {3, 2}:
            print('Full House')
        elif set(Counter(hand_val).values()) == {3, 1}:
            print('Three of a Kind')
        elif list(Counter(hand_val).values()).count(2) == 2:
            print('Two Pairs')
        elif list(Counter(hand_val).values()).count(1) == 3:
            print('Pair')
        else:
            print('High Card')


func()

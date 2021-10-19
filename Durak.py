def func(card_1, card_2):
    print(card_1, card_2)
    #    return
    if card_1[1] == card_2[1]:
        if int(card_1[0]) > int(card_2[0]):
            return 'First'
        elif int(card_1[0]) < int(card_2[0]):
            return 'Second'
        else:
            return 'Error'


def durak_card_1(val, card_1):
    if val == '1':
        card_1.append('10')
    else:
        card_1.append(val)
    return card_1


def durak_card_2(val, card_2):
    if val == '1':
        card_2.append('10')
    else:
        card_2.append(val)
    return card_2


def durak(suits, values, cards, trump):
    card_1 = []
    card_2 = []
    for val in values:
        if val == cards[0][0]:
            card_1 = durak_card_1(val, card_1)
        if val == cards[1][0]:
            card_2 = durak_card_2(val, card_2)

    for suit in suits:
        if suit == cards[0][-1]:
            card_1.append(suit)
        if suit == cards[1][-1]:
            card_2.append(suit)

    func(card_1, card_2)


#    return card_1, card_2


suits = ['C', 'D', 'H', 'S']
values = ['6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A']
cards = input().split()
trump = input()
print(durak(suits, values, cards, trump))

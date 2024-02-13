import json

NUMBER_OF_CARDS = 52

data = {}
data['cards'] = []

for i in range(1, NUMBER_OF_CARDS+1):
    if i < 14:
        suit = "Hearts"
    elif i < 27:
        suit = "Diamonds"
    elif i < 40:
        suit = "Spades"
    else:
        suit = "Clubs"

    CardNumber = i % 13

    if CardNumber == 1:
        name = "Ace"
    if CardNumber == 2:
        name = "Two"
    if CardNumber == 3:
        name = "Three"
    if CardNumber == 4:
        name = "Four"
    if CardNumber == 5:
        name = "Five"
    if CardNumber == 6:
        name = "Six"
    if CardNumber == 7:
        name = "Seven"
    if CardNumber == 8:
        name = "Eight"
    if CardNumber == 9:
        name = "Nine"
    if CardNumber == 10:
        name = "Ten"
    if CardNumber == 11:
        name = "Jack"
    if CardNumber == 12:
        name = "Queen"
    if CardNumber == 0:
        name = "King"
    
    data['cards'].append({
        'id': i,
        'name': name,
        'suit': suit
    })

    with open('cards.json', 'w') as outfile:
        json.dump(data, outfile)
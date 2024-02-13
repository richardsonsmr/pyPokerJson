import json
import random

hand = []
discard = []
json_card_file_name = 'cards.json'

def displayCards (json_card_file_name, collection_of_cards):
    str_list_collection_of_cards = []

    with open(json_card_file_name) as json_file:
        card_collection_from_json = json.load(json_file)

        for card in collection_of_cards:
            str_list_collection_of_cards.append(card_collection_from_json['cards'][card]['name'] + " of " + card_collection_from_json['cards'][card]['suit'])
    
    return str_list_collection_of_cards

def drawSingleCard (json_card_file_name, collection_of_cards, collection_of_used_cards):
    with open(json_card_file_name) as json_file:
        card_collection_from_json = json.load(json_file)

        number_of_cards_in_collection = len(card_collection_from_json['cards'])

        card_id = random.randint(1, number_of_cards_in_collection)

        while (card_id in hand or card_id in discard ):
            card_id = random.randint(1, number_of_cards_in_collection)

        return card_id       

def drawHand (number_of_cards_to_draw, collection_of_cards, collection_of_used_cards):
    for i in range(number_of_cards_to_draw):
        collection_of_cards.append(drawSingleCard(json_card_file_name, collection_of_cards, collection_of_used_cards))
    
    return collection_of_cards

def discardSingleCard (discard_card_position, collection_of_cards):
    collection_of_cards[discard_card_position] = None
    return collection_of_cards

def determineVictory (collection_of_cards):
    if checkFlush(collection_of_cards):
        return "Winner Flush"
    
    if checkStraight(collection_of_cards):
        return "Winner Straight"
    
    if checkThreeOfAKind(collection_of_cards):
        return "Winner Three of a kind"

    pair_number = checkPairs(collection_of_cards)
    if pair_number == 2:
        return "Winner Two Pair"
    elif pair_number == 1:
        return "Winner One Pair"
    
    return "Loss"

def checkFlush(collection_of_cards):
    first_suit_check = 0
    second_suit_check = 0
    third_suit_check = 0
    forth_suit_check = 0

    for i in range(len(collection_of_cards)):
        card_value = int(collection_of_cards[i])
        if 0 <= card_value < 13:
            first_suit_check += 1
        elif 13 < card_value < 26:
            second_suit_check += 1
        elif 26 < card_value < 39:
            third_suit_check += 1
        else:
            forth_suit_check += 1

    if first_suit_check == 5:
        return True
    elif second_suit_check == 5:
        return True
    elif third_suit_check == 5:
        return True
    elif forth_suit_check == 5:
        return True
    else:
        return False

def checkStraight (collection_of_cards):
    sorted_hand = collection_of_cards
    for i in range(len(collection_of_cards)):
        sorted_hand[i] = collection_of_cards[i] % 13
        if sorted_hand[i] == 0:
            sorted_hand[i] = 13

    sorted_hand.sort()
    check_result = False

    for i in range(len(sorted_hand) - 1):
        print(sorted_hand[i])
        print(sorted_hand[i+1])
        if sorted_hand[i] + 1 == (sorted_hand[i + 1]):
            check_result = True
        else:
            check_result = False
            break

    return check_result

def checkPairs (collection_of_cards):
    number_of_pairs = 0
    collection_of_cards_to_check = collection_of_cards
    
    while len(collection_of_cards_to_check) > 0:
        card_to_check = collection_of_cards_to_check.pop() % 13
        for i in range(len(collection_of_cards)):
            if card_to_check == collection_of_cards_to_check[i] % 13:
                number_of_pairs += 1

    return number_of_pairs

# HOW DOES THIS WORK?
#hand = drawHand(5, hand)
drawHand(5, hand, discard)
print(displayCards(json_card_file_name, hand))

discard_index = input("Card(s) to change (0-5, seperated by comma, enter to finish, 6 for all):")
while not discard_index:
    discard_index = input("Card(s) to change (0-5, seperated by comma, enter to finish, 6 for all):")

if "0" in discard_index:
    discard_index = []
elif "6" in discard_index:
    discard_index = [1,2,3,4,5]
else:
    discard_index = discard_index.split(",")
    discard_index = list(map(int, discard_index))

if not (len(discard_index) == 0):
    for i in discard_index:
        hand_index = i - 1
        discard.append(hand[hand_index])
        hand = discardSingleCard(hand_index, hand)

for i in range(0,len(hand)):
    if hand[i] is None:
        hand[i] = drawSingleCard(json_card_file_name, hand, discard)

print(displayCards(json_card_file_name, hand))

print(displayCards(json_card_file_name, discard))

print(determineVictory(hand))
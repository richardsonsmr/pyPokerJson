import json
import random


json_card_file_name = 'cards.json'

with open(json_card_file_name) as json_file:
    deck = json.load(json_file)

hand = {}
hand['cards'] = []
size_of_hand = 5


def draw_card(deck):
    draw_card = random.randint(0, len(deck['cards']) - 1)
    while True:
        draw_card = random.randint(0, len(deck['cards']) - 1)
        if(deck['cards'][draw_card]['in_deck']):
            deck['cards'][draw_card]['in_deck'] = False
            return deck['cards'][draw_card]


def reset_deck(deck):
    count = 51
    while count > 0:
        deck['cards'][count]['in_deck'] = True
        count = count - 1


def draw_hand(deck, size_of_hand):
    while len(hand['cards']) < size_of_hand:
        new_card = draw_card(deck)
        hand['cards'].append({
            'name': new_card['name'],
            'suit': new_card['suit']
        })
    return hand


def find_matches(hand, size_of_hand):
    matches = 0
    for root_card in range(size_of_hand - 1):
        for compare_card in range(root_card + 1, size_of_hand):
            if(hand['cards'][root_card]['name'] == hand['cards'][compare_card]['name']):
                matches = matches + 1
    return matches


def find_suit_match(hand, size_of_hand):
    for i in range(1, size_of_hand):
        if(hand['cards'][0]['suit'] != hand['cards'][i]['suit']):
            return False
    return True


def find_ordered_set(hand, size_of_hand):
    string_list = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    for card_index in range(size_of_hand):
        if(hand['cards'][card_index]['name'] in string_list):
            replace_index = string_list.index(hand['cards'][card_index]['name'])
            string_list[replace_index] = "found"
        else:
            return False
    first_found_element = string_list.index("found")
    if(first_found_element > (len(string_list) - size_of_hand)):
        return False
    for i in range(first_found_element, first_found_element + size_of_hand):
        if(string_list[i] != "found"):
            return False
    return True


def ace_exists(hand, size_of_hand):
    for card_index in range(size_of_hand):
        if(hand['cards'][card_index]['name'] == "Ace"):
            return True
    return False

def reset_hand(hand):
    del hand['cards'][:]

hands_dealt = 0
reset_deck(deck)
reset_hand(hand)
draw_hand(deck, size_of_hand)
while True:
    win_type = "None"
    straight_marker = False
    hands_dealt = hands_dealt + 1
    #reset_deck(deck)
    #reset_hand(hand)
    #draw_hand(deck, size_of_hand)
    match_number = find_matches(hand, size_of_hand)    
    if(match_number == 6):
        win_type = "Four of a Kind"
    elif(match_number == 4):
        win_type = "Full House"
    elif(match_number == 3):
        win_type = "Three of a Kind"
    elif(match_number == 2):
        win_type = "Two Pair"
    elif(match_number == 1):
        win_type = "One Pair"

    if(find_ordered_set(hand, size_of_hand)):
        win_type = "Straight"
        straight_marker = True
    
    if(find_suit_match(hand, size_of_hand)):
        win_type = "Flush"
    
    if(win_type == "Flush" and straight_marker):
        win_type = "Straight Flush"
    
    if(win_type == "Straight Flush" and ace_exists(hand, size_of_hand)):
        win_type = "Royal Flush"
    
    #if(win_type != "None"):
    #    break
    if(hands_dealt > 1):
        break

    #Show first hand
    for card in range(size_of_hand):
        print(hand['cards'][card]['name'] + " of " + hand['cards'][card]['suit'])

    #Didn't win, draw cards
    draw_times = 5
    discard_set = []
    while(draw_times > 0):
        #get user input
        discard_index = input("Card to change (1-5, seperated by comma, 0 to finish):")
        #normalize it from human input to base 0
        discard_index = int(discard_index) - 1
        #check if they ended draw
        if(int(discard_index) < 0):
            break

        #check draw card to make sure they can't double hit that card
        if(discard_index in discard_set):
            print("Card already drawn")
            break
        discard_set.append(discard_index)

        hand['cards'][int(discard_index)] = draw_card(deck)
        draw_times = draw_times - 1
    
    

    


print("Hands dealt: " + str(hands_dealt))
print("Win type: " + win_type)
for card in range(size_of_hand):
    print(hand['cards'][card]['name'] + " of " + hand['cards'][card]['suit'])


#in order or one will match a lower value set
#matches = 6 is four of a kind
#matches = 4 is a full house
#matches = 3 is three of a kind
#matches = 2 is two pair
#matches = 1 is a pair

#print(hand)

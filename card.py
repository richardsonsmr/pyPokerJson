import json
import random

hand_by_id_number = []
hand = []


def read_card_json(json_file_name, number_of_cards_to_draw):
    with open(json_file_name) as json_file:
        deck_from_file_dictionary = json.load(json_file)

        number_of_cards_in_collection = len(deck_from_file_dictionary['cards'])

        while len(hand_by_id_number) < number_of_cards_to_draw:
            draw_by_id = random.randint(1, number_of_cards_in_collection)
            if not(draw_by_id in hand_by_id_number):
                hand_by_id_number.append(draw_by_id)

        print(number_of_cards_in_collection)
        print(hand_by_id_number)

        for card in hand_by_id_number:
            print(deck_from_file_dictionary['cards'][card]['name'] + "\t of " + deck_from_file_dictionary['cards'][card]['suit'])

read_card_json('cards.json', 5)


input_number_of_cards_to_draw = 99
while( input_number_of_cards_to_draw > 5):
    input_number_of_cards_to_draw = int(input("How many to draw (0-5): ") or 99)
    if input_number_of_cards_to_draw > 5:
        input_number_of_cards_to_draw = 99
        print("Invalid number")
    

print(input_number_of_cards_to_draw)
read_card_json('cards.json', input_number_of_cards_to_draw)

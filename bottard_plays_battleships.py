from default_map import get_default_map
import random as r
from map_replacement_and_ship_validation import getKeysByValue


def bot_choose_your_ship_placements():
    # letters and values dictionary
    alphabet_letters_and_value = {chr(y): y - 64 for y in range(65, 91)}  # {"A":1,...}
    valid_ship_lengths = [2, 3, 3, 4, 5]
    bot_ships_placement_notations = []
    horizontal_or_vertical_placement = ['H', 'V']
    letters_to_choose = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers_to_choose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    starting_notation = ''
    ending_notation = ''
    for i in range(5):  # 5 pairs of notations
        placement = r.choice(horizontal_or_vertical_placement)
        if placement == 'V':  # if vertical placement
            starting_edge_letter = r.choice(letters_to_choose)  # Choosing only between 1-6 because if 8 was chosen
            # we couldn't add 3.
            length = r.choice(valid_ship_lengths)
            valid_ship_lengths.remove(length)
            starting_edge_number = r.choice(numbers_to_choose[0:5])
            bot_ships_placement_notations.append(starting_edge_letter + str(starting_edge_number) + "-" +
                                                 starting_edge_letter + str(starting_edge_number +
                                                                            length - 1))  # appending pair
        elif placement == 'H':  # horizontal placement   (A10 - C10)
            starting_edge_letter = r.choice(letters_to_choose[0:4])
            length = r.choice(valid_ship_lengths)
            valid_ship_lengths.remove(length)
            starting_edge_number = r.choice(numbers_to_choose)
            bot_ships_placement_notations.append(starting_edge_letter + str(starting_edge_number) + "-" + str("".join(
                getKeysByValue(alphabet_letters_and_value,
                               int(alphabet_letters_and_value[starting_edge_letter]) + length - 1))) + str(
                starting_edge_number))
            # using join because getkeysbyvalue functions returns letter in a list e.g. ['A']

    return bot_ships_placement_notations


# AI OF BOTTARD!!

def bot_play(played_notations):  # at Battleships! V1, bottard bombards a random location on map
    letters_to_choose = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers_to_choose = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    output = r.choice(letters_to_choose) + str(r.choice(numbers_to_choose))
    while output in played_notations:
        output = r.choice(letters_to_choose) + str(r.choice(numbers_to_choose))

    return output
import colorama

from notation_to_list_indexes import convert_notation_to_index
from colorama import Fore

colorama.init()


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


def getKeysByValue(dictOfElements, valueToFind):
    list_of_keys = list()
    list_of_items = dictOfElements.items()
    for item in list_of_items:
        if item[1] == valueToFind:
            list_of_keys.append(item[0])
    return list_of_keys


def convert_ship_edges_to_individual_notations(notations_list):
    # also validates if ships collide
    # B3-B7  -> {"ship1":[B3,B4,B5,B6,B7],...}
    ships = {"ship1": [], "ship2": [], "ship3": [], "ship4": [], "ship5": []}
    ships_keys_list = ["ship1", "ship2", "ship3", "ship4", "ship5"]  # for "for loop" later
    valid_ship_lengths = [2, 3, 3, 4, 5]  # validation of accepted ships
    alphabet_letters_and_value = {chr(y): y - 64 for y in range(65, 91)}  # {"A":1,...}

    for index, notation in enumerate(notations_list):  # for each notation  (e.g. A3-A5)
        start_end_list = notation.split("-")
        start = start_end_list[0]  # A3
        end = start_end_list[1]  # A5
        chain = 0
        if start[0] == end[0]:  # Vertical placement  (A3-A5)
            while chain <= (int(end[1::]) - int(start[1])):  # while chain is equal to the difference of A5 - A3 = 2.
                # <=> do the loop 3 times (1 is the starting notation A3)
                # Using slice because of A6-A10 case
                var = ships[ships_keys_list[index]]  # taking list / ship's value
                var.append(start[0] + str(int(start[1]) + chain))  # A1-A3 => A1, B1, C1
                ships[ships_keys_list[index]] = var  # putting list back
                chain += 1
                # validating ship lengths
                # chain = ship's length, there remove one ship from ships lengths list

        else:  # Horizontal placement  (A3-C3)
            while chain <= alphabet_letters_and_value[end[0]] - alphabet_letters_and_value[start[0]]:
                # while chain is equal to the
                # difference of C3-A3 (C  - A)  = 2.

                var = ships[ships_keys_list[index]]  # getting List (current ship's value)
                var.append("".join(getKeysByValue(alphabet_letters_and_value,
                                                  int(alphabet_letters_and_value[start[0]] + chain))) + start[
                                                                                                        1::])  # using slice because of A10-E10 case
                # appending to current ship's list the starting letter of alphabet + another letter according to chain.
                # e.g. (A1-C1) => {'ship1':["A1","B1","C1]}
                # + start 1 because number will always
                # be the same in horizontal placement (e.g. A3-C3)
                ships[ships_keys_list[index]] = var  # putting the result in current ships value
                chain += 1

    given_ship_lengths = []  # validation of ship lengths
    for k in ships:
        given_ship_lengths.append(len(ships[k]))
    if sorted(given_ship_lengths) != valid_ship_lengths:
        return 'INVALID SHIP LENGTHS'

    # validation of ship's collision
    all_taken_notations = []

    for k in ships:  # appending all ship's lists to all taken notation
        all_taken_notations.append(ships[k])

    all_taken_notations = flatten_list(all_taken_notations)

    for i in all_taken_notations:
        if all_taken_notations.count(i) > 1:
            return "SHIP COLLISION"

    return ships


def replace_map_with_ships(map, notation):
    indexes = convert_notation_to_index(notation)
    map[int(indexes[0])][int(indexes[1])] = "█"  # e.g.  makes C4 = █
    return map





def replace_hit_map_with_hit_notation(map, notation):
    indexes = convert_notation_to_index(notation)
    map[int(indexes[0])][int(indexes[1])] = '▒'
    return map


def replace_map_with_red_square(map, notation):
    indexes = convert_notation_to_index(notation)
    map[int(indexes[0])][int(indexes[1])] = ('\033[31m' + '▒' + "\033[0m")
    return map


def replace_map_with_green_square(map, notation):
    indexes = convert_notation_to_index(notation)
    map[int(indexes[0])][int(indexes[1])] = ('\033[32m' + '▒' + "\033[0m")
    return map


def replace_map_with_magenta_square(map, notation):
    indexes = convert_notation_to_index(notation)
    map[int(indexes[0])][int(indexes[1])] = ('\033[35m' + '▒' + "\033[0m")
    return map


def convert_ships_and_notations_dictionary_to_ship_names_and_notations(dic):
    output = {'Carrier': [], 'Battleship': [], 'Cruiser': [], 'Submarine': [], 'Destroyer': []}
    one_three_length_in_output = False
    for ship in dic:
        if len(dic[ship]) == 5:
            output['Carrier'] = dic[ship]
        elif len(dic[ship]) == 4:
            output['Battleship'] = dic[ship]
        elif len(dic[ship]) == 3 and one_three_length_in_output == True:
            output['Cruiser'] = dic[ship]

        elif len(dic[ship]) == 3:
            output['Submarine'] = dic[ship]
            one_three_length_in_output = True
        elif len(dic[ship]) == 2:
            output['Destroyer'] = dic[ship]
    return output


def check_whether_ships_collide(ships: dict):
    all_taken_notations = []

    for k in ships:  # appending all ship's lists to all taken notation
        all_taken_notations.append(ships[k])

    all_taken_notations = flatten_list(all_taken_notations)

    for i in all_taken_notations:
        if all_taken_notations.count(i) > 1:
            return False
    return True

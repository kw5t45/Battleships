from print_map_function import print_maps
from validate_ship_placement_notation import validate_ship_notation, validate_single_notation
from map_replacement_and_ship_validation import replace_map_with_ships, convert_notation_to_index, \
    convert_ship_edges_to_individual_notations, convert_ships_and_notations_dictionary_to_ship_names_and_notations, \
    check_whether_ships_collide, replace_hit_map_with_hit_notation, \
    flatten_list, replace_map_with_red_square, replace_map_with_green_square, replace_map_with_magenta_square
from default_map import get_default_map
from classes import Player, Ship
from bottard_plays_battleships import bot_choose_your_ship_placements, bot_play
import time as t


default_map = get_default_map()

bot_hit_map = get_default_map()

print("\nYou must choose where your 5 ships are placed across the board. Bottard's ship placements are chosen "
      "randomly by him.\n" + "To choose where you wish to place your ships, input the notation of ships edges.",
      "\n\n")
#############
position_notations = []
# #############
for i in range(1, 6):
    position_notations.append(input(f'''Give the position you wish to place ship n.{i}: '''))
for index, notation in enumerate(position_notations):
    if not validate_ship_notation(notation):
        print(f"\n\nInvalid notation in ship n.{index + 1}! Please give notation in CharacterNumber-CharacterNumber "
              f"form only, "
              f"e.g. B3-B5")
        quit()

your_ships_and_individual_notations_dic = convert_ship_edges_to_individual_notations(position_notations)

if your_ships_and_individual_notations_dic == 'SHIP COLLISION':
    print('\nThe ships that you choose collide!')
    quit()
if your_ships_and_individual_notations_dic == 'INVALID SHIP LENGTHS':
    print('Invalid ship lengths! Valid ships lengths are only 2, 3, 3, 4, and 5!')
    quit()

# placing ships on map

for ship in your_ships_and_individual_notations_dic:  # returns dictionary
    # ship / key has list as value
    list_of_notations_of_each_ship = your_ships_and_individual_notations_dic[ship]
    for x in list_of_notations_of_each_ship:
        replace_map_with_ships(default_map, x)

while True:  # Checking if bottards ships collide. If the do, bottard chooses new placements.
    bottards_ships_and_individual_notations = convert_ship_edges_to_individual_notations(
        bot_choose_your_ship_placements())
    if bottards_ships_and_individual_notations == 'SHIP COLLISION':
        continue
    else:
        break

# converting notation dictionaries to dictionaries with ship's names
bottards_ships_and_notations_with_names = convert_ships_and_notations_dictionary_to_ship_names_and_notations(
    bottards_ships_and_individual_notations)
players_ships_and_notations_with_names = convert_ships_and_notations_dictionary_to_ship_names_and_notations(
    your_ships_and_individual_notations_dic)

# creating objects

player1 = Player('You')
player2 = Player('Bot')

players_ship_1 = Ship('Your Carrier', len(players_ships_and_notations_with_names['Carrier']), players_ships_and_notations_with_names['Carrier'])
players_ship_2 = Ship('Your Battleship', len(players_ships_and_notations_with_names['Battleship']), players_ships_and_notations_with_names['Battleship'])
players_ship_3 = Ship('Your Cruiser', len(players_ships_and_notations_with_names['Cruiser']), players_ships_and_notations_with_names['Cruiser'])
players_ship_4 = Ship('Your Submarine', len(players_ships_and_notations_with_names['Submarine']), players_ships_and_notations_with_names['Submarine'])
players_ship_5 = Ship('Your Destroyer', len(players_ships_and_notations_with_names['Destroyer']), players_ships_and_notations_with_names['Destroyer'])

bots_ship_1 = Ship('Bottards Carrier', len(bottards_ships_and_notations_with_names['Carrier']), bottards_ships_and_notations_with_names['Carrier'])
bots_ship_2 = Ship('Bottards Battleship', len(bottards_ships_and_notations_with_names['Battleship']), bottards_ships_and_notations_with_names['Battleship'])
bots_ship_3 = Ship('Bottards Cruiser', len(bottards_ships_and_notations_with_names['Cruiser']), bottards_ships_and_notations_with_names['Cruiser'])
bots_ship_4 = Ship('Bottards Submarine', len(bottards_ships_and_notations_with_names['Submarine']), bottards_ships_and_notations_with_names['Submarine'])
bots_ship_5 = Ship('''Bottards Destroyer''', len(bottards_ships_and_notations_with_names['Destroyer']),bottards_ships_and_notations_with_names['Destroyer'])

players_objects = [players_ship_1, players_ship_2, players_ship_3, players_ship_4, players_ship_5]
bots_objects = [bots_ship_1, bots_ship_2, bots_ship_3, bots_ship_4, bots_ship_5]


players_played_moves = []
bots_played_moves = []

'''MAIN PART'''


print('\nGame is starting!\n')
while True:
    print_maps(default_map, bot_hit_map)
    print('\nChoose the notation you want to bomb!')

    player1_chosen_notation = input()
    while not validate_single_notation(player1_chosen_notation):
        print('Notation should be only in CharNum form!')
        player1_chosen_notation = input()
    while player1_chosen_notation in players_played_moves:
        print('You chose a notation that you already bombed! Please choose a new one!')
        player1_chosen_notation = input()
    if player1_chosen_notation not in players_played_moves:
        players_played_moves.append(player1_chosen_notation)

    replace_hit_map_with_hit_notation(bot_hit_map, player1_chosen_notation)
    # print_maps(default_map, bot_hit_map)

    # checking if players input hit an enemy ship
    for i in bots_objects:
        if player1_chosen_notation in i.notations:
            i.ship_got_hit()  # bots ship is hit
            replace_map_with_green_square(bot_hit_map, player1_chosen_notation)
            break
        else:  # missed
            replace_map_with_red_square(bot_hit_map, player1_chosen_notation)

        i.check_if_ship_got_sunk()

    print('Bottard is choosing a location!')
    t.sleep(2)
    player2_chosen_notation = bot_play(bots_played_moves)
    bots_played_moves.append(player2_chosen_notation)

    # checking if bots input hit a ship

    for i in players_objects:
        if player2_chosen_notation in i.notations:
            i.ship_got_hit()  # players ship is hit
            replace_map_with_magenta_square(default_map,player2_chosen_notation)
            break
        else:
            replace_map_with_red_square(default_map, player2_chosen_notation)

        i.check_if_ship_got_sunk()

    # Checking if game is over

    total_of_players_sunk_ships = []
    total_of_bots_sunk_ships = []

    for obj in players_objects:
        total_of_players_sunk_ships.append(obj.ship_is_sunk_boolean())
    for obj in bots_objects:
        total_of_bots_sunk_ships.append(obj.ship_is_sunk_boolean())

    if total_of_players_sunk_ships.count(True) == 5:
        player1.player_won()
        break
    elif total_of_bots_sunk_ships.count(True) == 5:
        player2.player_won()
        break
    total_of_players_sunk_ships.clear()
    total_of_bots_sunk_ships.clear()
quit()
class Player:
    player = ''
    has_won = False

    def __init__(self, name_of_player):
        self.player = name_of_player

    def player_won(self):
        if self.player == 'You':
            print(f'\n\n{self.player} have won the game! Congratulations!')

        else:
            print(f'{self.player}tard has won the game! You lost!')


class Ship:
    name_of_ship = ''
    length_of_ship = 0
    times_that_ship_got_hit = 0

    def __init__(self, name, length, notations):
        self.length_of_ship = length
        self.name_of_ship = name
        self.notations = notations

    def ship_got_hit(self):  # if ship gets hit
        print(f'\n{self.name_of_ship} got hit!')
        self.times_that_ship_got_hit += 1
        return ''

    def check_if_ship_got_sunk(self):  # checking if ship got sunk
        if self.times_that_ship_got_hit == self.length_of_ship:
            print(f'{self.name_of_ship}  has been sunk!')

    def ship_is_sunk_boolean(self):
        if self.length_of_ship == self.times_that_ship_got_hit:
            return True  # is sunk
        else:
            return False

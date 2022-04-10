class Player:
    player = ''
    has_won = False

    def __init__(self, name_of_player):
        self.player = name_of_player

    def player_won(self):
        self.has_won = True
        print(f'Player {self.player} has won the game!')
        quit()


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
            print(f'Oh no! Your {self.name_of_ship} ship has been sunk!')
        return ''

    def ship_is_sunk_boolean(self):
        if self.length_of_ship == self.times_that_ship_got_hit:
            return True  # is sunk
        return False

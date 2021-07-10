import random


class Grid:
    def __init__(self):
        self.gl = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.choice = [self.gl[1], self.gl[3], self.gl[7], self.gl[9]]
        self.choice2 = [self.gl[2], self.gl[8], self.gl[4], self.gl[6]]
        self.grid = f"""
            [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]
            [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]
            [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]
    """

    def display_grid(self):
        return self.grid


class Players(Grid):
    def __init__(self):
        super().__init__()

        self.player_name = ""
        self.cpu_player_name = ""
        ############
        self.symbols = ['x', 'o']
        self.player_symbol = ''
        self.CPU_symbol = ''
        self.players = []
        ##########
        self.player_names = ['Player', 'CPU']
        self.starter = random.choice(self.player_names)
        self.random = random.choice(self.choice)
        # print(self.random)
        self.random2 = random.choice(self.choice2)
        # print(self.random2)

    def player_creator(self):
        self.player_name = input('Enter Name: ')
        self.cpu_player_name = input('Enter CPU Name: ')
        return f"{self.player_name} VS CPU {self.cpu_player_name}"

    def symbol_selector(self):
        while self.player_symbol not in self.symbols:
            self.player_symbol = input("\nSelect your symbol x / o: ")
        if self.player_symbol == self.symbols[0]:
            self.CPU_symbol = self.symbols[1]
        else:
            self.CPU_symbol = self.symbols[0]
        return f"{self.player_name} plays '{self.player_symbol}' VS CPU '{self.cpu_player_name}' plays {self.CPU_symbol}"

    def game_starter(self):
        print(input("\n Press enter to select starter: "))
        print(f" \n{self.starter} plays first. ")

        return self.starter

    def cpu_hand(self):

        if self.gl[5] == " ":
            self.gl[5] = self.CPU_symbol
        elif self.gl[1] == " ":
            self.gl[1] = self.CPU_symbol
        elif self.gl[3] == " ":
            self.gl[3] = self.CPU_symbol
        elif self.gl[7] == " ":
            self.gl[7] = self.CPU_symbol
        elif self.gl[2] == " ":
            self.gl[2] = self.CPU_symbol
        elif self.gl[4] == " ":
            self.gl[4] = self.CPU_symbol
        elif self.gl[6] == " ":
            self.gl[6] = self.CPU_symbol
        elif self.gl[8] == " ":
            self.gl[8] = self.CPU_symbol
        # print(self.gl)
        self.grid = f"""
                        [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]
                        [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]
                        [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]
                """

        return self.grid

    def cpu_hand2(self):
        if self.gl[5] == " ":
            self.gl[5] = self.CPU_symbol
        elif self.random == " ":
            self.random = self.CPU_symbol
        elif self.random2 == " ":
            self.random2 = self.CPU_symbol

        self.grid = f"""

                                [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]

                                [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]

                                [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]


                        """

        return self.grid


    def player_hand(self):
        while True:
            # Used a try/except method to solve an incorrect input issue
            try:
                # Player inputs his move
                self.player_choice = int(input('\nChoose your move from 1 to 9:  '))
                print(self.player_choice)
                print(self.gl[self.player_choice])

                # If not available, the player has to choose another cell
                while self.gl[self.player_choice] != " ":
                    self.player_choice = int(input('\nChoice not available. Choose from 1 to 9:  '))
                else:
                    self.gl[self.player_choice] = self.player_symbol

                # print(gl)

                # Had to declare again the grid in order to make any changes on it
                self.grid = f"""
                [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]
                [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]
                [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]
        """
                return self.grid

            except:
                pass
            print("\nIncorrect input. Choose from 1 to 9:  ")

    def test_winner(self):
        # Iterating the player symbols and checking for any winning combo
        # Issue with break - after winning the game continues

        for i in self.symbols:
            # print(i)
            if self.gl[1] == self.gl[2] == self.gl[3] == i or \
                    self.gl[4] == self.gl[5] == self.gl[6] == i or \
                    self.gl[7] == self.gl[8] == self.gl[9] == i or \
                    self.gl[1] == self.gl[5] == self.gl[9] == i or \
                    self.gl[3] == self.gl[5] == self.gl[7] == i or \
                    self.gl[1] == self.gl[4] == self.gl[7] == i or \
                    self.gl[2] == self.gl[5] == self.gl[8] == i or \
                    self.gl[3] == self.gl[6] == self.gl[9] == i:
                print(f'{i} won!')

                return exit()

        else:
            return False

    def test_fullList(self):
        if " " in self.gl[1:]:
            # print("Not full")
            return False
        else:
            return True


grid = Grid()

players = Players()

print(players.player_creator())
print(players.symbol_selector())
print(players.game_starter())
# print(grid.display_grid())
# print(players.player_hand())
# print(players.cpu_hand())
# print(players.test_fullList())
# print(players.player_hand())
# print(players.cpu_hand())
# print(players.player_hand())
#
# print(players.cpu_hand())
# print(players.player_hand())
# print(players.cpu_hand())
# print(players.test_winner())


if players.game_starter()=="Player":
    while players.test_fullList() is False:
        print(players.player_hand())
        players.test_winner()
        print(players.cpu_hand())
        players.test_winner()


elif players.game_starter()=="CPU":
    while players.test_fullList() is False:
        print(players.cpu_hand())
        players.test_winner()
        print(players.player_hand())
        players.test_winner()
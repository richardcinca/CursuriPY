import random


class Grid:
    def __init__(self):
        self.gl = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

        self.grid = f"""
            [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]
            [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]
            [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]
    """

    def display_grid(self):
        return self.grid


class ExceptionPlayerHand(ValueError):

    def _init_(self, message):
        self.message = message

    def _str_(self):
        return str(self.message)


class ExceptionPlayerHandString(TypeError):

    def _init_(self, message):
        self.message = message

    def _str_(self):
        return str(self.message)


class Players(Grid):
    def __init__(self):
        super().__init__()
        self.player_name = input('Enter Name: ')
        self.cpu_player_name = input('Enter CPU Name: ')
        self.symbols = ['x', 'o']
        self.player_symbol = 'Symbol1'
        self.CPU_symbol = 'Symbol2'
        self.players = []
        self.player_names = [self.player_name, self.cpu_player_name]
        self.starter = random.choice(self.player_names)
        self.starter_index = self.player_names.index(self.starter)
        self.player_choice = 'default'

    def __str__(self):
        self.player_creator()
        self.symbol_selector()
        self.game_starter()
        if self.starter_index == 0:
            while self.test_full_list() is False:
                self.player_hand()
                self.test_winner()
                self.cpu_hand()
                self.test_winner()

        elif self.starter_index == 1:
            while self.test_full_list() is False:
                self.cpu_hand()
                self.test_winner()
                self.player_hand()
                self.test_winner()

    def player_creator(self):
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

        print(f"""
                        [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]
                        [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]
                        [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]
                """)
        return None

    def player_hand(self):
        while True:
            try:
                self.player_choice = input('\nChoose your move from 1 to 9:  ')
                if str(self.player_choice).isdigit() is False :
                    raise ExceptionPlayerHandString
                elif int(self.player_choice) not in range(1, 10):
                    raise ExceptionPlayerHand
                self.player_choice = int(self.player_choice)
                while self.gl[self.player_choice] != " ":
                    self.player_choice = input('\nChoice not available. Choose from 1 to 9:  ')
                    if str(self.player_choice).isdigit() is False:
                        raise ExceptionPlayerHandString
                    elif int(self.player_choice) not in range(1, 10):
                        raise ExceptionPlayerHand
                    self.player_choice = int(self.player_choice)

                else:
                    self.gl[self.player_choice] = self.player_symbol
                print(f"""
                [{self.gl[1]}]  [{self.gl[2]}]  [{self.gl[3]}]
                [{self.gl[4]}]  [{self.gl[5]}]  [{self.gl[6]}]
                [{self.gl[7]}]  [{self.gl[8]}]  [{self.gl[9]}]
        """)
                return None
            except ExceptionPlayerHandString:
                print("\nIncorrect input. Choose only numbers from 1 to 9:  ")
            except ExceptionPlayerHand:
                print("\nIncorrect input. Choose from 1 to 9:  ")

    def test_winner(self):

        for i in self.symbols:

            if self.gl[1] == self.gl[2] == self.gl[3] == i or \
                    self.gl[4] == self.gl[5] == self.gl[6] == i or \
                    self.gl[7] == self.gl[8] == self.gl[9] == i or \
                    self.gl[1] == self.gl[5] == self.gl[9] == i or \
                    self.gl[3] == self.gl[5] == self.gl[7] == i or \
                    self.gl[1] == self.gl[4] == self.gl[7] == i or \
                    self.gl[2] == self.gl[5] == self.gl[8] == i or \
                    self.gl[3] == self.gl[6] == self.gl[9] == i:
                print(f"'{i}' won!")

                return exit()

        else:
            return False

    def test_full_list(self):
        if " " in self.gl[1:]:

            return False
        else:
            return True


grid = Grid()
players = Players()
print(players)


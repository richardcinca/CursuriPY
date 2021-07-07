# Class Board:
    define grid_list
    define grid
# Class Players:
    define players
    define moves
    check_winnermove


import time
import random

class Game:
    def __init__(self):
        self.gl= [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.grid=f"""

            [{gl[1]}]  [{gl[2]}]  [{gl[3]}]

            [{gl[4]}]  [{gl[5]}]  [{gl[6]}]

            [{gl[7]}]  [{gl[8]}]  [{gl[9]}]


    """

    def starter(self):





class Players():
    #SUPER
    def __init__(self,name,symbol):
        super().__init__()
        self.name=name`
        self.symbol=symbol

    def CPU_hand():

        # Delayed the hand by 4sec
        time.sleep(4)

        if gl[5] == " ":
            gl[5] = CPU_symbol
        elif gl[1] == " ":
            gl[1] = CPU_symbol
        elif gl[3] == " ":
            gl[3] = CPU_symbol
        elif gl[7] == " ":
            gl[7] = CPU_symbol
        elif gl[2] == " ":
            gl[2] = CPU_symbol
        elif gl[4] == " ":
            gl[4] = CPU_symbol
        elif gl[6] == " ":
            gl[6] = CPU_symbol
        elif gl[8] == " ":
            gl[8] = CPU_symbol
        # print(gl)
        grid = f"""

            [{gl[1]}]  [{gl[2]}]  [{gl[3]}]

            [{gl[4]}]  [{gl[5]}]  [{gl[6]}]

            [{gl[7]}]  [{gl[8]}]  [{gl[9]}]


    """
        print(grid)

    # CPU_hand()

    def player_hand():

        while True:
            # Used a try/except method to solve an incorrect input issue
            try:
                # Player inputs his move
                player_choice = int(input('\nChoose your move from 1 to 9:  '))
                # print(player_choice)

                # If not available, the player has to choose another cell
                while self.gl[player_choice] != " ":
                    player_choice = int(input('\nChoice not available. Choose from 1 to 9:  '))
                else:
                    gl[player_choice] = player_symbol

                # print(gl)

                # Had to declare again the grid in order to make any changes on it
                grid = f"""

            [{gl[1]}]  [{gl[2]}]  [{gl[3]}]

            [{gl[4]}]  [{gl[5]}]  [{gl[6]}]

            [{gl[7]}]  [{gl[8]}]  [{gl[9]}]


    """
                print(grid)
                break
            except:
                pass
            print("\nIncorrect input. Choose from 1 to 9:  ")



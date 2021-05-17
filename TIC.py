# Main takeaways: 
    #   It's easier to work with functions and assemble them in the needed order, instead of just writing the program 
    #   Some parts of the code might be not necessary or could be written in a simpler way. Sometimes it's a "there I fixed it" kind of code. 
            # ex.1: maybe using a 10 element list for 9 cells. Should have used a matrix, df instead?
            # ex.2: trying to find a place to put the "break" - it seams unclear the concept of breaking when the code is a bit larger
            # ex.3: CPU_hand
    #   Try to create a clear "framework" for the code, a clear set of instructions with the order you need them to be executed. 
    # After that, mostly it's just translating the instructions


import time
import random


# Game description  print

print(""" 
        
        Tic-tac-toe is game for two players, X and O, 
        who take turns marking the spaces in a 3×3 grid. 
        The player who succeeds in placing three of their 
        marks in a diagonal, horizontal, or vertical row 
        is the winner. 

        """)
input("Press any key to continue: ")


# Declaration of Player by input
player=input("\nPlayer name: ")

# Symbols declaration
symbols=['x','o']
player_symbol=""
CPU_symbol=""

# While the player input for symbols is not x or o -> Player has to re-enter choice 

while player_symbol not in symbols:

    player_symbol=input("\nSelect your symbol x / o: ")

    # Depending on player's choice, the CPU's symbol will be auto-assigned

if player_symbol == symbols[0]:
    CPU_symbol = symbols[1]
else:
    CPU_symbol = symbols[0]

# Print the symbols for the players
print(f"\n{player} plays {player_symbol} VS CPU plays {CPU_symbol}")


# Declare a list to store the grid cells
gl= [" "," "," "," "," "," "," "," "," "," "]

# Create the grid using format to assign each cell the correspondent list element 
grid= f"""

        [{gl[1]}]  [{gl[2]}]  [{gl[3]}]

        [{gl[4]}]  [{gl[5]}]  [{gl[6]}]

        [{gl[7]}]  [{gl[8]}]  [{gl[9]}]

      
"""

# I declare a list of the players to use the random.choice() method and select the starter
# import random
player_names=[player,'CPU']
starter=random.choice(player_names)
print(f"\n{starter} plays first. ")
print(grid)
input("\nPress any key to start the game:   < PRESS KEY >")




#                                                                    F  U  N  C  T  I  O  N  S


#............................................................................................................................................................................


# TEST FULL GRID
# ------------------------------------------------------------------------
def test_fullList(gl):
    if " " in gl[1:]:
        #print("Not full")
        return False
    else:
        return True
# test_fullList()





# CPU HAND
# ------------------------------------------------------------------------
# # The function fills with the CPU_symbol the best available possition in this order : center,corners,middle(row/col) 
# -- should use random.choice() for the last two and create a function for the CPU to intercept the player's next move
#               def intercept() : should check player's filled positions, looks for a possible winning move and intercepts it by choosing that move.

def CPU_hand():

    # Delayed the hand by 4sec
    time.sleep(4)

    if gl[5] == " ":
        gl[5]= CPU_symbol
    elif gl[1] ==" ":
        gl[1]=CPU_symbol
    elif gl[3] ==" ":
        gl[3]=CPU_symbol
    elif gl[7] ==" ":
        gl[7]=CPU_symbol
    elif gl[2] ==" ":
        gl[2]=CPU_symbol
    elif gl[4] ==" ":
        gl[4]=CPU_symbol
    elif gl[6] ==" ":
        gl[6]=CPU_symbol
    elif gl[8] ==" ":
        gl[8]=CPU_symbol
    # print(gl)
    grid= f"""

        [{gl[1]}]  [{gl[2]}]  [{gl[3]}]

        [{gl[4]}]  [{gl[5]}]  [{gl[6]}]

        [{gl[7]}]  [{gl[8]}]  [{gl[9]}]

      
"""
    print(grid)
# CPU_hand()



# PLAYER HAND 
# ------------------------------------------------------------------------


def player_hand():
    
    while True:
        # Used a try/except method to solve an incorrect input issue
        try:
            # Player inputs his move 
            player_choice=int(input('\nChoose your move from 1 to 9:  '))
            # print(player_choice)

            # If not available, the player has to choose another cell
            while gl[player_choice] != " ":
                player_choice=int(input('\nChoice not available. Choose from 1 to 9:  '))
            else:
                gl[player_choice] = player_symbol
            
            #print(gl)

            # Had to declare again the grid in order to make any changes on it 
            grid= f"""

        [{gl[1]}]  [{gl[2]}]  [{gl[3]}]

        [{gl[4]}]  [{gl[5]}]  [{gl[6]}]

        [{gl[7]}]  [{gl[8]}]  [{gl[9]}]

      
"""
            print(grid)
            break
        except:
            pass
        print("\nIncorrect input. Choose from 1 to 9:  ")
          
# player_hand()


# TEST WINNER 
# ------------------------------------------------------------------------
players=[player_symbol,CPU_symbol]

def test_winner(gl,player_symbol,CPU_symbol):
    # Iterating the player symbols and checking for any winning combo 
    # Issue with break - after winning the game continues 

    for i in players:
        print(i)
        if gl[1] == gl[2] == gl[3] == i or \
            gl[4] == gl[5] == gl[6] == i or \
                gl[7] == gl[8] == gl[9] == i or \
                    gl[1] == gl[5] == gl[9] == i or\
                        gl[3] == gl[5] == gl[7] == i or\
                            gl[1] == gl[4] == gl[7] == i or\
                                gl[2] == gl[5] == gl[8] == i or\
                                    gl[3] == gl[6] == gl[9] == i:

                                

                                    print(f'{i} won!')
                                    break
        break                              
                                 
                                  
    else:       
        return False

# test_winner(gl,player_symbol,CPU_symbol)


#............................................................................................................................................................................








#                                                               ---------   G   A   M   E  -----------

#............................................................................................................................................................................

# Should be a better way to solve the order 


#
if starter is player:

    while test_fullList(gl) is False:
    
        player_hand()
        test_winner(gl,player_symbol,CPU_symbol)
        CPU_hand()
        test_winner(gl,player_symbol,CPU_symbol)


else:
    while test_fullList(gl) is False:
        CPU_hand()
        test_winner(gl,player_symbol,CPU_symbol)
        player_hand()
        test_winner(gl,player_symbol,CPU_symbol)
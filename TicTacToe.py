#####################################################
# Main Game                                         #
# Creator: MisterNSA aka Tobias Dominik Weber       #
# Date: 07.09.2020 0.1                              #
#####################################################

#from board import board
from player import player
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as ms

# Trivia:
# "# *** something *** #" means a Main Component like GUI, Functionality etc.
# "# --- something --- #" means a Subset of functions contained in a Main Component 


class TicTacToe():
    """The Main Class to play the game"""

    def __init__(self):
        """
        Asks for the game type and calls a function to init and play the game

        attributes:
        instance - Board - An instance of the Board class to represent the games board
        dict - switch - A self build switch to convert the numbers 1-9 to their corosponding coordinates
        Bool - board_init_true - Shows if board is already initialised. If so, only change it, dont init it again"""

        self.board_init_true = False

        # used later to make it easier for the Player to choose a field
        self.switch = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2]
        }
        # Start the game
        self.multiplayer()


    # ******************** GUI ******************** #
    def init_Board(self):
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        
        win = tk.Tk()
        win.title("TicTacToe")

        # -------------------- Button-Stringvalues -------------------- #
        self.button_1_text = tk.StringVar()
        self.button_1_text.set(self.grid[0][0])

        self.button_2_text = tk.StringVar()
        self.button_2_text.set(self.grid[1][0])

        self.button_3_text = tk.StringVar()
        self.button_3_text.set(self.grid[2][0])

        self.button_4_text = tk.StringVar()
        self.button_4_text.set(self.grid[0][1])

        self.button_5_text = tk.StringVar()
        self.button_5_text.set(self.grid[1][1])

        self.button_6_text = tk.StringVar()
        self.button_6_text.set(self.grid[2][1])

        self.button_7_text = tk.StringVar()
        self.button_7_text.set(self.grid[0][2])

        self.button_8_text = tk.StringVar()
        self.button_8_text.set(self.grid[1][2])

        self.button_9_text = tk.StringVar()
        self.button_9_text.set(self.grid[2][2])

        # -------------------- Actual Buttons -------------------- #
        # row 1
        self.button_1 = ttk.Button(
            win, textvariable=self.button_1_text, command=lambda: self.on_press(1))
        self.button_1.grid(row=0, column=0)

        self.button_2 = ttk.Button(
            win, textvariable=self.button_2_text, command=lambda: self.on_press(2))
        self.button_2.grid(row=0, column=1)

        self.button_3 = ttk.Button(
            win, textvariable=self.button_3_text, command=lambda: self.on_press(3))
        self.button_3.grid(row=0, column=2)
        # row 2
        self.button_4 = ttk.Button(
            win, textvariable=self.button_4_text, command=lambda: self.on_press(4))
        self.button_4.grid(row=1, column=0)

        self.button_5 = ttk.Button(
            win, textvariable=self.button_5_text, command=lambda: self.on_press(5))
        self.button_5.grid(row=1, column=1)

        self.button_6 = ttk.Button(
            win, textvariable=self.button_6_text, command=lambda: self.on_press(6))
        self.button_6.grid(row=1, column=2)
        # row 3
        self.button_7 = ttk.Button(
            win, textvariable=self.button_7_text, command=lambda: self.on_press(7))
        self.button_7.grid(row=2, column=0)

        self.button_8 = ttk.Button(
            win, textvariable=self.button_8_text, command=lambda: self.on_press(8))
        self.button_8.grid(row=2, column=1)

        self.button_9 = ttk.Button(
            win, textvariable=self.button_9_text, command=lambda: self.on_press(9))
        self.button_9.grid(row=2, column=2)

        self.board_init_true = True
        win.mainloop()


    def on_press(self, num):
        """
        Inserts players Symbol into the clicked square

        int - num = number of the clicked square
        string - current_player.symbol = X or O, the players Symbol that should be put in the square
        """
        if num == 1 and self.grid[0][0] == " ":
            self.grid[0][0] = self.current_player.symbol
            self.button_1_text.set(self.grid[0][0])
            self.evaluate_turn()
        elif num == 2 and self.grid[1][0] == " ":
            self.grid[1][0] = self.current_player.symbol
            self.button_2_text.set(self.grid[1][0])
            self.evaluate_turn()
        elif num == 3 and self.grid[2][0] == " ":
            self.grid[2][0] = self.current_player.symbol
            self.button_3_text.set(self.grid[2][0])
            self.evaluate_turn()
        elif num == 4 and self.grid[0][1] == " ":
            self.grid[0][1] = self.current_player.symbol
            self.button_4_text.set(self.grid[0][1])
            self.evaluate_turn()
        elif num == 5 and self.grid[1][1] == " ":
            self.grid[1][1] = self.current_player.symbol
            self.button_5_text.set(self.grid[1][1])
            self.evaluate_turn()
        elif num == 6 and self.grid[2][1] == " ":
            self.grid[2][1] = self.current_player.symbol
            self.button_6_text.set(self.grid[2][1])
            self.evaluate_turn()
        elif num == 7 and self.grid[0][2] == " ":
            self.grid[0][2] = self.current_player.symbol
            self.button_7_text.set(self.grid[0][2])
            self.evaluate_turn()
        elif num == 8 and self.grid[1][2] == " ":
            self.grid[1][2] = self.current_player.symbol
            self.button_8_text.set(self.grid[1][2])
            self.evaluate_turn()
        elif num == 9 and self.grid[2][2] == " ":
            self.grid[2][2] = self.current_player.symbol
            self.button_9_text.set(self.grid[2][2])
            self.evaluate_turn()


    # ******************** Multiplayer ******************** #
    def multiplayer(self):
        """Setup to represent the game with 2 human players

        variables:
        instances - Player1 and Player2 - Instances of player class who store name, Symbol and are used to determine whos turn it is 

        attributes:
        current_player - Points to the Instance of the player whos turn it is"""
        self.Player1 = player("X")
        self.Player1.turn = True
        self.Player2 = player("O")
        self.current_player = self.Player1
        self.Turn_count = 0
        # Setup Board
        if self.board_init_true == False:
            self.init_Board()
        


    def multiplayer_play_again(self):
        """Used to play again. Reset the Gamestate to the beginning of a new game"""
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        self.button_1_text.set(self.grid[0][0])
        self.button_2_text.set(self.grid[0][0])
        self.button_3_text.set(self.grid[0][0])
        self.button_4_text.set(self.grid[0][0])
        self.button_5_text.set(self.grid[0][0])
        self.button_6_text.set(self.grid[0][0])
        self.button_7_text.set(self.grid[0][0])
        self.button_8_text.set(self.grid[0][0])
        self.button_9_text.set(self.grid[0][0])

        self.multiplayer()


    # ******************** Functionality ******************** #
    def evaluate_turn(self):
        """ Reacts to the game Ending states """

        self.Turn_count += 1

        if self.Turn_count == 9:
            pass
            result = ms.askquestion(title="Draw!", message="Draw!\nDo you want to play again?")
            if result == "yes":
                self.multiplayer_play_again()
            else:
                sys.exit(0)
            ##### give out Draw in the GUI #####
        elif self.check_for_win():
            ##### give out the current Player and show, that he has won #####
            result = ms.askquestion(title=f"{self.current_player.symbol} won", message=f"{self.current_player.symbol} has won\nDo you want to play again?")
            if result == "yes":
                self.multiplayer_play_again()
            else:
                sys.exit(0)
        else:
            # Switch to the other Players turn
            self.set_current_player()


    def check_for_win(self):
        """
        Checks if Someone won the game

        If 3 fields in a line are equal and not " ", someone has won the game
        """
        # Check for a horizontal win
        if self.grid[0][0] == self.grid[0][1] == self.grid[0][2] != " ":
            return True
        elif self.grid[1][0] == self.grid[1][1] == self.grid[1][2] != " ":
            return True
        elif self.grid[2][0] == self.grid[2][1] == self.grid[2][2] != " ":
            return True

        # Check for a vertical win
        if self.grid[0][0] == self.grid[1][0] == self.grid[2][0] != " ":
            return True
        elif self.grid[0][1] == self.grid[1][1] == self.grid[2][1] != " ":
            return True
        elif self.grid[0][2] == self.grid[1][2] == self.grid[2][2] != " ":
            return True

        # Check for a horizontal win
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return True
        elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return True

        else:
            return False


    def set_current_player(self):
        """Switches the current player

        args:
        Player1 and Player2 - needs all players

        returns:
        Player1 or Player2, depending whos turn it is """
        # If Player 1 moved last, switch to player 2 and around
        if self.Player1.turn == True:
            self.Player1.turn = False
            self.Player2.turn = True
            self.current_player = self.Player2
        else:
            self.Player1.turn = True
            self.Player2.turn = False
            self.current_player = self.Player1

    



game = TicTacToe()

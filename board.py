#####################################################
# The Board of TicTacToe                            #
# Creator: MisterNSA aka Tobias Dominik Weber       #
# Date: 07.09.2020 0.9                              #
#####################################################

import tkinter as tk
import tkinter.ttk as ttk

"""
class board():
    ""Represents the grid of the game"

    def __init__(self):
        " 
        Initialise an empty grid

        attributes:
        2D Array - grid - Represents the 3x3 board and used to store the player symbols
        "
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def show_board(self):
        ""Prints the grid in an easier to read form"
        print(f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} ")
        print("---+---+---")
        print(f" {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} ")
        print("---+---+---")
        print(f" {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} ")

    def set_sign(self, sign, pos):
        "
        insert the players symbol at the selected field

        args:
        string - sign - The players symbol
        list - pos - x and y coordinates of the Field
        "
        x, y = pos
        self.grid[x][y] = sign

    def field_is_empty(self, pos):
        "
        Checks if the field is empty

        args:
        list - pos - x and y coordinates of the Field

        returns:
        True - if field is empty
        False - if field is not empty
        "
        x, y = pos
        if self.grid[x][y] == " ":
            return True
        else:
            return False
"""
# ---------- #


class board():
    """Represents the grid of the game"""

    def __init__(self):
        """ 
        Initialise an empty grid

        attributes:
        2D Array - grid - Represents the 3x3 board and used to store the player symbols
        """
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

        # only for test - DELETE
        player_symbol = "x"

        # --- GUI --- #
        win = tk.Tk()
        win.title("TicTacToe")

        # --- Button-Stringvalues #
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

        self.button_1_text = tk.StringVar()
        self.button_1_text.set(self.grid[0][0])

        # --- Actual Buttons --- #
        # row 1
        self.button_1 = ttk.Button(
            win, textvariable=self.button_1_text, command=lambda: self.on_press(1, player_symbol))
        self.button_1.grid(row=0, column=0)

        self.button_2 = ttk.Button(
            win, textvariable=self.button_2_text, command=lambda: self.on_press(2, player_symbol))
        self.button_2.grid(row=0, column=1)

        self.button_3 = ttk.Button(
            win, textvariable=self.button_3_text, command=lambda: self.on_press(3, player_symbol))
        self.button_3.grid(row=0, column=2)
        # row 2
        self.button_4 = ttk.Button(
            win, textvariable=self.button_4_text, command=lambda: self.on_press(4, player_symbol))
        self.button_4.grid(row=1, column=0)

        self.button_5 = ttk.Button(
            win, textvariable=self.button_5_text, command=lambda: self.on_press(5, player_symbol))
        self.button_5.grid(row=1, column=1)

        self.button_6 = ttk.Button(
            win, textvariable=self.button_6_text, command=lambda: self.on_press(6, player_symbol))
        self.button_6.grid(row=1, column=2)
        # row 3
        self.button_7 = ttk.Button(
            win, textvariable=self.button_7_text, command=lambda: self.on_press(7, player_symbol))
        self.button_7.grid(row=2, column=0)

        self.button_8 = ttk.Button(
            win, textvariable=self.button_8_text, command=lambda: self.on_press(8, player_symbol))
        self.button_8.grid(row=2, column=1)

        self.button_9 = ttk.Button(
            win, textvariable=self.button_9_text, command=lambda: self.on_press(9, player_symbol))
        self.button_9.grid(row=2, column=2)

        win.mainloop()

    def on_press(self, num, player_symbol):
        # num = number of squares clicked
        # player_symbol = X or O, the players Symbol that should be put in the square
        if num == 1 and self.grid[0][0] == " ":
            self.grid[0][0] = player_symbol
            self.button_1_text.set(self.grid[0][0])
        elif num == 2 and self.grid[1][0] == " ":
            self.grid[1][0] = player_symbol
            self.button_2_text.set(self.grid[1][0])
        elif num == 3 and self.grid[2][0] == " ":
            self.grid[2][0] = player_symbol
            self.button_3_text.set(self.grid[2][0])
        elif num == 4 and self.grid[0][1] == " ":
            self.grid[0][1] = player_symbol
            self.button_4_text.set(self.grid[0][1])
        elif num == 5 and self.grid[1][1] == " ":
            self.grid[1][1] = player_symbol
            self.button_5_text.set(self.grid[1][1])
        elif num == 6 and self.grid[2][1] == " ":
            self.grid[2][1] = player_symbol
            self.button_6_text.set(self.grid[2][1])
        elif num == 7 and self.grid[0][2] == " ":
            self.grid[0][2] = player_symbol
            self.button_7_text.set(self.grid[0][2])
        elif num == 8 and self.grid[1][2] == " ":
            self.grid[1][2] = player_symbol
            self.button_8_text.set(self.grid[1][2])
        elif num == 9 and self.grid[2][2] == " ":
            self.grid[2][2] = player_symbol
            self.button_9_text.set(self.grid[2][2])


b = board()
# TO DO: implement into code

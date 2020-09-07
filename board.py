#####################################################
# The Board of TicTacToe                            #
# Creator: MisterNSA aka Tobias Dominik Weber       #
# Date: 07.09.2020 0.9                              #
#####################################################

class board():
    """Represents the grid of the game"""

    def __init__(self):
        """ 
        Initialise an empty grid
        
        attributes:
        2D Array - grid - Represents the 3x3 board and used to store the player symbols
        """
        self.grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def show_board(self):
        """Prints the grid in an easier to read form"""
        print(f" {self.grid[0][0]} | {self.grid[0][1]} | {self.grid[0][2]} ")
        print("---+---+---")
        print(f" {self.grid[1][0]} | {self.grid[1][1]} | {self.grid[1][2]} ")
        print("---+---+---")
        print(f" {self.grid[2][0]} | {self.grid[2][1]} | {self.grid[2][2]} ")

    def set_sign(self, sign, pos):
        """
        insert the players symbol at the selected field
        
        args:
        string - sign - The players symbol
        list - pos - x and y coordinates of the Field
        """
        x, y = pos
        self.grid[x][y] = sign

    def field_is_empty(self, pos):
        """
        Checks if the field is empty
        
        args:
        list - pos - x and y coordinates of the Field

        returns:
        True - if field is empty
        False - if field is not empty
        """
        x, y = pos
        if self.grid[x][y] == " ":
            return True
        else:
            return False




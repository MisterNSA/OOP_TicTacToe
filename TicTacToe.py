#####################################################
# Main Game                                         #
# Creator: MisterNSA aka Tobias Dominik Weber       #
# Date: 07.09.2020 0.1                              #
#####################################################

from board import board
from player import player

class TicTacToe():
    """The Main Class to play the game"""

    def __init__(self):
        """
        Asks for the game type and calls a function to init and play the game
        
        attributes:
        instance - Board - An instance of the Board class to represent the games board
        Bool - game_running - Flag if the game still runs or if it is over
        dict - switch - A self build switch to convert the numbers 1-9 to their corosponding coordinates"""

        # Create the board
        self.Board = board()
        self.game_running = True
        # used later to make it easier for the Player to choose a field
        self.switch = {
                1: [0,0],
                2: [0,1],
                3: [0,2],
                4: [1,0],
                5: [1,1],
                6: [1,2],
                7: [2,0],
                8: [2,1],
                9: [2,2]
            }

        # Check if a multiplayer or singleplayer game should be created
        Valid = False
        while Valid == False:
            game = input("Do you want to play Multiplayer(m) or Singleplayer(s)?\n")
            if game.lower() == "m":
                Valid = True
                self.multiplayer()
            elif game.lower() == "s":
                Valid = True
                self.singleplayer()

    #
    # ----------------------------------------- Singleplayer -------------------------------------------
    #

    def singleplayer(self):
        """Setup to represent the game with 1 human player who plays against an algorithm"""
        #Player = player("X")
        pass

    #
    # ----------------------------------------- Multiplayer --------------------------------------------
    #

    def multiplayer(self):
        """Setup to represent the game with 2 human players
        
        variables:
        instances - Player1 and Player2 - Instances of player class who store name, Symbol and are used to determine whos turn it is 
        
        attributes:
        current_player - Points to the Instance of the player whos turn it is"""
        Player1 = player("X")
        Player1.turn = True
        Player2 = player("O")
        self.current_player = Player1
        Turn_count = 0

    # ------------------------- Main Game Loop --------------------------
        while self.game_running:
            # Ask Player where he wants to play his Symbol
            Valid = False
            while Valid == False:
                try:
                    coordinates = int(input("""
Where do you want to playe your symbol?
1|2|3
4|5|6
7|8|9\n"""))
                except:
                    print("This wasnt a number!")

                if coordinates < 10:
                    pos = self.switch.get(coordinates)
                    if self.Board.field_is_empty(pos):
                        Valid = True
                    else:
                        print("This field was already taken!")
                else:
                    print("The number wasnt between 1 and 9!")
                

            # Insert Players Symbol into the Board and show it
            self.Board.set_sign(self.current_player.symbol, pos)
            self.Board.show_board()

            # If someone has one, end the game
            Turn_count += 1
            if Turn_count == 9:
                print("Draw!")
                self.game_running = False
            elif self.check_for_win():
                print(f"{self.current_player.name} has won!")
                self.game_running = False
            else:
                # Switch to the other Players turn
                self.set_current_player(Player1, Player2)

    # ---------------------------------------------- Fuctionality -------------------------------
    def check_for_win(self):
        """
        Checks if Someone won the game
        
        If 3 fields in a line are equal and not " ", someone has won the game
        """
        # Check for a horizontal win
        if self.Board.grid[0][0] == self.Board.grid[0][1] == self.Board.grid[0][2] != " ":
            return True 
        elif self.Board.grid[1][0] == self.Board.grid[1][1] == self.Board.grid[1][2] != " ":
            return True 
        elif self.Board.grid[2][0] == self.Board.grid[2][1] == self.Board.grid[2][2] != " ":
            return True 

        # Check for a vertical win
        if self.Board.grid[0][0] == self.Board.grid[1][0] == self.Board.grid[2][0] != " ":
            return True 
        elif self.Board.grid[0][1] == self.Board.grid[1][1] == self.Board.grid[2][1] != " ":
            return True 
        elif self.Board.grid[0][2] == self.Board.grid[1][2] == self.Board.grid[2][2] != " ":
            return True 

        # Check for a horizontal win
        if self.Board.grid[0][0] == self.Board.grid[1][1] == self.Board.grid[2][2] != " ":
            return True 
        elif self.Board.grid[0][2] == self.Board.grid[1][1] == self.Board.grid[2][0] != " ":
            return True 
        
        else:
            return False

    def set_current_player(self, Player1, Player2):
        """Return the Players whos turn it is
        
        args:
        Player1 and Player2 - needs all players
        
        returns:
        Player1 or Player2, depending whos turn it is"""
        # If Player 1 moved last, switch to player 2 and around
        if Player1.turn == True:
            Player1.turn = False
            Player2.turn = True
            self.current_player = Player2
        else:
            Player1.turn = True
            Player2.turn = False
            self.current_player = Player1



game = TicTacToe()


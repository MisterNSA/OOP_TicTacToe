#####################################################
# Just used to store players name and symbol        #
# Creator: MisterNSA aka Tobias Dominik Weber       #
# Date: 07.09.2020 1.0                              #
#####################################################


class player():
    """Represents the player"""

    def __init__(self, symbol):
        """
        Init the player

        args:
        string - symbol - the players symbol

        attributes:
        string - symbol - Strores the players symbol
        Bool - turn - Stores if it is the Players Turn or not
        """
        self.symbol = symbol
        self.turn = False

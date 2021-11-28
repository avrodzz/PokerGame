from GameText import GameText
from PokerGameBaseConstants import PokerGameBaseConstants

# A Pot is a GameText (a text with a message, font size, font color, and position) with a pot amount that can be set.


class Pot(GameText):
    def __init__(self, amount=0, message=PokerGameBaseConstants.POT_MESSAGE, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE, fontColor=PokerGameBaseConstants.BLACK, x=0, y=0):
        super().__init__(message=message + str(amount),
                         fontSize=fontSize, fontColor=fontColor, x=x, y=y)
        self._potAmount = amount

    ## Accessor (Getter)
    #  @return self._potAmount (int) the amount of money in the pot
    #
    def getPotAmount(self):
        return self._potAmount

    ## Mutator (Setter)
    #  @param amount (int) changes the _potAmount to amount
    #
    def setPotAmount(self, amount):
        self._potAmount = amount

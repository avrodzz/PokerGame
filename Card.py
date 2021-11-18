# A Card has a suit and value.
class Card:
    # CONSTANTS
    #  NUM_OF_SUITS (int) the number of possible suits a card could have
    #  NUM_OF_VALUES (int) the number of possible values a card could have
    NUM_OF_SUITS = 4
    NUM_OF_VALUES = 13

    # CONSTANT LISTS
    #  SUITS (string[]) contains the suit names
    #  VALUES (string[]) contains the value names
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    VALUES = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
              'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']

    # CONSTANT DICTIONARIES
    #  FILESUITS (string) [key: 'suitName', value: 'the suit char needed to access the gif file']
    #  FILEVALUES (string) [key: 'valueName', value: 'the value char needed to acces the gif file']
    FILESUITS = {SUITS[0]: 'c', SUITS[1]: 'd', SUITS[2]: 'h', SUITS[3]: 's'}
    FILEVALUES = {VALUES[0]: '1', VALUES[1]: '2', VALUES[2]: '3', VALUES[3]: '4',
                  VALUES[4]: '5', VALUES[5]: '6', VALUES[6]: '7', VALUES[7]: '8',
                  VALUES[8]: '9', VALUES[9]: '10', VALUES[10]: '11', VALUES[11]: '12',
                  VALUES[12]: '13'}

    # IMAGE CONSTANTS
    GIF_SIZE_WIDTH = 73
    GIF_SIZE_HEIGHT = 97

    # Constructs a Card object with a suit and value.
    #  @param value (string) the value value
    #  @param suit (string) the suit value
    #
    def __init__(self, value='', suit=''):
        self._value = value
        self._suit = suit

    ## Accessor (Getter)
    #  @return self._suit (string) the suit of the card
    #
    def getSuit(self):
        return self._suit

    ## Accessor (Getter)
    #  @return self._value (string) the value of the card
    #
    def getValue(self):
        return self._value

    ## Accessor (Getter)
    #  @return the numeric value of self._value
    def getNumericValue(self):
        return int(Card.FILEVALUES[self._value])

    # Prints the string value and suit of the Card
    #  @return example: 'Ace of Hearts'
    def __repr__(self):
        return self._value + ' of ' + self._suit

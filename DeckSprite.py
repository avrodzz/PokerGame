from CardSprite import CardSprite
from random import shuffle

# A DeckSprite contains 52 CardSprites.


class DeckSprite:
    # Constructs a DeckSprite object with 52 CardSprites.
    #
    def __init__(self):
        self._deckSprite = []
        self.initSpriteDeck()

    ## Accessor (Getter)
    #  @return self._deckSprite (CardSprite[]) the array of CardSprites
    #
    def getDeckSprite(self):
        return self._deckSprite

    # Adds 52 CardSprites to the self._deckSprite
    #  The cards are added in clubs, diamonds, hearts, and spades order
    #  Uses the CardSprite dictionaries, numberOfSuits, and numberOfValues in order to get the correct values
    #
    def initSpriteDeck(self):
        for i in range(CardSprite.NUM_OF_SUITS):
            for j in range(CardSprite.NUM_OF_VALUES):
                tempCardSprite = CardSprite(
                    CardSprite.VALUES[j], CardSprite.SUITS[i])
                self._deckSprite.append(tempCardSprite)

    # Takes the in order deck of cards and mixes it up randomly.
    #  Using the shuffle function from the random library.
    #
    def shuffle(self):
        shuffle(self._deckSprite)

    # Pops a card from the end of the deck
    #  If there are no more cards in the deck then more cards are added and are shuffled
    #  If there are still cards in the deck then it pops one card from the deck
    #
    def dealCard(self):
        if len(self._deckSprite) == 0:
            self.initSpriteDeck()
            self.shuffle()
            temp = self._deckSprite.pop()
            return temp
        else:
            temp = self._deckSprite.pop()
            return temp

    # Draws the Deck of CardSprites to the screen.
    #  Prints 13 cards on four different rows
    #  @param screen (pygame Surface) the window where the content is being displayed
    #
    def draw(self, screen):
        XCount = 0
        YCount = 0

        for i in range(len(self._deckSprite)):
            if i < 13:
                screen.blit(self._deckSprite[i].getCardSprite().image,
                            (CardSprite.XOFFSET * XCount, YCount * CardSprite.YOFFSET))
                XCount += 1
                if XCount == 13:
                    XCount = 0
            elif 13 <= i < 26:
                YCount = 1
                screen.blit(self._deckSprite[i].getCardSprite().image,
                            (CardSprite.XOFFSET * XCount, YCount * CardSprite.YOFFSET))
                XCount += 1
                if XCount == 13:
                    XCount = 0
            elif 26 <= i < 39:
                YCount = 2
                screen.blit(self._deckSprite[i].getCardSprite().image,
                            (CardSprite.XOFFSET * XCount, YCount * CardSprite.YOFFSET))
                XCount += 1
                if XCount == 13:
                    XCount = 0
            else:
                YCount = 3
                screen.blit(self._deckSprite[i].getCardSprite().image,
                            (CardSprite.XOFFSET * XCount, YCount * CardSprite.YOFFSET))
                XCount += 1
                if XCount == 13:
                    XCount = 0

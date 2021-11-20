import pygame
from CardSprite import CardSprite

# A CardHandSprite is a hand of x amount of cards.


class CardHandSprite:
    # CONSTANTS
    NUM_OF_CARDS = 5
    INITIAL_POS_X = 0
    INITIAL_POS_Y = 0

    # Constructs a CardHandSprite with an empty hand
    #
    def __init__(self):
        self._hand = []
        self._numFaceUp = 0

    # Adds a CardSprite object to the CardSprite list (self._hand)
    #  @param deck (DeckSprite) the deck of CardSprites
    #

    def addCard(self, deck):
        cardSpriteTemp = deck.dealCard()
        # print(cardSpriteTemp)
        self._hand.append(cardSpriteTemp)

    # Pops a CardSprite object from the CardSprite list (self._hand)
    #
    def popCard(self):
        if len(self._hand > 0):
            self._hand.pop()

    ## Accessor (Getter)
    #  @return self._numFaceUp (int) the number of cards that are face up in the hand
    #
    def getNumFaceUp(self):
        return self._numFaceUp

    # Control the number of cards that are face up or not
    #
    def increaseNumFaceUp(self):
        if self._numFaceUp < CardHandSprite.NUM_OF_CARDS:
            self._numFaceUp += 1

    ## Accessor (Getter)
    #  @return len(self._hand) (int) the number of cards that are in the hand
    #
    def getNumOfCards(self):
        return len(self._hand)

    ## Accessor (Getter)
    #  @return self._hand (CardSprite[]) the list of CardSprites in the hand
    #
    def getHand(self):
        return self._hand

    # Draws the hand of CardSprites to the screen.
    #  Prints NUM_OF_CARDS on different rows
    #  @param screen (pygame Surface) the window where the content is being displayed
    #
    def draw(self, screen):
        for i in range(len(self._hand)):
            temp = self._hand[i]
            screen.blit(temp.getCardSprite().image, temp.getRect())

    # Set position of the top left corner of the CardSprites in the CardHandSprite list (self._hand)
    #  @param x (float) the x-coordinate position of the top left of the CardHandSprite object
    #  @param y (float) the y-coordniate position of the top top of the CardHandSprite object
    #
    def setPosition(self, x=INITIAL_POS_X, y=INITIAL_POS_Y):
        currentCardSprite = self._hand[0]
        currentCardSprite.setPosition(x, y)
        for i in range(1, len(self._hand)):
            temp = self._hand[i]
            temp.setPosition(currentCardSprite.getRect().x + i *
                             CardSprite.XOFFSET, currentCardSprite.getRect().y)

    # Set position of all cards in hand to the center of the screen
    #  @param screenWidth (float) the width of the screen
    #  @param screenHeight (float) the height of the screen
    #
    def centerOnScreen(self, screenWidth, screenHeight):
        self.setPosition(screenWidth / 2 - (CardSprite.XOFFSET *
                         (self.getNumOfCards() / 2)), screenHeight / 2 - CardSprite.YOFFSET / 2)

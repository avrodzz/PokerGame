import pygame
from Card import Card

# A CardSprite has all attributes of a Card and is a pygame sprite


class CardSprite(Card):
    # GIF FILE SIZE CONSTANTS
    XOFFSET = 75
    YOFFSET = 99

    # FILE PATH CONSTANTS
    FRONTOFCARDFILEPATH = 'DECK_OF_CARDS/'
    BACKOFCARDFILEPATH = 'DECK_OF_CARDS/back02.gif'
    GIF = '.gif'

    # Constructs a CardSprite object with a suit and value as a pygame sprite
    #  @param value (string) the value value
    #  @param suit (string) the suit value
    #
    def __init__(self, value='', suit='', x=0, y=0, flip=True):
        super().__init__(value, suit)
        self._images = [CardSprite.FRONTOFCARDFILEPATH + Card.FILEVALUES[value] + Card.FILESUITS[suit] + CardSprite.GIF,
                        CardSprite.BACKOFCARDFILEPATH]
        self._flipped = flip
        if self._flipped:
            self._cardImage = pygame.image.load(self._images[0])
        else:
            self._cardImage = pygame.image.load(self._images[1])
        self._cardSprite = pygame.sprite.Sprite()
        self._cardSprite.image = self._cardImage.convert()
        self._rect = self._cardSprite.image.get_rect()
        self._rect.x = x
        self._rect.y = y
        self._cardSprite.rect = self._rect

    ## Accessor (Getter)
    #  @return self._cardSprite (pygame Sprite) the card pygame sprite
    #
    def getCardSprite(self):
        return self._cardSprite

    ## Accessor (Getter)
    #  @return self._rect (Rect) the x- and y- coordinates of the sprite
    #
    def getRect(self):
        return self._rect

    # Moves the CardSprite object by an offset of x and y
    #  @param x (float) the x-offset
    #  @param y (float) the y-offset
    #
    def move(self, x, y):
        self._rect.x += x
        self._rect.y += y

    # Moves the CardSprite object to a fixed position
    #  @param x (float) the x-coordinate on the grid
    #  @param y (float) the y-coordinate on the grid
    #
    def setPosition(self, x, y):
        self._rect.x = x
        self._rect.y = y

    # Flips the CardSprite object (changes image from front to back gif)
    #  @return new CardSprite that is flipped with the same value, suit, position, but a different image
    #
    def flipCard(self):
        temp = self._flipped
        if temp:
            self._flipped = False
        else:
            self._flipped = True
        return CardSprite(self.getValue(), self.getSuit(), self._rect.x, self._rect.y, self._flipped)

    # Draws the CardSprite object to the screen
    #  @param screen (pygame Surface) the window where the content is being displayed
    def draw(self, screen):
        screen.blit(self._cardSprite.image, self._rect)

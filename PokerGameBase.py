import pygame
from pygame.locals import *
from CardSprite import CardSprite
from DeckSprite import DeckSprite
from CardHandSprite import CardHandSprite
from GameText import GameText
from Pot import Pot
from PokerGameBaseConstants import PokerGameBaseConstants
from HandScorer import HandScorer

# A PokerGameBase object is in charge of creating the pokerGame and its functionality.
# This includes drawing to the screen, [check,raise,fold], and playerInput.


class PokerGameBase:
    def __init__(self, width=PokerGameBaseConstants.SCREEN_WIDTH, height=PokerGameBaseConstants.SCREEN_HEIGHT, caption=PokerGameBaseConstants.SCREEN_CAPTION, backgroundColor=PokerGameBaseConstants.TABLE_RGB):
        pygame.init()
        self._width = width
        self._height = height
        self._raiseInput = ''

        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(caption)

        # Fill the background color to the screen
        self._screen.fill(backgroundColor)

        # GameText Objects
        self._titleText = GameText(
            message=PokerGameBaseConstants.TITLE_TEXT, fontSize=PokerGameBaseConstants.TITLE_FONT_SIZE)
        self._playerText = GameText(
            message=PokerGameBaseConstants.PLAYER_TEXT, fontSize=PokerGameBaseConstants.PLAYER_FONT_SIZE)
        self._aiText = GameText(message=PokerGameBaseConstants.AI_TEXT,
                                fontSize=PokerGameBaseConstants.PLAYER_FONT_SIZE)
        self._playOptionText = GameText(
            message=PokerGameBaseConstants.PLAY_OPTION_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._pot = Pot(amount=PokerGameBaseConstants.MINIMUM_WAGE)
        self._raiseInputText = GameText(message=PokerGameBaseConstants.RAISE_INPUT_TEXT +
                                   self._raiseInput, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._enterOptionText = GameText(
            message=PokerGameBaseConstants.ENTER_OPTION_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._startText = GameText(message=PokerGameBaseConstants.START_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._checkText = GameText(message=PokerGameBaseConstants.CHECK_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)


        # Position GameText Objects
        self._titleText.centerOnScreen(self._width, self._height, 'top_center')
        self._playerText.centerOnScreen(
            self._width, self._height, 'bottom_left')
        self._aiText.centerOnScreen(self._width, self._height, 'bottom_right')
        self._playOptionText.centerOnScreen(
            self._width, self._height, 'bottom_center')
        self._playOptionText.move(
            0, -CardSprite.YOFFSET // 2 + (-CardSprite.XOFFSET // 2))
        self._pot.centerOnScreen(self._width, self._height, 'bottom_center')
        self._raiseInputText.centerOnScreen(self._width, self._height, 'top_center')
        self._raiseInputText.move(
            0, CardSprite.YOFFSET
        )
        self._enterOptionText.centerOnScreen(
            self._width, self._height, 'top_center')
        self._enterOptionText.move(
            0, CardSprite.YOFFSET + CardSprite.YOFFSET // 2
        )
        self._startText.centerOnScreen(self._width,self._height,'center')
        self._startText.move(
            0, CardSprite.YOFFSET
        )
        self._checkText.centerOnScreen(self._width,self._height,'center')
        self._checkText.move(
            0, CardSprite.YOFFSET
        )

        # Game Status
        self._gameOver = False
        self._raiseStatus = False

        # Game Options
        self._check = False
        self._raise = False
        self._fold = False
        self._playerWin = False
        self._tie = False

        # Constructs A DeckSprite Object with a total of 52 shuffled CardSprites in it
        self._deck = DeckSprite()
        self._deck.shuffle()

        # Constructs board, boardScorer, player, playerScorer, ai, aiScorer, and gives them the correct number of cards
        #
        self._board = CardHandSprite()
        self._boardScore = HandScorer()
        self._player = CardHandSprite()
        self._playerScore = HandScorer()
        self._ai = CardHandSprite()
        self._aiScore = HandScorer()
        self.dealAllHands()

        # Position CardHandSprite objects
        self._board.centerOnScreen(self._width, self._height)
        self._player.centerOnScreen(self._width, self._height, 'bottom_left')
        self._player.move(0, -CardSprite.YOFFSET / 2)
        self._ai.centerOnScreen(self._width, self._height, 'bottom_right')
        self._ai.move(0, -CardSprite.YOFFSET / 2)

        self.flipCardsInHand(self._ai)
        self.initGame()

    def dealAllHands(self):
        self.dealCards(
            PokerGameBaseConstants.NUM_OF_CARDS_IN_BOARD, self._board)
        self.dealCards(
            PokerGameBaseConstants.NUM_OF_CARDS_IN_HAND, self._player)
        self.dealCards(PokerGameBaseConstants.NUM_OF_CARDS_IN_HAND, self._ai)

    def dealCards(self, numCards, hand):
        for i in range(numCards):
            hand.addCard(self._deck)

    def flipCardsInHand(self, hand):
        for i in range(len(hand.getHand())):
            hand.getHand()[i] = hand.getHand()[i].flipCard()

    def initGame(self):
        self._pot = Pot(amount=PokerGameBaseConstants.MINIMUM_WAGE * 2)
        self._pot.centerOnScreen(self._width,self._height,'bottom_center')
        self.theFlop()

    def theFlop(self):
        self._board.getHand()[3] = self._board.getHand()[3].flipCard()
        self._board.getHand()[4] = self._board.getHand()[4].flipCard()
        for i in range(3):
            self._board.increaseNumFaceUp()

    def theTurn(self):
        self._board.getHand()[3] = self._board.getHand()[3].flipCard()
        self._board.increaseNumFaceUp()

    def theRiver(self):
        self._board.getHand()[4] = self._board.getHand()[4].flipCard()
        self._board.increaseNumFaceUp()

    def nextTurn(self):
        if self._board.getNumFaceUp() == 3:
            self.theTurn()
        elif self._board.getNumFaceUp() == 4:
            self.theRiver()

    def check(self):
        self._fold = self._raise = self._check = False
        if self._board.getNumFaceUp() == 5:
            self._gameOver = True
            self.flipCardsInHand(self._ai)
        else:
            self.nextTurn()
        self._check = True

    def fold(self):
        self._fold = self._raise = self._check = False
        self._gameOver = True
        self._fold = True
        if self._board.getNumFaceUp() == 3:
            self.theTurn()
            self.theRiver()
        elif self._board.getNumFaceUp() == 4:
            self.theRiver()
        self.flipCardsInHand(self._ai)

    def raiseBet(self):
        self._fold = self._raise = self._check = False
        self._raiseStatus = True

    def run(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                   
            self._titleText.draw(self._screen)
            self._playerText.draw(self._screen)
            self._aiText.draw(self._screen)
            self._playOptionText.draw(self._screen)
            self._pot.draw(self._screen)
            self._raiseInputText.draw(self._screen)
            self._enterOptionText.draw(self._screen)
            self._board.draw(self._screen)
            self._player.draw(self._screen)
            self._ai.draw(self._screen)
            pygame.display.flip()

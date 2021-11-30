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
    # Constructs a PokerGameBase object
    # - Screen (width, height, background, background color)
    # - GameText
    #   (titleText, playerText, aiText, playOptionText, pot, raiseInputText, enterOptionText, etc)
    # - GameText positioning
    # - GameStatus
    # - GameOptions (check, raise, fold, playerWin, tie)
    # - Deck
    # - CardHands (board, player, ai) and positioning
    # - Flip Ai's cards
    #
    def __init__(self, width=PokerGameBaseConstants.SCREEN_WIDTH, height=PokerGameBaseConstants.SCREEN_HEIGHT, caption=PokerGameBaseConstants.SCREEN_CAPTION, backgroundColor=PokerGameBaseConstants.TABLE_RGB):
        pygame.init()
        self._width = width
        self._height = height
        self._raiseInput = ''

        # Game Screen
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(caption)

        # Fill the background color to the screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background = self._background.convert()
        self._background.fill(backgroundColor)

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
        self._startText = GameText(
            message=PokerGameBaseConstants.START_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._checkText = GameText(
            message=PokerGameBaseConstants.CHECK_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._raiseText = GameText(
            message=PokerGameBaseConstants.RAISE_TEXT, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._foldText = GameText(message=PokerGameBaseConstants.FOLD_TEXT,
                                  fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._winText = GameText(message=PokerGameBaseConstants.WIN_TEXT,
                                 fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._lostText = GameText(message=PokerGameBaseConstants.LOST_TEXT,
                                  fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
        self._tieText = GameText(message=PokerGameBaseConstants.TIE_TEXT,
                                 fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)

        # Positions all of the GameText objects above
        self.positionGameText()

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

        # Flips the ai's hand so that the player does not have an advantage
        self.flipCardsInHand(self._ai)

        # Sets the Pot amount to double the minimum to start and then proceeds with the Flop
        self.initGame()

    # Positions all of the GameText objects in the game.
    #
    def positionGameText(self):
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
        self._raiseInputText.centerOnScreen(
            self._width, self._height, 'top_center')
        self._raiseInputText.move(
            0, CardSprite.YOFFSET
        )
        self._enterOptionText.centerOnScreen(
            self._width, self._height, 'top_center')
        self._enterOptionText.move(
            0, CardSprite.YOFFSET + CardSprite.YOFFSET // 2
        )
        self._startText.centerOnScreen(self._width, self._height, 'center')
        self._startText.move(
            0, CardSprite.YOFFSET
        )
        self._checkText.centerOnScreen(self._width, self._height, 'center')
        self._checkText.move(
            0, CardSprite.YOFFSET
        )
        self._raiseText.centerOnScreen(self._width, self._height, 'center')
        self._raiseText.move(
            0, CardSprite.YOFFSET
        )
        self._foldText.centerOnScreen(self._width, self._height, 'center')
        self._foldText.move(
            0, CardSprite.YOFFSET
        )
        self._winText.centerOnScreen(self._width, self._height, 'center')
        self._winText.move(
            0, CardSprite.YOFFSET
        )
        self._lostText.centerOnScreen(self._width, self._height, 'center')
        self._lostText.move(
            0, CardSprite.YOFFSET
        )
        self._tieText.centerOnScreen(self._width, self._height, 'center')
        self._tieText.move(
            0, CardSprite.YOFFSET
        )

    # Deals cards from self._deck into the hand that is passed into the method.
    #  @param numCards (int) the number of cards that you want dealed to the hand
    #  @param hand (CardHandSprite) the hand that you are giving cards
    #
    def dealCards(self, numCards, hand):
        for i in range(numCards):
            hand.addCard(self._deck)

    # Deals cards into the board, player, and ai. The number of cards dealed is determined by PokerGameBaseConstants.py
    #
    def dealAllHands(self):
        self.dealCards(
            PokerGameBaseConstants.NUM_OF_CARDS_IN_BOARD, self._board)
        self.dealCards(
            PokerGameBaseConstants.NUM_OF_CARDS_IN_HAND, self._player)
        self.dealCards(PokerGameBaseConstants.NUM_OF_CARDS_IN_HAND, self._ai)

    # Reveals all the cards in a hand.
    #  @param hand (CardHandSprite) the hand that you are flipping
    #
    def flipCardsInHand(self, hand):
        for i in range(len(hand.getHand())):
            hand.getHand()[i] = hand.getHand()[i].flipCard()

    # Starts the game with Pot amount of double the minimum wage and the Flop.
    #
    def initGame(self):
        self._pot = Pot(amount=PokerGameBaseConstants.MINIMUM_WAGE * 2)
        self._pot.centerOnScreen(self._width, self._height, 'bottom_center')
        self.theFlop()

    # The Flop: the first round in the game.
    #  Only the first three cards are revealed to the player.
    #
    def theFlop(self):
        # Hides that back two cards in the hand
        self._board.getHand()[3] = self._board.getHand()[3].flipCard()
        self._board.getHand()[4] = self._board.getHand()[4].flipCard()
        # Increase the number of cards that are face up, so you can keep track of when it is gameover
        for i in range(3):
            self._board.increaseNumFaceUp()

    # The Turn: the second round in the game.
    #  The fourth card is now revealed to the player.
    #
    def theTurn(self):
        self._board.getHand()[3] = self._board.getHand()[3].flipCard()
        self._board.increaseNumFaceUp()  # keep track of gameover

    # The River: the third round in the game.
    #  The fifth and final card is now revealed to the player.
    #
    def theRiver(self):
        self._board.getHand()[4] = self._board.getHand()[4].flipCard()
        self._board.increaseNumFaceUp()  # keep track of gameover

    # Determines what round of the game should be called based on the number of face up cards in the board.
    #
    def nextTurn(self):
        if self._board.getNumFaceUp() == 3:
            self.theTurn()  # the Turn
        elif self._board.getNumFaceUp() == 4:
            self.theRiver()  # the River

    # Check: Pass your turn
    #
    def check(self):
        # Set all game options to false to start
        self._fold = self._raise = self._check = False
        if self._board.getNumFaceUp() == 5:
            self._gameOver = True
            self.flipCardsInHand(self._ai)  # Flips the ai's cards face up
        else:
            self.nextTurn()
        self._check = True

    # Fold: Give up the game
    #
    def fold(self):
        # Set all game options to false to start
        self._fold = self._raise = self._check = False

        # Fold means GAMEOVER!
        self._gameOver = True
        self._fold = True

        # Flip the remaining cards from the Turn and the River
        if self._board.getNumFaceUp() == 3:
            self.theTurn()
            self.theRiver()
        elif self._board.getNumFaceUp() == 4:
            self.theRiver()

        # Reveal the ai cards
        self.flipCardsInHand(self._ai)

    # Raise: Add an amount to the Pot during one's turn.
    #
    def raiseBet(self):
        # Set all game options to false to start
        self._fold = self._raise = self._check = False
        self._raiseStatus = True

    # Draws all the text and hands (board, player, ai) that are constantly on the board.
    #
    def draw(self):
        self._titleText.draw(self._screen)
        self._playerText.draw(self._screen)
        self._aiText.draw(self._screen)
        self._playOptionText.draw(self._screen)
        self._pot.draw(self._screen)
        self._board.draw(self._screen)
        self._player.draw(self._screen)
        self._ai.draw(self._screen)

    # Takes care of all the event handling needed in the Poker Game
    #
    def run(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                # Stops game!
                if event.type == QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    # ESCAPE Key Pressed - Stops game!
                    if event.key == pygame.K_ESCAPE:
                        return

                    # BACKSPACE Key Pressed
                    if event.key == pygame.K_BACKSPACE:
                        # [:-1] slices the string to omit the last character
                        self._raiseInput = self._raiseInput[:-1]

                    # Adds characters to the _raiseInput
                    if self._raiseStatus and 10 > event.key - ord('0') >= 0:
                        self._raiseInput += str(event.key - ord('0'))

                    # Raise is True and RETURN/ENTER Key Pressed
                    elif self._raiseStatus and event.key == pygame.K_RETURN:
                        self._raise = True
                        self._raiseStatus = False
                        temp = self._pot.getPotAmount()

                        # Takes the original pot amount and then adds 2x _raiseInput
                        # b/c every time the player raises so does the ai
                        self._pot = Pot(int(self._raiseInput) * 2 + temp)
                        self._pot.centerOnScreen(
                            self._width, self._height, 'bottom_center')
                        if self._board.getNumFaceUp() == 5:
                            self._gameOver = True
                            self.flipCardsInHand(self._ai)
                        else:
                            self.nextTurn()
                        self._raiseInput = ''  # Reset the raiseInput string
                    if not self._gameOver:
                        # C Key Pressed
                        if event.key == pygame.K_c:
                            self.check()

                        # R Key Pressed
                        if event.key == pygame.K_r:
                            self.raiseBet()

                        # F Key Pressed
                        if event.key == pygame.K_f:
                            self.fold()
                    else:
                        # R Key Pressed
                        if event.key == pygame.K_r:
                            self.__init__()

            # Updates the screen so that the different GameText objects do NOT overlap one another
            self._screen.blit(self._background, (0, 0))

            # Determines what Text should be drawn during the game
            if self._check and not self._gameOver:
                self._checkText.draw(self._screen)  # check & not gameover
            elif self._raise and not self._gameOver:
                self._raiseText.draw(self._screen)  # raise & not gameover
            elif self._raiseStatus and not self._gameOver:
                self._raiseInputText = GameText(
                    message='Enter Raise Amount: $' + self._raiseInput, fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
                self._raiseInputText.centerOnScreen(
                    self._width, self._height, 'top_center')
                self._raiseInputText.move(
                    0, CardSprite.YOFFSET
                )
                # prompts the player to press Enter once done inputting raise amount
                self._enterOptionText.draw(self._screen)
                self._raiseInputText.draw(self._screen)

            elif self._fold and not self._gameOver:
                self._foldText.draw(self._screen)  # fold & not gameover

            elif not self._gameOver:
                # start of the game & not gameover
                self._startText.draw(self._screen)

            # Draws the final winner and the corresponding text message
            if self._gameOver and self._playerWin:
                self._winText.draw(self._screen)
            elif self._gameOver and not self._playerWin and not self._tie:
                self._lostText.draw(self._screen)
            elif self._gameOver and self._tie:
                self._tieText.draw(self._screen)

            ## Determines who will win between the player and ai depending on the score given by there HandScorer object.
            #  - if they have the same CardHand score then the winner is determined by the highest card in their hand.
            if self._gameOver:
                # print(str(self._playerScore.getScore(self._board, self._player)
                #           ) + ' ' + str(self._aiScore.getScore(self._board, self._ai)))
                if self._playerScore.getScore(self._board, self._player) > self._aiScore.getScore(self._board, self._ai):
                    self._playerWin = True
                elif self._playerScore.getScore(self._board, self._player) == self._aiScore.getScore(self._board, self._ai):
                    if self._playerScore.getScore(self._board, self._player) == self._aiScore.getScore(self._board, self._ai) and self._aiScore.getScore(self._board, self._ai) != 1:
                        self._tie = True
                    elif self._playerScore.getScore(self._board, self._player) == 1:
                        if self._playerScore.highCard(self._board, self._player) > self._aiScore.highCard(self._board, self._ai):
                            self._playerWin = True
                        elif self._playerScore.highCard(self._board, self._player) == self._aiScore.highCard(self._board, self._ai):
                            self._tie = True
                        else:
                            self._playerWin = False
            
            # Draws all the text and hands (board, player, ai) that are constantly on the board.
            self.draw()
            # Updates the screen.
            pygame.display.flip()

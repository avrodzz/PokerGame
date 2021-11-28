# Alexis Rodriguez
# Poker Game
# Last Changed: November 27, 2021


import pygame
from CardSprite import CardSprite
from DeckSprite import DeckSprite
from CardHandSprite import CardHandSprite
from GameText import GameText
from Pot import Pot
from PokerGameBaseConstants import PokerGameBaseConstants


def main():
    pygame.font.init()

    # Define the dimensions of
    # screen object(width,height)
    screen = pygame.display.set_mode(
        (PokerGameBaseConstants.SCREEN_WIDTH, PokerGameBaseConstants.SCREEN_HEIGHT))

    # Set the caption of the screen
    pygame.display.set_caption('Poker Game')

    # Fill the background colour to the screen
    screen.fill(PokerGameBaseConstants.TABLE_RGB)

    # Variable to keep our game loop running
    running = True

    hand = CardHandSprite()

    # aceOfHearts = CardSprite('Ace', 'Hearts')
    deck = DeckSprite()
    deck.shuffle()

    for i in range(PokerGameBaseConstants.NUM_OF_CARDS_IN_BOARD):
        hand.addCard(deck)

    hand.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                        PokerGameBaseConstants.SCREEN_HEIGHT)

    text = GameText(message=PokerGameBaseConstants.TITLE_TEXT,
                    fontSize=PokerGameBaseConstants.TITLE_FONT_SIZE)

    text.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                        PokerGameBaseConstants.SCREEN_HEIGHT, 'top_center')

    playerText = GameText(
        message='PLAYER', fontSize=PokerGameBaseConstants.PLAYER_FONT_SIZE)
    playerText.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                              PokerGameBaseConstants.SCREEN_HEIGHT, 'bottom_left')

    playerHand = CardHandSprite()
    for i in range(PokerGameBaseConstants.NUM_OF_CARDS_IN_HAND):
        playerHand.addCard(deck)

    playerHand.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                              PokerGameBaseConstants.SCREEN_HEIGHT, 'bottom_left')
    playerHand.move(0, -CardSprite.YOFFSET / 2)

    aiText = GameText(
        message='AI', fontSize=PokerGameBaseConstants.PLAYER_FONT_SIZE)
    aiText.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                          PokerGameBaseConstants.SCREEN_HEIGHT, 'bottom_right')

    aiHand = CardHandSprite()
    for i in range(PokerGameBaseConstants.NUM_OF_CARDS_IN_HAND):
        aiHand.addCard(deck)

    aiHand.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                          PokerGameBaseConstants.SCREEN_HEIGHT, 'bottom_right')
    aiHand.move(0, -CardSprite.YOFFSET / 2)

    pot = Pot(amount=PokerGameBaseConstants.MINIMUM_WAGE)
    pot.centerOnScreen(PokerGameBaseConstants.SCREEN_WIDTH,
                       PokerGameBaseConstants.SCREEN_HEIGHT, 'bottom_center')

    playOptionText = GameText(
        message='[C]heck [R]aise [F]old', fontSize=PokerGameBaseConstants.GENERAL_FONT_SIZE)
    playOptionText.centerOnScreen(
        PokerGameBaseConstants.SCREEN_WIDTH, PokerGameBaseConstants.SCREEN_HEIGHT, 'bottom_center')
    playOptionText.move(0, -CardSprite.YOFFSET // 2 +
                        (-CardSprite.XOFFSET // 2))

    # game loop
    while running:

        # for loop through the event queue
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

        # aceOfHearts.draw(screen)
        # deck.draw(screen)
        hand.draw(screen)
        playerHand.draw(screen)
        aiHand.draw(screen)

        # for i in range(hand.getNumOfCards()):
        #     # print(tempX[i].getRect().x + CardSprite.XOFFSET / 2)
        #     pygame.draw.line(screen, Color_line,
        #                      (tempX[i].getRect().x + CardSprite.XOFFSET / 2, 0), (tempX[i].getRect().x + CardSprite.XOFFSET / 2, SCREEN_HEIGHT))

        # CENTER VERTICAL LINE (NEON GREEN)
        # pygame.draw.line(screen, (57, 255, 20), (PokerGameBaseConstants.SCREEN_WIDTH /
        #                  2, 0), (PokerGameBaseConstants.SCREEN_WIDTH/2, PokerGameBaseConstants.SCREEN_HEIGHT))

        # CENTER HORIZONTAL LINE (NEON GREEN)
        # pygame.draw.line(screen, (57, 255, 20),
        #                  (0, PokerGameBaseConstants.SCREEN_HEIGHT/2), (PokerGameBaseConstants.SCREEN_WIDTH, PokerGameBaseConstants.SCREEN_HEIGHT/2))

        text.draw(screen)
        playerText.draw(screen)
        aiText.draw(screen)
        pot.draw(screen)
        playOptionText.draw(screen)

        # Update the display using flip
        pygame.display.flip()


if __name__ == '__main__':
    main()

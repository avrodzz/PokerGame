# Alexis Rodriguez
# Poker Game
# Last Changed: November 17, 2021


from Card import Card
from CardSprite import CardSprite
from DeckSprite import DeckSprite
from CardHandSprite import CardHandSprite
import pygame


def main():
    # Define the background colour
    # using RGB color coding.
    background_color = (255, 166, 43)

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    # Define the dimensions of
    # screen object(width,height)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the caption of the screen
    pygame.display.set_caption('Poker Game')

    # Fill the background colour to the screen
    screen.fill(background_color)

    # Variable to keep our game loop running
    running = True

    hand = CardHandSprite()

    # aceOfHearts = CardSprite('Ace', 'Hearts')
    deck = DeckSprite()
    deck.shuffle()

    for i in range(5):
        hand.addCard(deck)

    hand.centerOnScreen(SCREEN_WIDTH, SCREEN_HEIGHT)

    Color_line = (255, 0, 0)

    tempX = hand.getHand()

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
        # for i in range(hand.getNumOfCards()):
        #     # print(tempX[i].getRect().x + CardSprite.XOFFSET / 2)
        #     pygame.draw.line(screen, Color_line,
        #                      (tempX[i].getRect().x + CardSprite.XOFFSET / 2, 0), (tempX[i].getRect().x + CardSprite.XOFFSET / 2, SCREEN_HEIGHT))

        # CENTER VERTICAL LINE (NEON GREEN)
        # pygame.draw.line(screen, (57, 255, 20), (SCREEN_WIDTH/2,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

        # CENTER HORIZONTAL LINE (NEON GREEN)
        # pygame.draw.line(screen, (57, 255, 20), (0, SCREEN_HEIGHT/2), (SCREEN_WIDTH, SCREEN_HEIGHT/2))

        # Update the display using flip
        pygame.display.flip()


if __name__ == '__main__':
    main()

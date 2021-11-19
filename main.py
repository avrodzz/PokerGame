# Alexis Rodriguez
# Poker Game
# Last Changed: November 17, 2021

from pygame.constants import RESIZABLE
# from CardSprite import CardSprite
from DeckSprite import DeckSprite
import pygame


def main():
    # Define the background colour
    # using RGB color coding.
    background_color = (255, 166, 43)

    # Define the dimensions of
    # screen object(width,height)
    screen = pygame.display.set_mode((975, 396))

    # Set the caption of the screen
    pygame.display.set_caption('Poker Game')

    # Fill the background colour to the screen
    screen.fill(background_color)

    # Variable to keep our game loop running
    running = True

    # aceOfHearts = CardSprite('Ace', 'Hearts')
    deck = DeckSprite()
    deck.shuffle()
 
    # game loop
    while running:

        # for loop through the event queue
        for event in pygame.event.get():

            # Check for QUIT event
            if event.type == pygame.QUIT:
                running = False

        # aceOfHearts.draw(screen)
        deck.draw(screen)

        # Update the display using flip
        pygame.display.flip()


if __name__ == '__main__':
    main()

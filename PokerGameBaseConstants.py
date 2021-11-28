# PokerGameBaseConstants is to avoid hard coding values within the game.


class PokerGameBaseConstants:
    # SCREEN CONSTANTS
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 700

    # POKER HANDS CONSTANTS
    NUM_OF_CARDS_IN_BOARD = 5
    NUM_OF_CARDS_IN_HAND = 2

    # COLORS
    TABLE_RGB = 255, 162, 0
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0

    # TITLE TEXT
    TITLE_TEXT = 'TEXAS HOLD\'EM'

    # POT MINIMUM BET
    MINIMUM_WAGE = 20

    # POT MESSAGE
    POT_MESSAGE = 'Pot: $'

    # FONT SIZES
    TITLE_FONT_SIZE = 75
    PLAYER_FONT_SIZE = (TITLE_FONT_SIZE * 2) // 3
    GENERAL_FONT_SIZE = TITLE_FONT_SIZE // 2

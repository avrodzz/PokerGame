# PokerGameBaseConstants is to avoid hard coding values within the game.


class PokerGameBaseConstants:
    # SCREEN CONSTANTS
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 600
    SCREEN_CAPTION = 'Poker Game!'

    # POKER HANDS CONSTANTS
    NUM_OF_CARDS_IN_BOARD = 5
    NUM_OF_CARDS_IN_HAND = 2

    # COLORS
    TABLE_RGB = 71,132,122
    WHITE = 255, 255, 255
    BLACK = 0, 0, 0

    # TEXT
    TITLE_TEXT = 'TEXAS HOLD\'EM'
    PLAYER_TEXT = 'PLAYER'
    AI_TEXT = 'AI'
    PLAY_OPTION_TEXT = '[C]heck [R]aise [F]old'
    START_TEXT = 'The game started and both players added to the pot!'
    CHECK_TEXT = 'The player just checked and the AI did too!'
    RAISE_TEXT = 'The player just raised and the AI added the same amount!'
    FOLD_TEXT = 'GAME OVER! The player folded! [R]estart!'
    WIN_TEXT = 'The player won and took the pot! [R]estart!'
    LOST_TEXT = 'The player lost and the AI took the pot! [R]estart!'
    TIE_TEXT = 'The player and the AI tied and split the pot! [R]estart!'
    RAISE_INPUT_TEXT = 'Enter Raise Amount: $'
    ENTER_OPTION_TEXT = 'Press Enter When Done'
 
    # POT MINIMUM BET
    MINIMUM_WAGE = 20

    # POT MESSAGE
    POT_MESSAGE = 'Pot: $'

    # FONT SIZES
    TITLE_FONT_SIZE = 60
    PLAYER_FONT_SIZE = (TITLE_FONT_SIZE * 2) // 3
    GENERAL_FONT_SIZE = TITLE_FONT_SIZE // 2

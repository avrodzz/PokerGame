import pygame

# A GameText is a text with a message, font size, font color, and position.


class GameText:

    # Constructs a GameText with a blank message, 12pt font size, black font color, and positioned at (0,0).
    #
    def __init__(self, message='', fontSize=12, fontColor=(0, 0, 0),
                 x=0, y=0):
        self._message = message
        self._font = pygame.font.Font(None, fontSize)
        self._gameText = self._font.render(self._message, False, fontColor)
        self._gameTextRect = self._gameText.get_rect()
        self._gameTextRect.x = x
        self._gameTextRect.y = y

    ## Accessor (Getter)
    #  @return self._gameTextRect (Rect) the x- and y- coordinates of the text
    #
    def getRect(self):
        return self._gameTextRect

    # Sets the x and y position of the top left corner of the text
    #  @param x (float) the x-coordinate position
    #  @param y (float) the y-coordniate position
    #
    def setPosition(self, x, y):
        self._gameTextRect.x = x
        self._gameTextRect.y = y

    # Moves the GameText object by an offset of x and y
    #  @param x (float) the x offset
    #  @param y (float) the y offset
    #
    def move(self, x, y):
        self._gameTextRect.x += x
        self._gameTextRect.y += y

    # Set position of text to the center of the screen by default
    #  Other options include 'top_left', 'left_center', 'bottom_left'
    #                        'top_center', 'center', 'bottom_center',
    #                        'top_right', 'right_center', 'bottom_right'
    #  @param screenWidth (float) the width of the screen
    #  @param screenHeight (float) the height of the screen
    #  @param location (string) the desired location of the text
    #
    def centerOnScreen(self, screenWidth, screenHeight, location='center'):
        center_x_pos = screenWidth / 2 - (self._gameTextRect.size[0] / 2)
        center_y_pos = screenHeight / 2 - (self._gameTextRect.size[1] / 2)
        bottom_y_pos = screenHeight - self._gameTextRect.size[1]
        right_x_pos = screenWidth - self._gameTextRect.size[0]
        if location == 'top_left':
            self.setPosition(
                0, 0
            )
        elif location == 'left_center':
            self.setPosition(
                0, center_y_pos
            )
        elif location == 'bottom_left':
            self.setPosition(
                0, bottom_y_pos
            )
        elif location == 'top_center':
            self.setPosition(
                center_x_pos, 0
            )
        elif location == 'center':
            self.setPosition(
                center_x_pos, center_y_pos)
        elif location == 'bottom_center':
            self.setPosition(
                center_x_pos, bottom_y_pos
            )
        elif location == 'top_right':
            self.setPosition(
                right_x_pos, 0
            )
        elif location == 'right_center':
            self.setPosition(
                right_x_pos, center_y_pos
            )
        elif location == 'bottom_right':
            self.setPosition(
                right_x_pos, bottom_y_pos
            )

    # Draws the text to the screen.
    #  @param screen (pygame Surface) the window where the content is being displayed
    #
    def draw(self, screen):
        screen.blit(self._gameText, self._gameTextRect)

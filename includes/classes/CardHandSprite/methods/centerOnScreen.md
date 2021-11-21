<!-- Method Name -->

# <code>centerOnScreen(self,screenWidth,screenHeight)</code>

<!-- Method Description -->
> Set position of all cards in hand to the center of the screen.

<!-- Parameters -->
###### Parameters
| Name           | Data Type | Description                                                                                                                    |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `self`         |           |                                                                                                                                |
| `screenWidth`  | float     | the width of the screen                                                                                                        |
| `screenHeight` | float     | the height of the screen                                                                                                       |
| `location`     | string    | 'top_left', 'left_center', 'bottom_left', 'top_center', 'center', 'bottom_center', 'top_right', 'right_center', 'bottom_right' |

<!-- Return Type -->
###### Return Type
`void`

<!-- Method Example -->
###### Usage
```python
# Constructs CardHandSprite object
hand = CardHandSprite()

# Constructs a DeckSprite object with 52 cards
deck = DeckSprite()

# Shuffles the deck of cards
deck.shuffle()

# Adds five cards to the CardHandSprite object
for i in range(5):
    hand.addCard(deck)

# Changes the position of the cards so that they appear in the center of the screen
hand.centerOnScreen(SCREEN_WIDTH, SCREEN_HEIGHT)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../CardHandSprite.md)
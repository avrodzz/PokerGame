<!-- Method Name -->

# <code>_checkHand(self,board,hand)</code>

<!-- Method Description -->
> Determines the score of the hand including the possible score options with the board cards.

<!-- Parameters -->
###### Parameters
| Name    | Data Type      | Description            |
| ------- | -------------- | ---------------------- |
| `self`  |                |                        |
| `board` | CardHandSprite | the cards in the board |
| `hand`  | CardHandSprite | the cards in the hand  |

<!-- Return Type -->
###### Return Type
`int`

<!-- Method Example -->
###### Usage
```python
# Private class method
# _checkHand returns the highest score that the hand and board can produce
def getScore(self, board, hand):
    return self._checkHand(board, hand)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../HandScorer.md)
<!-- Method Name -->

# <code>getScore(self,board,hand)</code>

<!-- Method Description -->
> Accessor (Getter): Gets the score of the hand.

<!-- Parameters -->
###### Parameters
| Name   | Data Type | Description |
| ------ | --------- | ----------- |
| `self` |           |             |
| `board` | CardHandSprite | the cards in the board |
| `hand` | CardHandSprite | the cards in the hand |

<!-- Return Type -->
###### Return Type
`int`

<!-- Method Example -->
###### Usage
```python
# Constructs HandScorer object
handscorer = HandScorer() 

# Retrieves a score of 1-10
score = handscorer.getScore(board,hand)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../HandScorer.md)
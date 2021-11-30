<!-- Method Name -->

# <code>dealCards(self,numCards,hand)</code>

<!-- Method Description -->
> Deals cards from deck into the hand that is passed into the method.

<!-- Parameters -->
###### Parameters
| Name       | Data Type      | Description                                    |
| ---------- | -------------- | ---------------------------------------------- |
| `self`     |                |                                                |
| `numCards` | int            | the number of cards you want to deal to a hand |
| `hand`     | CardHandSprite | the hand that is getting dealt cards           |

<!-- Return Type -->
###### Return Type
`void`

<!-- Method Example -->
###### Usage
```python
# Constructs PokerGameBase object
game = PokerGameBase()

# Constructs CardHandSprite object
hand = CardHandSprite()

# Call to dealCards
game.dealCards(hand)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../PokerGameBase.md)
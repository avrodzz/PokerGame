<!-- Method Name -->

# <code>addCard(self,deck)</code>

<!-- Method Description -->
> Adds a CardSprite object to the CardSprite list (self._hand).

<!-- Parameters -->
###### Parameters
| Name   | Data Type  | Description       |
| ------ | ---------- | ----------------- |
| `self` |            |                   |
| `deck` | DeckSprite | the deck of cards |

<!-- Return Type -->
###### Return Type
`void`

<!-- Method Example -->
###### Usage
```python
hand = CardHandSprite()
deck = DeckSprite()
deck.shuffle()
for i in range(5):
    hand.addCard(deck)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../CardHandSprite.md)
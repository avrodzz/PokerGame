<!--Name Of Class -->

# DeckSprite

<!-- Description -->

>A DeckSprite contains 52 CardSprites.

<!-- Screenshots -->
###### Screenshots
<!-- ![CardSprite](../../images/cardSprite.png) -->

<img src="../../images/deckSprite_in_order.png" alt="DeckSprite_In_Order" width="500"/>

<img src="../../images/deckSprite_shuffled.png" alt="DeckSprite_Shuffled" width="500"/>

<!-- Imports -->
###### Imports
```python
from CardSprite import CardSprite
from random import shuffle
```

<!-- Usage -->

###### Usage

```python
# Contructs the deck of 52 cards
deck = DeckSprite()
# Shuffles the deck
deck.shuffle()
```

<!-- Instance Variables -->
###### Instance Variables
| Name          | Data Type    | Description         |
| ------------- | ------------ | ------------------- |
| `_deckSprite` | CardSprite[] | list of CardSprites |


###### Methods

<ul>

<!-- (Add Member Functions Here) -->
<!-- [`nameOfFunction(parameters)`](functions/nameOfFunction.md) -->
<!-- Make sure to create a .md file in the functions folder for EVERY function added -->

[`getDeckSprite(self)`](methods/getDeckSprite.md)

[`initSpriteDeck(self)`](methods/initSpriteDeck.md)

[`shuffle(self)`](methods/shuffle.md)

[`dealCard(self)`](methods/dealCard.md)

[`draw(self,screen)`](methods/draw.md)


</ul>

---

<!-- Back to README.md -->
[back](../../../README.md)
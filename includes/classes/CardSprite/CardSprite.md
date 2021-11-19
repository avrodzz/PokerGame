<!--Name Of Class -->

# CardSprite

<!-- Description -->

>A CardSprite has all attributes of a Card object and also has pygame sprite qualities.

<!-- Screenshots -->
###### Screenshots
<!-- ![CardSprite](../../images/cardSprite.png) -->

<img src="../../images/cardSprite.png" alt="CardSprite" width="300"/>


<!-- Imports -->
###### Imports
```python
import pygame
from Card import Card
```

<!-- Usage -->

###### Usage

```python
aceOfHearts = CardSprite('Ace', 'Hearts', 0, 0, True)
```

<!-- Instance Variables -->
###### Instance Variables
| Name          | Data Type | Description                                                |
| ------------- | --------- | ---------------------------------------------------------- |
| `_images`     | string[]  | images for the front and back the card                     |
| `_flipped`    | bool      | keeps track of whether the card is flipped or not          |
| `_cardImage`  | Surface   | holds the image that will be loaded into the pygame Sprite |
| `_cardSprite` | Sprite    | the pygame sprite for the CardSprite object                |
| `_rect`       | Rect      | stores rectangular coordinates of the Sprite               |

###### Methods

<ul>

<!-- (Add Member Functions Here) -->
<!-- [`nameOfFunction(parameters)`](functions/nameOfFunction.md) -->
<!-- Make sure to create a .md file in the functions folder for EVERY function added -->

[`getCardSprite(self)`](methods/getCardSprite.md)

[`getRect(self)`](methods/getRect.md)

[`move(self,x,y)`](methods/move.md)

[`setPosition(self,x,y)`](methods/setPosition.md)

[`flipCard(self)`](methods/flipCard.md)

[`draw(self,screen)`](methods/draw.md)


</ul>

---

<!-- Back to README.md -->
[back](../../../README.md)
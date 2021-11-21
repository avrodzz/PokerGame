<!-- Method Name -->

# <code>move(self,x,y)</code>

<!-- Method Description -->
> Moves the CardHandSprite object by an offset of x and y.

<!-- Parameters -->
###### Parameters
| Name   | Data Type | Description            |
| ------ | --------- | ---------------------- |
| `self` |           |                        |
| `x`    | float     | the x-coordinate value |
| `y`    | float     | the y-coordinate value |

<!-- Return Type -->
###### Return Type
`void`

<!-- Method Example -->
###### Usage
```python
hand = CardHandSprite()
# Assuming that there are already cards in your hand and starts a position (0,0) this below would move the position to (50,50)
hand.move(50,50)

# This below would move the position to (51,50)
hand.move(1,0)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../CardHandSprite.md)
<!-- Method Name -->

# <code>move(self,x,y)</code>

<!-- Method Description -->
> Moves the CardSprite object by an offset of x and y.

<!-- Parameters -->
###### Parameters
| Name   | Data Type | Description                         |
| ------ | --------- | ----------------------------------- |
| `self` |           |                                     |
| `x`    | float     | offsets the x-coordinate value by x |
| `y`    | float     | offsets the y-coordniate value by y |

<!-- Return Type -->
###### Return Type
`void`

<!-- Method Example -->
###### Usage
```python
# Position of card starts at (0,0) then moves to (1,3)
card = CardSprite('Ace', 'Hearts', 0, 0)    
card.move(1, 3)
# Position of card moves to (2,3)
card.move(1, 0)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../CardSprite.md)
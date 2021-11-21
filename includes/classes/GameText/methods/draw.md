<!-- Method Name -->

# <code>draw(self,screen)</code>

<!-- Method Description -->
> Draws the text to the screen.

<!-- Parameters -->
###### Parameters
| Name     | Data Type | Description                                     |
| -------- | --------- | ----------------------------------------------- |
| `self`   |           |                                                 |
| `screen` | Surface   | the surface where the content will be displayed |

<!-- Return Type -->
###### Return Type
`void`

<!-- Method Example -->
###### Usage
```python
screen = pygame.display.set_mode((500, 500))
text = GameText(message='Test Message')    
text.draw(screen)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../GameText.md)
<!-- Method Name -->

# <code>centerOnScreen(self,screenWidth,screenHeight,location)</code>

<!-- Method Description -->
> Set position of text to the center of the screen by default.

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
# Constructs GameText object that will be centered on the top
text = GameText(message='TEXAS HOLD\'EM')
text.centerOnScreen(SCREEN_WIDTH, SCREEN_HEIGHT, 'top_center')
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../GameText.md)
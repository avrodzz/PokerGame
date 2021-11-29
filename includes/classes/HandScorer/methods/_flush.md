<!-- Method Name -->

# <code>_flush(self,allcards)</code>

<!-- Method Description -->
> Checks if there is a flush (all of the same suit) in the set of cards.

<!-- Parameters -->
###### Parameters
| Name       | Data Type | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| `self`     |           |                                                    |
| `allCards` | set       | the set of cards that is being checked for a flush |

<!-- Return Type -->
###### Return Type
`bool`

<!-- Method Example -->
###### Usage
```python
# Private class method
# If true then return a score of 6
if self._flush(allCards):
    return 6
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../HandScorer.md)
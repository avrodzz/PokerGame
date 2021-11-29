<!-- Method Name -->

# <code>_royalFlush(self,allcards)</code>

<!-- Method Description -->
> Checks if there is a royal flush (A 10 J Q K and of the same suit) in the set of cards.

<!-- Parameters -->
###### Parameters
| Name       | Data Type | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| `self`     |           |                                                    |
| `allCards` | set       | the set of cards that is being checked for a royal flush |

<!-- Return Type -->
###### Return Type
`bool`

<!-- Method Example -->
###### Usage
```python
# Private class method
# If true then return a score of 10
if self._royalFlush(allCards):
    return 10
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../HandScorer.md)
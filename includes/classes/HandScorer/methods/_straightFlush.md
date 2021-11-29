<!-- Method Name -->

# <code>_straightFlush(self,allcards)</code>

<!-- Method Description -->
> Checks if there is a straight flush (1,2,3,4,5 or 2,3,4,5,6, etc. and all of the same suit) in the set of cards.

<!-- Parameters -->
###### Parameters
| Name       | Data Type | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| `self`     |           |                                                    |
| `allCards` | set       | the set of cards that is being checked for a straight flush |

<!-- Return Type -->
###### Return Type
`bool`

<!-- Method Example -->
###### Usage
```python
# Private class method
# If true then return a score of 9
if self._straightFlush(allCards):
    return 9
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../HandScorer.md)
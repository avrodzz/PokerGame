<!-- Method Name -->

# <code>_checkCardMatches(self,allCards,numMatches)</code>

<!-- Method Description -->
> Determines how many of the same card value are in the set called allCards.

<!-- Parameters -->
###### Parameters
| Name   | Data Type | Description |
| ------ | --------- | ----------- |
| `self` |           |             |
| `allCards` | set | the set of cards that is being checked for matches |
| `numMatches` | int | the number of matches we are checking for |

<!-- Return Type -->
###### Return Type
`bool`

<!-- Method Example -->
###### Usage
```python
# Example: Private class method _pair that is checking for 2 matches of the same card value
def _pair(self, allCards):
    return self._checkCardMatches(allCards, 2)
```
<!-- Back to className.md -->
<!-- The path in this link will be the one that is used for the component -->
[back](../HandScorer.md)
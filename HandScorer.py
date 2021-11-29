# A HandScorer scores a CardHand object.
class HandScorer:

    # Constructs a HandScorer with a score of zero.
    def __init__(self):
        self._score = 0

    ## Accessor (Getter)
    #  @param board (CardHandSprite) the cards in the board
    #  @param hand (CardHandSprite) the cards in the hand
    #  @return self._checkHand(board,hand) (int) the score of the hand
    #
    def getScore(self, board, hand):
        return self._checkHand(board, hand)

    ## Mutator (Setter)
    #  Sets the score back to zero
    #
    def resetScore(self):
        self._score = 0

    # Determines the score of the hand including the possibilities with the board cards
    #  @param board (CardHandSprite) the cards in the board
    #  @param hand (CardHandSprite) the cards in the hand
    #  @return (int) the number corresponding with the score
    #
    def _checkHand(self, board, hand):
        # Sets cannot have repeated items
        allCards = set()

        # Adds all card options from board and hand
        for i in range(len(board.getHand())):
            allCards.add(board.getHand()[i])

        for i in range(len(hand.getHand())):
            allCards.add(hand.getHand()[i])

        # Uses allCards set and class methods to determine the score of the hand
        if self._royalFlush(allCards):
            return 10
        if self._straightFlush(allCards):
            return 9
        if self._fourOfAKind(allCards):
            return 8
        if self._fullHouse(allCards):
            return 7
        if self._flush(allCards):
            return 6
        if self._straight(allCards):
            return 5
        if self._threeOfAKind(allCards):
            return 4
        if self._twoPair(allCards):
            return 3
        if self._pair(allCards):
            return 2
        return 1

    # Determines how many of same card values are in allCards
    #  @param allCards (set) the cards in both the board and hand
    #  @param numMatches (int) the number of duplicates we are searching for
    #  @return (boolean) true or false
    #
    def _checkCardMatches(self, allCards, numMatches):
        # Dictionaries {key, value}
        temp = dict()

        # Adds each card value in the temp dict
        # The value in the key-value pair is how we determine the number of card value multiples
        for card in allCards:
            if card.getValue() in temp:
                temp[card.getValue()] += 1
            else:
                temp[card.getValue()] = 1

        # Checks each key (card value) for the numMatches that is passed in to the method
        for num in temp:
            if temp[num] == numMatches:
                return True
        return False

    # Checks if there is 2 of a kind in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _pair(self, allCards):
        return self._checkCardMatches(allCards, 2)

    # Checks if there is 2 of a kind but TWICE in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _twoPair(self, allCards):
        # Dictionaries {key, value}
        # Ex: {'Ace': 1, 'Three': 2 ...}
        temp = dict()

        # Adds each card value in the temp dict
        # The value in the key-value pair is how we determine the number of card value multiples
        for card in allCards:
            if card.getValue() in temp:
                temp[card.getValue()] += 1
            else:
                temp[card.getValue()] = 1

        # Now checking for the value of 2 in the dictionary
        # This would mean that we have a pair with the same card values
        # Adds 1 if this is the case
        numOfPairs = 0
        for num in temp:
            if temp[num] == 2:
                numOfPairs += 1

        # Checks if the card set is a two pair or not based on the variable numOfPairs
        if numOfPairs == 2:
            return True
        return False

    # Checks if there is 3 of a kind in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _threeOfAKind(self, allCards):
        return self._checkCardMatches(allCards, 3)

    # Checks if there is a straight in the set of cards
    #  1,2,3,4,5 or 2,3,4,5,6 or 3,4,5,6,7 ... etc as well as 10,11,12,13,1 for royal flush purposes
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _straight(self, allCards):
        # Dictionaries {key, value}
        # Ex: {1: 1, 2: 0, 3: 1 ...}
        temp = dict()

        # Adds each card numeric value in the temp dict
        # The int value in the key-value pair is how we determine the straight
        for card in allCards:
            if card.getNumericValue() in temp:
                temp[card.getNumericValue()] += 1
            else:
                temp[card.getNumericValue()] = 1

        # Royal flush straight case
        if 1 in temp and 13 in temp and 12 in temp and 11 in temp and 10 in temp:
            return True

        # For loop where i goes from 1 to 9
        # Checks the remaining straight cases
        for i in range(1, 10):
            if i in temp and i + 1 in temp and i + 2 in temp and i + 3 in temp and i + 4 in temp:
                return True
        return False

    # Checks if there is 4 of a kind in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _fourOfAKind(self, allCards):
        return self._checkCardMatches(allCards, 4)

    # Checks if there is a flush in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _flush(self, allCards):
        # Dictionaries {key, value}
        # Ex: {'Clubs': 5, 'Diamonds': 0, 'Hearts': 0, 'Spades': 0}
        temp = dict()

        # Adds each card's suit value in the temp dict
        # The suit value in the key-value pair is how we determine the flush
        for card in allCards:
            if card.getSuit() in temp:
                temp[card.getSuit()] += 1
            else:
                temp[card.getSuit()] = 1
        # temp.values is a list of the dictionaries values NOT including the keys
        return 5 in temp.values()

    # Checks if there is a full house in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _fullHouse(self, allCards):
        # Dictionaries {key, value}
        # Ex: {12: 2, 7: 3}
        temp = dict()

        # Adds each card numeric value in the temp dict
        # The int value in the key-value pair is how we determine the full house
        for card in allCards:
            if card.getNumericValue() in temp:
                temp[card.getNumericValue()] += 1
            else:
                temp[card.getNumericValue()] = 1

        # Needs a pair and three of a kind
        return 2 in temp.values() and 3 in temp.values()

    # Checks if there is a straight flush in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _straightFlush(self, allCards):
        return self._straight(allCards) and self._flush(allCards)

    # Checks if there is a royal flush in the set of cards
    #  @param allCards (set) the set of cards that is being checked
    #  @return (boolean) true or false depending on whether it fits or not
    #
    def _royalFlush(self, allCards):
        # Dictionaries {key, value}
        # Ex: {1: 1, 13: 1, 12: 1, 11: 1, 10: 1}
        temp = dict()

        # Adds each card numeric value in the temp dict
        # The int value in the key-value pair is how we determine the royal flush
        for card in allCards:
            if card.getNumericValue() in temp:
                temp[card.getNumericValue()] += 1
            else:
                temp[card.getNumericValue()] = 1

        return self._straightFlush(allCards) and 1 in temp and 10 in temp

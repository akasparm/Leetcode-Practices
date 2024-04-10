class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()

        i = len(deck)-1
        while i>1:
            deck.insert(i-1, deck[-1])
            deck.pop()
            i -= 1

        return deck
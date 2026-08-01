class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        n = len(hand) // groupSize
        arr = [[] for _ in range(n)]
        hand = sorted(hand)
        
        for card in hand:
            placed = False
            # Try to extend an existing group that needs this card next
            for j in range(n):
                if len(arr[j]) > 0 and len(arr[j]) < groupSize and arr[j][-1] + 1 == card:
                    arr[j].append(card)
                    placed = True
                    break
            # Otherwise, start a new group in an empty slot
            if not placed:
                for j in range(n):
                    if len(arr[j]) == 0:
                        arr[j].append(card)
                        placed = True
                        break
            if not placed:
                return False
        
        return True
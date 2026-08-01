class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False
        n=len(hand)//groupSize
        arr=[[] for _ in range(n)]
        hand=sorted(hand)
        for i in hand:
            placed=False
            for j in range(n):
                if len(arr[j])>0 and len(arr[j])<groupSize and arr[j][-1]+1==i:
                    arr[j].append(i)
                    placed=True
                    break
            if not placed:
                for j in range(n):
                    if len(arr[j])==0:
                        arr[j].append(i)
                        placed=True
                        break
            if not placed:
                return False
        return True

            
        
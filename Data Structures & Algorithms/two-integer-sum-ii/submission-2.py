class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
                ndict=defaultdict(int)
                for i in range(len(numbers)):
                        temp=target-numbers[i]
                        if ndict[temp]:
                                return [ndict[temp],i+1]
                        ndict[numbers[i]]=i+1
                return []
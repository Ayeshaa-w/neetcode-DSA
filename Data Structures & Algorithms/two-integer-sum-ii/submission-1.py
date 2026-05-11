class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        for i,c in enumerate(numbers):
            if (target-c) in numbers:
                if numbers.index(target-c) == i:
                    continue
                res.append(i+1)
        return res[:2]
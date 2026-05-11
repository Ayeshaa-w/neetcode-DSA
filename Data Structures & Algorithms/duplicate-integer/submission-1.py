
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        iss=set()
        for i in nums:
            if i in iss:
                return True
            iss.add(i)
        return False

        
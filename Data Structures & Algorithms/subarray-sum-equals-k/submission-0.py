class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        prefixsums={0:1}
        currsum=0
        for i in nums:
            currsum+=i
            diff=currsum-k
            res+=prefixsums.get(diff,0)
            prefixsums[currsum]=1+prefixsums.get(currsum,0)
        return res

        
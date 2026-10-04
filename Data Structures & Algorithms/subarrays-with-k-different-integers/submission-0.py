class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmost(k):
            distinct=0
            freq=defaultdict(int)
            l=0
            count=0
            for r in range(len(nums)):
                if nums[r] not  in freq:
                    distinct+=1
                freq[nums[r]]+=1
                while distinct>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        distinct-=1
                        del freq[nums[l]]
                    l+=1
                count+=r-l+1
            return count
        return atmost(k)-atmost(k-1)

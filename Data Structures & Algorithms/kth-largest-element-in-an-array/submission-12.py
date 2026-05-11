import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert kth largest to the index in a sorted array
        # e.g., in, 1st largest is index 2
        target_idx = len(nums) - k
        
        def quickSelect(l, r):
            # Optimization: Randomly pick a pivot and swap with the end
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            # Move pivot to its final sorted position
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > target_idx:
                return quickSelect(l, p - 1)
            elif p < target_idx:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
        
        return quickSelect(0, len(nums) - 1)
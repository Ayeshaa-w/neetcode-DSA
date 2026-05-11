class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap={}
        ans=[-1]*len(nums1)
        for i,c in enumerate(nums1):
            hashmap[c]=i
        stack=[]
        for curr in nums2:
            while stack and curr>stack[-1]:
                indx=hashmap[stack.pop()]
                ans[indx]=curr
            if curr in hashmap:
                stack.append(curr)
        return ans



        
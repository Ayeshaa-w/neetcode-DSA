class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackt,stack_ind=stack.pop()
                res[stack_ind]=i-stack_ind
            stack.append((t,i))
        return res
                

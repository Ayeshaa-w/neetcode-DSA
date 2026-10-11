# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count,answer=0,None
        def dfs(node):
            nonlocal count,answer
            if not node or answer :
                return 
            dfs(node.left)
            count+=1
            if count==k:
                answer=node.val
                return answer
            dfs(node.right)
        dfs(root)
        return answer
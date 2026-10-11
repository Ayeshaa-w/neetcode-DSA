# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(node):
            if not node:
                return 0
            leftmax=dfs(node.left)
            leftmax=max(leftmax,0)
            rightmax=dfs(node.right)
            rightmax=max(rightmax,0)
            res[0]=max(res[0],node.val+leftmax+rightmax)
            return node.val+max(leftmax,rightmax)
        dfs(root)
        return res[0]
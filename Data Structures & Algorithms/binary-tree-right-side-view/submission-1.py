# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq=collections.deque([root])
        res=[]
        if not root:
            return res
        while dq:
            length=len(dq)
            for i in range(length):
                node=dq.popleft()
                if i==length-1:
                    res.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        cpt = 0
        if root:
            if root.left and root.left.left is None and root.left.right is None:
                cpt += root.left.val
            cpt += self.sumOfLeftLeaves(root.left)
            cpt += self.sumOfLeftLeaves(root.right)
            
        return cpt
        
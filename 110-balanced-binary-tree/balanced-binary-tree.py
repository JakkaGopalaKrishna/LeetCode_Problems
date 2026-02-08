# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (d:=lambda r:(inf,max(l:=d(r.left),r:=d(r.right))+1)[-2<l-r<2] if r else 0)(root)!=inf
        
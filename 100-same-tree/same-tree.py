# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(pr,qr):
            print(pr)
            print(qr)
            print('-----------')
            if(not pr and not qr):
                return
            if(not pr or not qr):
                return False
            if(pr.val != qr.val):
                return False
            if(pr.left==None and qr.left!=None):
                return False
            if(pr.left!=None and qr.left==None):
                return False
            if(pr.left!=None and qr.left!=None):
                res= check(pr.left,qr.left)
                if(res==False):
                    return False

            if(pr.right==None and qr.right!=None):
                return False
            if(pr.right!=None and qr.right==None):
                return False
            if(pr.right!=None and qr.right!=None):
                res = check(pr.right,qr.right)
                if(res==False):
                    return False
            return
        re = check(p,q)
        if(re!=False):
            re =True
        return re

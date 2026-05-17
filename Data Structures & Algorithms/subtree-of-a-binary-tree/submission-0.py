# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # leaf nodes
        if not subRoot:  # if subtree is null:
            return True
        if subRoot and not root:
            return False
        
        # Are root and subroot same tree? 
        if self.sameTree(root, subRoot): return True
    
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    

    def sameTree(self, r, s):
        if not r and not s:
            return True

        if r and not s: 
            return False

        if s and not r: 
            return False

        if s.val != r.val: 
            return False
        
        return self.sameTree(r.left, s.left) and self.sameTree(r.right, s.right)





        
        
        




        


        
        
        
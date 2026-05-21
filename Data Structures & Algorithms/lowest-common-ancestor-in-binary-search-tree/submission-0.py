# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # LCA value has to be between p and q
        node = root
        smaller = min(p.val, q.val)
        larger = max(p.val, q.val)

        if smaller <= node.val and node.val <= larger: return node

        # if node < p < q --> move left
        if node.val < smaller: 
            return self.lowestCommonAncestor(node.right, p, q)

        # if q < p < node --> move right
        if node.val > larger: 
            return self.lowestCommonAncestor(node.left, p, q)
        
        





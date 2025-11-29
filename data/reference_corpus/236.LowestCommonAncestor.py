
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

    def findPath(self, root, target, path):
        if not root: return False
        path.append(root)
        if root == target: return True
        if self.findPath(root.left, target, path) or self.findPath(root.right, target, path):
            return True
        path.pop()
        return False

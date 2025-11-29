
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        return (t1.val == t2.val) and                self.isMirror(t1.right, t2.left) and                self.isMirror(t1.left, t2.right)

    def isSymmetricIterative(self, root: TreeNode) -> bool:
        if not root: return True
        q = [root, root]
        while q:
            t1 = q.pop(0)
            t2 = q.pop(0)
            if not t1 and not t2: continue
            if not t1 or not t2: return False
            if t1.val != t2.val: return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True



class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.sum = -9999999999 #float('-inf')
        self.getSum(root)
        return self.sum

    def getSum(self, root):
        if root is None: return 0
        left = self.getSum(root.left)
        right = self.getSum(root.right)
        max_in_node = max(max(left, right) + root.val, root.val)
        max_sum = max(max_in_node, left + right + root.val)
        self.sum = max(self.sum, max_sum)
        return max_in_node

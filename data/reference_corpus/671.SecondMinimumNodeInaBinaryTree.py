

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        result = []
        self.preorder(root, result)
        return sorted(result)[1] if len(result) > 1 else -1

    def preorder(self, root, result):
        if not root:
            return 0
        if root.val not in result:
            result.append(root.val)
        if root.left:
            self.preorder(root.left, result)
        if root.right:
            self.preorder(root.right, result)

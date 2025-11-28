
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            length = len(queue)
            level = []
            while length:
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                length -= 1
            l = len(level)
            for i in range(l):
                if i == l - 1:
                    level[i].next = None
                if i + 1 < l:
                    level[i].next = level[i+1]
        return root

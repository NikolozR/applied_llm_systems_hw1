def deleteNode(self, root, key):
    if not root: return None
    if key < root.val: 
        root.left = self.deleteNode(root.left, key)
    elif key > root.val:
        root.right = self.deleteNode(root.right, key)
    else:
        # if this node has only one child or no child:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        
        # otherwise, find the inorder successor:
        curr = root.right
        while curr.left:
            curr = curr.left
        
        root.val = curr.val
        root.right = self.deleteNode(root.right, curr.val)
    return root
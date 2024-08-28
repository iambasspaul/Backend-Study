from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap the left and right children
        node.left, node.right = node.right, node.left
        
        # Add the children to the queue if they are not None
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root

# Helper function to insert nodes into the binary tree
def insert_level_order(arr, root, i, n):
    if i < n:
        temp = TreeNode(arr[i])
        root = temp
        
        # insert left child
        root.left = insert_level_order(arr, root.left, 2 * i + 1, n)
        
        # insert right child
        root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    
    return root

# Helper function to print the binary tree in level order
def print_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing Nones that represent missing children in the last level
    while result and result[-1] is None:
        result.pop()
    
    return result

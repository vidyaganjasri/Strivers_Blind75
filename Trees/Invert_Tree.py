'''Inverting a Binary Tree — Our Approach:
Check if the root is None:
If it is, return None (base case of recursion).
If the root is not None:
Swap the left and right child nodes of the current root.
Recursively invert the left and right subtrees:
Call the function on root.left and root.right.
Return the root node after inversion.'''
def invertTree(root):
    if root is None:
        return None

    # Swap children
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root

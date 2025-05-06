'''To find the Lowest Common Ancestor of two nodes in a Binary Search Tree, I leverage the BST property — where the left child is 
smaller and the right child is larger than the current node.
Here's how I approach it:
First, I check if the current node is either of the given nodes p or q. If it is, I return it — because a node is its own ancestor.
Next, I compare both p and q values with the current node:
If both values are less than the current node, I move to the left subtree.
If both are greater than the current node, I move to the right subtree.
If the two nodes lie on different sides, one left and one right, it means the current node is the point where their paths diverge — 
so it is their Lowest Common Ancestor.
I handle the base case by returning None if the root is null.'''
'''
I'm using recursion to solve the LCA problem. Since each recursive call adds a frame to the call stack, the space complexity is proportional to the height of the tree.
In a balanced BST, the height is O(log n), so space complexity is O(log n).
In the worst case (a skewed tree), the height is O(n), so space complexity becomes O(n)'''

'''Iterative approach '''
def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left  # Both nodes are in left subtree
        elif p.val > root.val and q.val > root.val:
            root = root.right  # Both nodes are in right subtree
        else:
            return root  # This is the split point — LCA

def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return 

        if root.val == p.val or root.val == q.val:
            return root 

        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root

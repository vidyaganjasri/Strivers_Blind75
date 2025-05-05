'''
Base Case:
If the node is None, the height is 0.
Recursive Case:
Recursively compute the height of the left and right subtrees.
Combine:
Take the maximum of the two heights and add 1 to include the current node.
📌 Why max()?
Because height is determined by the longest path, not the shortest.
The shorter subtree doesn't affect the total height.'''
if root==None:
    return 0 
l = self.maxDepth(root.left)
r = self.maxDepth(root.right)

return 1+max(l,r)



'''We are initially keeping ranges to ensure the nodes fall within the range.
At the beginning, we will consider the root node to lie within int_min and int_max.
If that is not the case, we simply return False.

We also consider a base condition which handles when we reach the end of the tree — in that case, we simply return True.

After all those conditions, if they are satisfied, we start traversing the left subtree, reassigning the range where the left subtree values should lie within min_val and up to the current root value.
Similarly, for the right subtree, we ensure that the min_val is the current root value and the range goes up to max_val.'''
def isValidBST(self, root):
  """
  :type root: Optional[TreeNode]
  :rtype: bool
  """
  def isBST(root,min_val,max_val):
      if root is None:
          return True 
      if not(min_val<root.val<max_val):
          return False 
      return isBST(root.left,min_val,root.val) and isBST(root.right,root.val,max_val)
  
  return isBST(root,float('-inf'),float('inf'))

'''Check if two trees p and q are identical.
✅ Steps:
Both nodes are None:
This means we've reached the leaves of both trees at the same position.
So, we return True.
One is None and the other is not:
This means structure is different, so return False.
Values of the current nodes differ:
Even if structure is same, differing values means trees aren’t identical.
So, return False.
Else:
Recur for left and right children.
'''
def isSameTree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

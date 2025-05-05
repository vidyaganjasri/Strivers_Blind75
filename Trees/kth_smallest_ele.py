'''
Brute Force Approach (Traverse → Store → Sort):
Traverse the tree (any traversal).
Store all node values in a list.
Sort the list and return the kth element.
Time Complexity: O(N + NlogN)
(O(N) to traverse, O(NlogN) to sort)
Space Complexity: O(N) for the list.

Improved Approach (Inorder Traversal with Extra Space):
Use inorder traversal (which gives sorted values for BST).
Store visited node values in a list.
Return list[k-1] after traversal.
Time Complexity: O(N)
Space Complexity: O(N) for the list.

Optimal Approach (Inorder Traversal without Extra Space):
Perform inorder traversal.
Instead of storing values, maintain a count variable.
Every time you visit a node, increment the count.
When count == k, save that node's value as the result and stop traversal early.
Use a base condition to return if:
You reach a None node (root is None)
Or you’ve already found the kth smallest (result is not None)
Time Complexity: O(H + k) where H = height of tree (Best case)'''
def kthSmallest(self, root, k):
        
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        
        '''
        res = []
        def pre(root):
            if root is None:
                return 
            print(root.val)
            res.append(root.val)
            pre(root.left)
            pre(root.right)

        pre(root)
        res.sort()
        return res[k-1]
        #O(N)+O(NlogN), O(N)

        '''
        '''
        res = []
        def inorder_traversal(root):
            if root is None:
                return 
            inorder_traversal(root.left)
            res.append(root.val)
            inorder_traversal(root.right)
        inorder_traversal(root)
        return res[k-1]
        '''
        
        count = [0]
        result = [None]
        def inorder_traversal(root):
            if root is None or result[0] is not None:
                return 
            inorder_traversal(root.left)
            count[0]+=1 
            if count[0]==k:
                result[0] = root.val
                return 
            inorder_traversal(root.right)

        inorder_traversal(root)
        return result[0]
        
        


'''Approach 1: Height + DFS (Two-pass traversal)
First Pass: Compute the height/depth of the tree using DFS (recursive function).
Second Pass: Traverse again, and only sum the nodes that are at the deepest level (i.e., where current depth == tree height).
Use a list s = [0] to hold the sum, since lists are mutable and avoid needing nonlocal.
Pros: Clear logic, good practice with recursion.'''
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def dfs(root, level, target, s):
    if not root:
        return
    if level == target:
        s[0] += root.val
    dfs(root.left, level + 1, target, s)
    dfs(root.right, level + 1, target, s)

def deepestSum(root):
    depth = height(root)
    s = [0]
    dfs(root, 1, depth, s)
    return s[0]
'''
✅ Approach 2: BFS (One-pass Level Order Traversal)
Use a queue to traverse the tree level by level (Breadth First Search).
For each level, compute the sum of nodes.
At the end, the last computed level_sum will be the sum of the deepest level.
But:
If you add None nodes, the last sum becomes 0 (and deepest sum is at res[-2]).
So, only append non-None nodes.
Optimized BFS Code:
'''
def deepestSum(root):
    queue = [root]
    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.pop(0)
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return level_sum
'''
✅ Summary
Approach	Technique	Time Complexity	Notes
Height + DFS	Two-pass DFS	O(N)	Clear and structured
BFS Level Traversal	One-pass BFS	O(N)	Efficient and concise'''

'''In general, BFS might be the better approach when you want efficiency, especially for large, deep, or skewed trees. But DFS is great for simpler, more readable solutions when recursion depth is manageable.'''

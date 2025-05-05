'''
1.What is the Goal?
We want to return the values of a binary tree level by level — that’s level-order traversal, also known as Breadth First Search (BFS).

2. What Data Structures Do We Use?
A queue: to process nodes in FIFO (first-in, first-out) order.
A result list (res): to store each level's values as a sublist.
A temporary list (level): to store values of the current level.

3. What’s the Core Logic?
Add the root node to the queue.
While the queue is not empty:
Get the number of nodes in the current level (q_len = len(queue)).
For each node in this level:
Pop the node from the queue.
If it’s not None, add its value to level.
Add its left and right children to the queue (even if they are None).
After processing the level, if level is not empty, add it to res.'''
queue = []
res = []
if root==None:
    return res
queue.append(root)
while queue:
    q_len = len(queue)
    level = []
    for _ in range(q_len):
        node = queue.pop(0)
        if node:
            level.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    if level:
        res.append(level) 
    
return res

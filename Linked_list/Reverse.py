'''
 Reversing a Linked List – Two Approaches
✅ 1. Using a Stack (Brute Force)
Step 1: Traverse the linked list and push all the node values into a stack.
Step 2: Traverse the list again and pop values from the stack to overwrite each node’s value.
✅ This uses the Last-In-First-Out (LIFO) principle of the stack.
✅ At the end, return the original head.
❌ Drawback: It uses extra space (O(n)), and it doesn’t reverse the actual node links — only the values.
⚡ 2. In-Place Reversal (Optimal)
We use three pointers: curr, prev (or dummy), and next_node.
Initially, prev = None (acts like a dummy node).
While traversing:
Save next_node = curr.next
Reverse the pointer: curr.next = prev
Move prev forward: prev = curr
Move curr forward: curr = next_node
This continues until curr becomes None.
Finally, prev will be the new head of the reversed list.
'''
#Brute force approach 
'''Extra space 
stk = []
curr  = head
while curr:
    stk.append(curr.val)
    curr = curr.next
curr = head 
while curr:
    curr.val = stk.pop()
    curr = curr.next
return head 
'''
prev = None 
curr = head 
while curr: 
    next_node = curr.next 
    curr.next = prev 
    prev = curr 
    curr = next_node 
return prev

        

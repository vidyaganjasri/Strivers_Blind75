'''Approach 1: Using Auxiliary Memory (Hashing / Set)
Idea: Keep track of all visited nodes.

How: Store each node's reference (id(node)) in a set.

If a node is revisited → there's a cycle.

🧠 Code:
'''

def has_cycle(head):
    visited = set()
    while head:
        if head in visited:
            return True  # cycle detected
        visited.add(head)
        head = head.next
    return False  # no cycle
  
#Time Complexity: O(n)

#Space Complexity: O(n) → uses extra memory
'''

✅ Approach 2: Floyd’s Cycle Detection (Tortoise & Hare)
Use two pointers:

slow: moves one step at a time

fast: moves two steps at a time

If they ever meet → cycle exists

If fast reaches None → no cycle

'''
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

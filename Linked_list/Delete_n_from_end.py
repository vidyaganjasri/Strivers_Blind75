'''

1 one approach we could do is
we traverse the entire the linked list to get the length , and subtract the value which is the position frmo the end of the linked list at which the node should be deleted so
now the difference which we will get will allow us to traverse till the node before the actual node to be deleted, and acc we will perform the operatoin
One thing to keep in mind if they ask to delete the node at positoin k which is the length of linked list we will simply return head.next since they r indirectly asking us to remove the first node
this takes time complexity O(N)+O(N-k)
an optimal approach would be

using two pointers fast and slow pointers, we first travsere fast pointers upto k positoins then simulateneously we move fast and
slow pointer togeater but before that if the fast pointer 
lands on None then we will simply return head.next as 
they are indirectly asking us to remove the first node, 
else we will then simultaneously move the fast and slow pointer togeather until fast .next 
becomes null at this pointer slow will land on before the node to be deleted then we can perform slow.next = slow.next.next



Approach 1: Using Length Calculation
Traverse the Linked List to Find the Length:
We traverse the entire linked list to determine its length L.
Calculate the Position from the Start:
To delete the nth node from the end, we calculate the position from the start as L - n.
Traverse Again:
Then, we traverse the list again up to L - n - 1 (the node just before the node to be deleted). We update the next pointer of this node to skip the node to be deleted.
Time Complexity:
First, the traversal to find the length takes O(N).
Then, the second traversal to delete the node takes O(N - k), where k is the position from the end of the list.
Thus, the overall time complexity is O(N).

Edge Case:
If the node to be deleted is the head node (i.e., the length of the list equals n), we can simply return head.next.

Approach 2: Using Two Pointers (Optimal Approach)
This approach is more efficient, as it reduces the number of traversals:

Initialize Two Pointers:
Use two pointers: fast and slow.
First, move the fast pointer n steps ahead.
Simultaneously Move Both Pointers:
After the fast pointer has moved n steps, move both the fast and slow pointers one step at a time until the fast pointer reaches the last node (i.e., fast.next == None).
At this point, the slow pointer will be just before the node to be deleted.
Delete the Node:
Set slow.next = slow.next.next, effectively deleting the nth node from the end.

Time Complexity:
The time complexity for this approach is O(N) because we traverse the list only once (both pointers moving together).

Edge Case:
If fast reaches None before moving n steps (i.e., the list length is less than n), it means we need to remove the head node, so we return head.next.'''
#Brute force approach 
temp = head 
N = 0 
while temp:
    N+=1 
    temp = temp.next

if N==n:
    return head.next
#Edge cases [1,2] n = 2 and [1] n =1 

K = N-n 
temp = head
while K!=1:
    temp = temp.next 
    K-=1 
temp.next = temp.next.next
return head
'''
fast, slow = head, head

for _ in range(n):
    fast = fast.next

if fast == None:
    return head.next

while fast.next:
    fast = fast.next
    slow = slow.next 
slow.next = slow.next.next
return head

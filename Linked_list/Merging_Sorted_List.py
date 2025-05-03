'''Brute Force – Array + Sort + Create List
Time: O((n + m) log(n + m))
Space: O(n + m)
What it does:
Extracts all values into an array
Sorts them
Creates a new list
Why Brute:
Doesn't use the fact that the input lists are already sorted.
Highest time due to sorting step.'''
array = []
l1 = list1
l2 = list2
while l1:
    array.append(l1.val)
    l1 = l1.next 
while l2:
    array.append(l2.val)
    l2 = l2.next 
array.sort()
dummy = ListNode(None)
temp = dummy 
for i in range(len(array)):
    New_node = ListNode(array[i])
    temp.next = New_node
    temp = New_node 
return dummy.next

'''
Better – Create New Nodes by Comparing
Time: O(n + m)
Space: O(n + m)
What it does:
Compares values one by one
Creates new nodes for the merged list
Why Better:
Uses the sorted property to avoid sorting
But still creates extra space due to new nodes'''
dummy1 = ListNode(None)
dummy = dummy1
curr1 = list1
curr2 = list2
while curr1 and curr2:
    if curr1.val<curr2.val:
        new_node = ListNode(curr1.val)
        dummy.next = new_node
        dummy = new_node 
        curr1 = curr1.next
    else:
        new_node = ListNode(curr2.val)
        dummy.next = new_node 
        dummy = new_node
        curr2 = curr2.next
if curr1:
    dummy.next = curr1
if curr2:
    dummy.next = curr2 
#No point of doing this below since ur appending the remainging untraversed elements as either of the linkedlist has been ended already 
#So to append the reamining the reaminging elements ur doing the above steps but the problem is that ur down below dummy.next will overwrite those lateluy appended elements
#dummy.next = None 
return dummy1.next
'''
Optimal – Reuse Existing Nodes
Time: O(n + m)
Space: O(1)
What it does:
Compares and re-links nodes directly
No extra nodes created
Why Optimal:
No extra memory
Efficient pointer manipulation
Best for performance'''
dummy = ListNode(None)
temp = dummy 
l1 = list1
l2 = list2 

while l1 and l2:
    if l1.val<l2.val:
        temp.next = l1
        temp = l1 
        l1 = l1.next 
    else:
        temp.next = l2 
        temp = l2 
        l2 = l2.next 
if l1:
    temp.next = l1 
if l2:
    temp.next = l2 

return dummy.next



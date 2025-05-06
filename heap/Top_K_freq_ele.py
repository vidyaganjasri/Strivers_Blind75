'''Approach 1: Hash Map + Sorting
Step 1: Count frequencies using a hashmap (i.e. collections.Counter).
Step 2: Sort the items based on frequency in descending order.
Step 3: Return the top k elements.
🔧 Code:'''
from collections import Counter
def topKFrequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in sorted(count.items(), key=lambda x: -x[1])[:k]]
'''
🕒 Time Complexity:
O(N log N) due to sorting.'''

'''
✅ Approach 2: Hash Map + Min Heap (Heapq)
Step 1: Count frequencies using Counter.
Step 2: Use a min heap of size k, where each element is a tuple (frequency, value).
Step 3: Push into heap and pop the smallest when size exceeds k.
Step 4: Return the k most frequent from the heap.
🔧 Code:'''

from collections import Counter
import heapq

def topKFrequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    return [num for freq, num in heap]
'''
🕒 Time Complexity:
O(N log K) → more efficient when k is much smaller than N.'''


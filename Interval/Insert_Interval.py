'''✅ Strategy:
Add intervals before newInterval — those that end before newInterval starts.

Merge overlapping intervals — those that overlap with newInterval (i.e., overlap if interval[i][0] <= newInterval[1]).

Add remaining intervals — those that start after newInterval ends.

🧠 Edge Cases You Covered:
If intervals is empty → return [newInterval].

If newInterval comes after all → handle using the first loop with bounds check.

If newInterval overlaps everything or nothing → handled by merge and third phase respectively.

'''
if len(intervals)==0:
    return [newInterval]
i =0 
res = []
n = len(intervals)

#Edge case [[1,5]] , [6,8]
while i<n and intervals[i][1]<newInterval[0]:
    res.append(intervals[i])
    i+=1 

#Edge case [[1,3][6,9]] , [5,10] hence i<n
while i<n and intervals[i][0]<=newInterval[1]:
    newInterval[0] = min(newInterval[0],intervals[i][0])
    newInterval[1] = max(newInterval[1],intervals[i][1])
    i+=1 
res.append(newInterval)

while i<n:
    res.append(intervals[i])
    i+= 1
return res

'''
We start by keeping track of the first interval as our current new_int, and begin traversing the list from the next interval.
For each interval, we check whether it overlaps with new_int.
If it does, we merge them by taking the minimum of the start values and the maximum of the end values. This updated interval becomes the new new_int.
If it doesn't overlap, it means the current new_int is finalized, so we append it to the result list. 
Then we update new_int to the current non-overlapping interval and continue.
After the loop, we append the last merged interval (new_int) to ensure the final result includes all intervals.
This approach ensures all overlapping intervals are properly merged, and the output list contains only non-overlapping intervals in sorted order.
'''
if len(intervals)<=1:
    return intervals 

res = []
intervals.sort()
new_int = intervals[0]
for i in range(1,len(intervals)):
    if new_int[1]>=intervals[i][0]:
        new_int[0] = min(new_int[0],intervals[i][0])
        new_int[1] = max(new_int[1],intervals[i][1])
    else:
        res.append(new_int)
        new_int = intervals[i]
res.append(new_int)
return res

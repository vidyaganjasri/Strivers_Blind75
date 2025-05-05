'''
Given a list of intervals, return the minimum number of intervals to remove so that the rest are non-overlapping.
✅ Why sort by end time?
Because:
Keeping the interval that ends earlier leaves more room for the next intervals.
If you keep intervals that end later, you might unnecessarily block future ones.
So sorting by end time helps you greedily pick the best non-overlapping intervals.
'''
intervals.sort(key = lambda x:x[1])
end = float('-inf')
c = 0 
for i in range(len(intervals)):
    if intervals[i][0]>=end:
        end = intervals[i][1]
    else:
        c +=1 
return c 

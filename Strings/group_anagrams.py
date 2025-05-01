'''
Brute-Force Approach:
Use two nested loops to compare every string with every other string.
Check whether two strings are anagrams by sorting and comparing.
Maintain a boolean array (visited[]) to avoid grouping the same string multiple times.
If two strings are anagrams, group them together.
This approach works but is inefficient for large inputs.
Time Complexity:
O(n² × k log k), where n is the number of strings and k is the average length of the strings (due to sorting).

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        def is_anagram(s,t):
            return sorted(s)==sorted(t)
        
        res = []
        bool_arr = [0]*len(strs)

        for i in range(len(strs)):
            if not bool_arr[i]:
                curr = []
                curr.append(strs[i])

                for j in range(i+1,len(strs)):
                    if is_anagram(strs[i],strs[j]):
                        curr.append(strs[j])
                        bool_arr[j] =1 
                res.append(curr)
        return res 
'''
'''
 Efficient Approach (Using HashMap):
Use a hashmap (dictionary) to store grouped anagrams.

The key is the sorted version of the string.

For each string:

Sort it → use it as the key.

Append the original string to the list at that key.

At the end, return all the values in the hashmap as the grouped result.

Time Complexity:
O(n × k log k) — better than brute force.
'''
hm = {}
        for i in range(len(strs)):
            ele = ''.join(sorted(strs[i]))
            if ele not in hm.keys():
                hm[ele] = [strs[i]]
            else:
                hm[ele].append(strs[i])
        res = []
        for i in hm.values():
            res.append(i)
        return res

'''
Time Complexity: O(N^2 * 26) (for each substring, finding max frequency among 26 letters).
Logic:
Outer loop picks the start index i of the substring.
For each start index, we initialize a hashmap (or array of size 26) to count frequencies.
Inner loop extends the substring from i to j.
Update the character count.
Calculate conversions = (j - i + 1) - max_freq_in_window.
If conversions <= k, update max_len.
Return the maximum length.
'''
max_len = float('-inf')
        for i in range(len(s)):
            hm = [0]*26
            for j in range(i,len(s)):
                hm[ord(s[j])-ord('A')]+=1 
                #max freq of char in current sub string
                max_freq = max(hm)
                conversions = (j-i+1)- max_freq
                if conversions<=k:
                    max_len = max(max_len,j-i+1)
        return max_len

#Optimized approach 
'''
Time Complexity: O(N) — each character is processed at most twice.
Logic:
Initialize:
left = 0, right = 0, max_len = 0, max_freq = 0
Hashmap/array to keep frequency count.
Expand window with right++:
Update character count and max_freq.
Calculate window_len = right - left + 1
If window_len - max_freq > k, too many conversions:
Shrink window from the left: left++, and update character count.
Keep updating max_len = max(max_len, right - left + 1)
Return max_len.
'''
max_len = float('-inf')
left,right = 0,0
hm = [0]*26
while right<len(s):
    hm[ord(s[right])-ord('A')]+=1 
    max_freq = max(hm)
    conversions = (right-left+1 )- max_freq
    while conversions>k:
        hm[ord(s[left])-ord('A')]-=1 
        left+=1 
        max_freq = max(hm)
        conversions = (right-left+1)-max_freq
    max_len = max(max_len,right-left+1)
    right+=1 
return max_len

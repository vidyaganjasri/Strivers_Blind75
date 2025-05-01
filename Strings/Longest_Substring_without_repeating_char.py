#Brute force approach 
'''
In this approach we use two nested loops
the outer loop responsible for picking the starting index 
while the inner loop for extending the substring 
For each new starting index selected by the outer loop a new bool array of 256 characaters is created 
representing the number of ascii values to keep track of the values that are encoutered so far
As the inner loop iterates 
If the current value has not been encountered so far we mark it in the bool array corresponding to its ascii value
if the char has already been seen we break the inner loop since the substring is no longer valid 
after breaking we will update the max_len acc 
'''

def lengthOfLongestSubstring(self, s):
        
        if len(s)==0:
            return 0 

        max_len = float('-inf')

        for i in range(len(s)):
            bool_array = [0]*256
            for j in range(i,len(s)):
                ind = j
                if bool_array[ord(s[ind])]:
                    ind = j-1
                    break 
                bool_array[ord(s[ind])]=1
            max_len = max(max_len,ind-i+1)

        return max_len


'''
 Optimized Approach – Sliding Window with HashMap
Here’s the logic:
We use a hashmap to keep track of characters and their last seen indices.
We use two pointers:
left: the start of the current window
right: the end (expanding) pointer
We also maintain a variable max_len to keep track of the longest substring without repeating characters.
🔄 How It Works:
Initialize left = 0, right = 0, and max_len = 0.
Start expanding the window by incrementing right.
For each character at index right:
Check if it’s already in the hashmap and if its last seen index ≥ left.
If yes, it means the character repeats within the current window, so move left to last_seen_index + 1.
Add/update the character's index in the hashmap.
Update max_len as max(max_len, right - left + 1).
Repeat this until the end of the string.
'''

#Ofc the edges cases very careful
if len(s)==0:
    return 0 
if len(s)==1:
    return 1

hm = {}
max_len = float("-inf")
left,right = 0,0
while right<len(s):
    if hm and s[right] in hm and hm[s[right]]>=left:
        left = hm[s[right]]+1
    hm[s[right]] = right 
    max_len = max(max_len,right-left+1)
    right+=1 

return max_len

            

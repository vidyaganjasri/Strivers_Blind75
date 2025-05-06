def reversebit(n):
  res = 0 
  for _ in range(32):
      k = n&1#helps us to get the last bit 
      res = res<<1#shifts the result left by 1 position to allow us to add a bit 
      res = res|k#performing or opersation to insert the bit which we got from doing th eand oepation 
      n= n>>1 # we right shift value to process the leftover bits 
  return res 

both tc and sc are O(1)

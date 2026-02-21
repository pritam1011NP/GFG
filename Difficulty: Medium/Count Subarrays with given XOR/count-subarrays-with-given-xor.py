class Solution:
    def subarrayXor(self, arr, k):
        prefix_xor = 0
        count = 0
        freq = {0: 1}  # Important: handles case where prefix_xor == k
        
        for num in arr:
            prefix_xor ^= num
            
            # If prefix_xor ^ k was seen before,
            # then we found subarrays ending here
            if (prefix_xor ^ k) in freq:
                count += freq[prefix_xor ^ k]
            
            # Store/update frequency of current prefix_xor
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1
        
        return count
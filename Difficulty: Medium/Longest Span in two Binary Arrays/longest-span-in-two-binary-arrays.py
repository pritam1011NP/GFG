class Solution:
    def equalSumSpan(self, a1, a2):
        n = len(a1)
        # diff_sum stores the running prefix sum of (a1[i] - a2[i])
        diff_sum = 0
        # Hash map to store the first occurrence of a prefix sum
        # Key: prefix_sum, Value: first index encountered
        first_occurrence = {0: -1} 
        max_len = 0
        
        for i in range(n):
            # Calculate the difference at current index and add to prefix sum
            diff_sum += (a1[i] - a2[i])
            
            if diff_sum in first_occurrence:
                # If this prefix sum has been seen before, the subarray 
                # between the first occurrence and now has a sum of 0.
                current_len = i - first_occurrence[diff_sum]
                if current_len > max_len:
                    max_len = current_len
            else:
                # Store the first time we see this sum to maximize distance later
                first_occurrence[diff_sum] = i
                
        return max_len
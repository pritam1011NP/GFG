class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix_sum = 0
        # Stores the first index where a specific prefix_sum was encountered
        first_occurrence = {}
        max_len = 0
        
        for i in range(n):
            # Transform value: +1 if > k, else -1
            if arr[i] > k:
                prefix_sum += 1
            else:
                prefix_sum -= 1
            
            # Case 1: The subarray from the very beginning (index 0 to i) works
            if prefix_sum > 0:
                max_len = i + 1
            
            # Case 2: We need to find the earliest index 'j' such that 
            # prefix_sum[i] - prefix_sum[j] > 0 (meaning prefix_sum[j] = prefix_sum[i] - 1)
            else:
                # We look for (prefix_sum - 1) because that's the smallest 
                # difference needed to make the current subarray sum positive.
                target = prefix_sum - 1
                if target in first_occurrence:
                    max_len = max(max_len, i - first_occurrence[target])
            
            # Store the index only if the prefix_sum hasn't been seen before
            # to ensure we keep the leftmost index for maximum length.
            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i
                
        return max_len
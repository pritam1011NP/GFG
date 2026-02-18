class Solution:
    def missingRange(self, arr, low, high):
        # Store array elements in a set for O(1) lookup
        nums = set(arr)
        
        missing = []
        
        # Check every number in range [low, high]
        for num in range(low, high + 1):
            if num not in nums:
                missing.append(num)
        
        return missing

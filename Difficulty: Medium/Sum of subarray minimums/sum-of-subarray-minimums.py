class Solution:
    def sumSubMins(self, arr):
        n = len(arr)
        
        left = [0] * n
        right = [0] * n
        
        stack = []
        
        # Previous Less Element
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((arr[i], count))
            left[i] = count
        
        stack = []
        
        # Next Less Element
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack[-1][1]
                stack.pop()
            stack.append((arr[i], count))
            right[i] = count
        
        result = 0
        
        for i in range(n):
            result += arr[i] * left[i] * right[i]
        
        return result
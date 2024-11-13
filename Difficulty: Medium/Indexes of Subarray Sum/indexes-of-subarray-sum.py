#User function Template for python3
class Solution: 
    def subArraySum(self, arr, target):
        
        start = 0
        curr_sum = 0
        
        # Traverse the array
        for end in range(len(arr)):
            # Add current element to the current sum
            curr_sum += arr[end]
            
            # If curr_sum exceeds the target, move the start pointer to the right
            while curr_sum > target and start <= end:
                curr_sum -= arr[start]
                start += 1
            
            # Check if the current sum matches the target
            if curr_sum == target:
                # Return 1-based indices
                return [start + 1, end + 1]
        
        # If no subarray found
        return [-1]

# Example usage:
# code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subArraySum(arr, d)
        print(" ".join(map(str,
                           result)))  # Print the result in the desired format
        tc -= 1
        print("~")

# } Driver Code Ends
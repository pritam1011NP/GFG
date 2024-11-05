#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # Create a set to keep track of elements within the current window of size k
        seen = set()
        
        # Iterate through the array
        for i in range(len(arr)):
            # If element arr[i] is already in the set, return True
            if arr[i] in seen:
                return True
            
            # Add the current element to the set
            seen.add(arr[i])
            
            # Maintain the window size k by removing the oldest element
            if i >= k:
                seen.remove(arr[i - k])
        
        # No duplicates found within k distance
        return False

        # your code


#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends
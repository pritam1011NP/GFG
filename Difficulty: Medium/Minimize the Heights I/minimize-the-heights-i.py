#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        arr.sort()
        n = len(arr)

        # Initial difference
        result = arr[-1] - arr[0]

        # Iterate through the array
        for i in range(n-1):

            # Calculate new min and max heights
            min_height = min(arr[0] + k, arr[i+1] - k)
            max_height = max(arr[i] + k, arr[-1] - k)

            # Update result
            result = min(result, abs(max_height - min_height))

        return result
        # code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends
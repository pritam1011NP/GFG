#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        n=len(arr)
        arr.sort()
        ans=arr[-1]-arr[0]
        smallest=arr[0]+k
        largest=arr[-1]-k
        if smallest>largest:
            smallest,largest=largest,smallest
        
        for i in range(n):
            min_value=min(smallest,arr[i]-k)
            max_value=max(largest,arr[i-1]+k)
            if min_value<0:
                continue
            ans=min(ans,max_value-min_value)
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
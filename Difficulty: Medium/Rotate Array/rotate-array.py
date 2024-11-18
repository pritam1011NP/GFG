#User function Template for python3

class Solution:
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # Handle the case when d > n

        # Function to reverse a part of the array
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Step 1: Reverse the first d elements
        reverse(arr, 0, d - 1)
        # Step 2: Reverse the remaining n-d elements
        reverse(arr, d, n - 1)
        # Step 3: Reverse the entire array
        reverse(arr, 0, n - 1)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders_list = []
        max_from_right = arr[-1]
        leaders_list.append(max_from_right)
        
        # Traverse the array in reverse order starting from the second last element
        for i in range(n-2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders_list.append(max_from_right)
        
        # The leaders were added in reverse order, so reverse the list before returning
        leaders_list.reverse()
        return leaders_list
        

        # code here


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends
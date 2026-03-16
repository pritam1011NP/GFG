from collections import defaultdict

class Solution:
    def countAllPaths(self, root, k):
        prefix = defaultdict(int)
        prefix[0] = 1
        
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.data
            
            count = prefix[curr_sum - k]
            
            prefix[curr_sum] += 1
            
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)
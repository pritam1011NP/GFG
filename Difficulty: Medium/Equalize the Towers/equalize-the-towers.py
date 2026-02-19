class Solution:
    def minCost(self, heights, cost):
        # function to compute cost for making all heights equal to target
        def getCost(target):
            total = 0
            for h, c in zip(heights, cost):
                total += abs(h - target) * c
            return total
        
        left = min(heights)
        right = max(heights)
        
        # binary search on convex function
        while left < right:
            mid = (left + right) // 2
            
            cost1 = getCost(mid)
            cost2 = getCost(mid + 1)
            
            if cost2 > cost1:
                right = mid
            else:
                left = mid + 1
                
        return getCost(left)

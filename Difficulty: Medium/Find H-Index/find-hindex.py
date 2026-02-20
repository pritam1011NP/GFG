class Solution:
    def hIndex(self, citations):
        n = len(citations)
        
        # Create bucket array
        count = [0] * (n + 1)
        
        # Fill buckets
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        total = 0
        
        # Traverse from high to low
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        
        return 0
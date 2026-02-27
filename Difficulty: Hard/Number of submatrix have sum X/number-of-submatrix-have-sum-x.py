class Solution:
    def countSquare(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        # Step 1: Build prefix sum matrix
        prefix = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                prefix[i][j] = (
                    mat[i-1][j-1]
                    + prefix[i-1][j]
                    + prefix[i][j-1]
                    - prefix[i-1][j-1]
                )
        
        count = 0
        
        # Step 2: Try every top-left corner
        for i in range(n):
            for j in range(m):
                
                # Maximum square size possible from (i, j)
                max_size = min(n - i, m - j)
                
                for size in range(1, max_size + 1):
                    r = i + size
                    c = j + size
                    
                    # Step 3: Compute square sum using prefix
                    total = (
                        prefix[r][c]
                        - prefix[i][c]
                        - prefix[r][j]
                        + prefix[i][j]
                    )
                    
                    if total == x:
                        count += 1
        
        return count
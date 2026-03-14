from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root): 
        if not root:
            return []
        
        hd_map = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, hd = q.popleft()
            
            hd_map[hd].append(node.data)
            
            if node.left:
                q.append((node.left, hd - 1))
                
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        
        for hd in sorted(hd_map.keys()):
            result.append(hd_map[hd])
            
        return result
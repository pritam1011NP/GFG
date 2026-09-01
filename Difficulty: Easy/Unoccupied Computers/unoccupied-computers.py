class Solution:
    def solve(self, n, s):
        # 0 = not seen
        # 1 = seen once, did NOT get a computer
        # 2 = currently using a computer
        state = [0] * 26
        
        occupied = 0
        rejected = 0
        
        for ch in s:
            idx = ord(ch) - ord('A')
            
            if state[idx] == 0:
                # First occurrence: customer arrives
                if occupied < n:
                    occupied += 1
                    state[idx] = 2
                else:
                    rejected += 1
                    state[idx] = 1
            
            elif state[idx] == 2:
                # Customer who had a computer is leaving
                occupied -= 1
                state[idx] = 0
            
            else:
                # Customer was rejected earlier and is now leaving
                state[idx] = 0
        
        return rejected
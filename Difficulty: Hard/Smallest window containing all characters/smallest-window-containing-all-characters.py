class Solution:
    def minWindow(self, s, p):
        if len(p) > len(s):
            return ""
        
        from collections import Counter
        
        need = Counter(p)
        required = len(need)
        
        l = 0
        formed = 0
        window = {}
        
        ans = float("inf"), None, None
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in need and window[char] == need[char]:
                formed += 1
            
            while l <= r and formed == required:
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                left_char = s[l]
                window[left_char] -= 1
                
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                
                l += 1
        
        if ans[0] == float("inf"):
            return ""
        
        return s[ans[1]:ans[2] + 1]
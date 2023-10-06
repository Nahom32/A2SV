class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s: return "" # boundary condition 
        ss = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in ss: 
                
                return max(self.longestNiceSubstring(s[:i]),self.longestNiceSubstring(s[i+1:]), key=len)
        return s
        
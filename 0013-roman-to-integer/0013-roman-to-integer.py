class Solution:
    def romanToInt(self, s: str) -> int:
        hs = {'I': 1,'V': 5, 'X': 10,
              'L': 50,'C':100,
              'D': 500,'M': 1000}
        val = 0
        for i in range(len(s)):
            if i < len(s)-1 and hs[s[i]] < hs[s[i+1]]:
                val+=hs[s[i+1]]-hs[s[i]]
            else:
                if i > 0 and hs[s[i-1]] < hs[s[i]]:
                    continue
                else:
                    val+=hs[s[i]]
        return val
        
        
            
                
            
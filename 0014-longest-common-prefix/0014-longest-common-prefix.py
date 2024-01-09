
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        retval = ''
        strs.sort()
        fir,las = strs[0],strs[-1]
        itr = min(len(fir),len(las))
        for i in range(itr):
            if fir[i] != las[i]:
                return retval
            retval+=fir[i]
        return retval
        
            
        
        
            
            
            
        
        
        
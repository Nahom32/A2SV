class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        retval = []
        check = set(p)
        j = 0
        if len(s) < len(p):
            return []
        p_val = defaultdict(int)
        for i in p:
            p_val[i]+=1
        for i in range(len(p),len(s)+1):
            if set(s[j:i]) == check:
                temp = s[j:i]
                s_val = defaultdict(int)
                for i in range(len(p)):
                    s_val[temp[i]]+=1
                if s_val == p_val:
                    retval.append(j)
            j+=1
        return retval
                    
            
                
                    
                
        
        
        
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        m1 = {}
        for i in range(len(s1)):
            if s1[i] not in m1:
                m1[s1[i]] = 1
            else:
                m1[s1[i]]+=1
        for i in range(len(s2)-len(s1)+1):
            m2 = {}
            value = s2[i:i+len(s1)]
            for i in range(len(value)):
                if value[i] not in m2:
                    m2[value[i]] = 1
                else:
                    m2[value[i]]+=1
            if m1  == m2:
                return True      
        return False
            
            
            
        
        
        
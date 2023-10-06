class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kb = 0
        itr = str(num)
        val = itr[:k]
        if num % int(val) == 0:
            kb+=1
               
        for i in range(k,len(itr)):
            val+=str(itr[i])
            val= val[1:]
            if int(val) == 0:
                continue
            if num % int(val) == 0:
                kb+=1
        return kb
        
            
        
        
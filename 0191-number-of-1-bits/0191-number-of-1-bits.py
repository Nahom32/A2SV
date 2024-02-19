class Solution:
    def hammingWeight(self, n: int) -> int:
        valbin = str(bin(n)[2:])
        retval = 0
        for i in valbin:
            if i == '1':
                retval+=1
        return retval
            
       
    
            
        
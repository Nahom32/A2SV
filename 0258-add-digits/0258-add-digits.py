class Solution:
    def addDigits(self, num: int) -> int:
        x= str(num)
        
        while len(x) != 1:
            y = 0
            for i in x:
                y+=int(i)
            x= str(y)
        return int(x)
                
                
            
        
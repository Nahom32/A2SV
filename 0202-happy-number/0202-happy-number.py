class Solution:
    def isHappy(self, n: int) -> bool:
        mat = {'0':0,'1':1 , '2': 4, '3': 9,
               '4': 16, '5': 25, '6': 36,
               '7': 49, '8': 64, '9': 81}
        x = str(n)
        while len(x) > 1:
            y = 0
            for i in x:
                y+=mat[i]
            x = str(y)
        if int(x) == 1 or int(x)==7:
            return True
        return False
            
        
        
        
        
        
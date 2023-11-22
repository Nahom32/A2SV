class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lis = []
        for i in range(left,right+1):
            data = str(i)
            val = True
            for j in data:
                if int(j) == 0 or i % int(j) != 0 :
                    val = False
                    break
            if val == True:
                lis.append(i)
        return lis
            
        
        
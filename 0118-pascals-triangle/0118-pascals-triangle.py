class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        gen = [[1]]
        for i in range(numRows-1):
            if i == 0:
                gen.append([1,1])
            else:
                val = gen[-1]
                data = []
                for i in range(1,len(val)):
                    data.append(val[i]+val[i-1])
                data.insert(0,1)
                data.append(1)
                gen.append(data)
        return gen
                    
        
        
        
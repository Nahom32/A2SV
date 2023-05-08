class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        tot = 0
        for i in range(len(mat)):
            tot+=mat[i][i]
        x = 0
        y = len(mat)-1
        while y >= 0 and x <= len(mat)-1:
            tot+=mat[x][y]
            x+=1
            y-=1
        if len(mat) % 2 != 0:
            val = ceil(len(mat)/2)-1
            tot-=mat[val][val]
        return tot
            
        
        
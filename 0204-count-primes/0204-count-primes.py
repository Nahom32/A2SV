class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        field = [1 for i in range(n+1)]
        pval = 2 # since its the first prime number
        while(pval**2 <= n):
            if field[pval] == 1:
                j = pval**2
                while j < n+1:
                    field[j] = 0
                    j+=pval
            pval+=1
        for i in range(2,n):
            if field[i] == 1:
                count+=1
        return count
                    
        
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        j = n
        while True:
            if j % n == 0 and j % 2 == 0:
                return j
            j*=2
        
            
        
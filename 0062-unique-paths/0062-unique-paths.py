class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def unique(m,n,memo={}):
            if (m,n) in memo.keys():
                return memo[(m,n)]
            if m == 1 and n == 1:
                return 1
            if ((m <1) or (n<1)):
                return 0
            
            memo[(m,n)] = unique(m-1,n,memo) + unique(m,n-1,memo)
            return memo[(m,n)]
        val = unique(m,n)
        return val
        
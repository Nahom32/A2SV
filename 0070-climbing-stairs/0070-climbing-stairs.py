class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        fir,sec = 1,1
        for i in range(n-1):
            temp = fir + sec
            fir = sec
            sec = temp
        return sec
        
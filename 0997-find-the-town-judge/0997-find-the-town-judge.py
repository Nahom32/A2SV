class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = [0]*(n+1)
        trusted = [0]*(n+1)
        for i in trust:
            trusts[i[0]]+=1
            trusted[i[1]]+=1
        j = 1
        while j < n+1:
            if trusts[j] == 0 and trusted[j] == n-1:
                return j
            j+=1
        return -1
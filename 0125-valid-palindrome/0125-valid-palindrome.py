class Solution:
    def isPalindrome(self, s: str) -> bool:
        up = set(range(65,91))
        lo = set(range(97,123))
        num = set(range(48,58))
        cor = ''
        for i in s:
            if ord(i) in up or ord(i) in lo:
                cor+=i.lower()
            elif ord(i) in num:
                cor+=i
        p1 = 0
        p2 = len(cor) - 1
        while p1 < p2:
            if cor[p1] != cor[p2]:
                return False
            p1+=1
            p2-=1
        return True
        
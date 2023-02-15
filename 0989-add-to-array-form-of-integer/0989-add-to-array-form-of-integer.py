class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        a = ''
        for i in num:
            a+=str(i)
        b = int(a) + k
        hol = []
        for i in str(b):
            hol.append(int(i))
        return hol
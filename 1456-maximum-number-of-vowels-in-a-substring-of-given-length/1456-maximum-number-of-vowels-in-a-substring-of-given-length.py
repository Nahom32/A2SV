class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        slide = s[:k]
        count = 0
        mxval = 0
        for i in slide:
            if i in vowels:
                count+=1
        mxval = count
        for i in range(k, len(s)):
            count += int(s[i] in vowels)
            count -= int(s[i - k] in vowels)
            mxval = max(mxval, count)
        return mxval
            
        
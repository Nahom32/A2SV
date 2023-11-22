class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ''
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            merge+=word1[i]
            merge+=word2[j]
            i+=1
            j+=1
        if len(word1) > len(word2):
            merge+=word1[i:]
        elif len(word1) < len(word2):
            merge+=word2[j:]
        return merge
            
        
        
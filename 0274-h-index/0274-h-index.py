class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        hindex = 0
        for i in range(len(citations)):
            if citations[i] <= len(citations[i:]):
                hindex = citations[i]
            else:
                if hindex  < len(citations[i:]):
                    hindex = len(citations[i:])
        return hindex
                
                
        
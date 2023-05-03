class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        n1 = []
        n2 = []
        for i in nums1:
            if i not in s2 and i not in n1:
                n1.append(i)
        for i in nums2:
            if i not in s1 and i not in n2:
                n2.append(i)
        return [n1, n2]
        
                
                
                
        
        
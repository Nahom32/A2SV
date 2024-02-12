class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        values = set()
        tally = Counter()
        tres = len(nums)//3
        for i in nums:
            tally[i]+=1
            if tally[i] > tres:
                values.add(i)
        return list(values)
            
            
            
        
        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        fir = 0
        las = len(nums) -1
        
        while fir <= las:
            mid = (fir + las)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                las = mid - 1
            else:
                fir = mid + 1
        return -1
        
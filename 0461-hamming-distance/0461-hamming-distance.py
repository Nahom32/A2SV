class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin  = str(bin(x)[2:])
        ybin = str(bin(y)[2:])
        count = 0
        chug_val_1 = '0'*(32-len(xbin))
        chug_val_2 = '0'*(32-len(ybin))
        xbin = chug_val_1 + xbin
        ybin = chug_val_2 + ybin
        for i in range(len(xbin)):
            if xbin[i] != ybin[i]:
                count+=1
        return count
        
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        holder = {}
        for i in s:
            if i in holder.keys():
                holder[i]+=1
            else:
                holder[i]=1
        if 1 not in holder.values():
            return -1
        for i in range(len(s)):
            if holder[s[i]] == 1:
                return i
            
        
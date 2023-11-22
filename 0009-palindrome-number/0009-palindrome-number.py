class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        can be solved using different techniques recursion, string reversal and two pointers.
        '''
        val  = str(x)
        i = 0
        j = len(val)-1
        while j > i:
            if val[i] != val[j]:
                return False
            i+=1
            j-=1
        return True
        
        
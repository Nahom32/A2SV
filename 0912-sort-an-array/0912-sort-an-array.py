class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_alternative(a: List[float],l:int,r:int,q:int):
            '''
            This procedure assumes that the two sublists in it are sorted ascendingly.
            If this is not met the whole process will not work at all.
            This varies from the above auxiliary procedure in such a way this algorithm doesn't contain
            a sentinel in the sublists.
            '''
            left = a[l:r+1] #contains the sublist from l to r
            right = a[r+1:q+1] #contains the sublist from r+1 to q
            nL = r-l+1 #adds one to cntain the lth element.
            nR = q-r # this is similar to nL as follows nR = q -(r+1)+1 the ones cancel
            i = 0 #pointer index for left
            j= 0 #pointer index for right
            a_var = l
            while i < nL and j < nR:
                if left[i] <= right[j]:
                    a[a_var] = left[i]
                    i+=1
                else:
                    a[a_var] = right[j]
                    j+=1
                a_var+=1
            while i < nL:
                a[a_var] = left[i]
                i+=1
                a_var+=1
            while j < nR:
                a[a_var] = right[j]
                j+=1
                a_var+=1



        def merge_recur(a,p,r):
            '''
            This algorithm recursively breaks the elements of the array until it reaches a singlton
            array. Then merges them ascendingly.
            '''
            if p >=r:
                return
            else:
                m = (p+r)//2
                merge_recur(a,p,m)
                merge_recur(a,m+1,r)
                merge_alternative(a,p,m,r)
                
        merge_recur(nums,0,len(nums)-1)
        return nums            
                        
        
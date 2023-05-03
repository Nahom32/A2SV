class Solution:
    def reverse(self, x: int) -> int:
        sign = ''
        b = str(x)
        if b[0]=='-':
            sign = '-'
            b = b[1:]
        a = list(b)
        ptr_1 = 0
        ptr_n = len(a)-1
        for i in range(len(a)//2):
            a[ptr_1],a[ptr_n] = a[ptr_n], a[ptr_1]
            ptr_1+=1
            ptr_n-=1
        collector = ''
        for i in a:
            collector+=i
        number = sign + collector
        if int(number) >= pow(2,31)-1 or int(number)<= -pow(2,31):
            return 0
        else:
            return int(number)
        
        
        
        
            
                
        
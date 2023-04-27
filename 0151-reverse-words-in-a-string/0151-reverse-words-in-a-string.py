class Solution:
    def reverseWords(self, s: str) -> str:
        x  = s.strip()
        y = x.split(" ")
        print(y)
        for i in y:
            i = i.strip()
        
        fir = 0
        las = len(y) - 1
        while fir < las:
            y[fir],y[las] = y[las],y[fir]
            fir+=1
            las-=1
        x = ''
        for i in y:
            if i != '':
                x+=i
                x+=" "
        return x.strip()
    
        
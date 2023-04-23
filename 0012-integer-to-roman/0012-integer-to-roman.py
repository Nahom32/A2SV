class Solution:
    def intToRoman(self, i: int) -> str:
        htab = {1:'I', 5:'V', 10:'X', 
                50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        val = ''
        while i > 0:
            if i >= 1000:
                val+=htab[1000]
                i-=1000
            elif i >= 500:
                if i >= 900:
                    val+=htab[100]
                    val+=htab[1000]
                    i-=900
                else:
                    val+=htab[500]
                    i-=500
            elif i >= 100:
                if i >= 400:
                    val+=htab[100]
                    val+=htab[500]
                    i-=400
                else:
                    val+=htab[100]
                    i-=100
            elif i >= 50:
                if i >= 90:
                    val+=htab[10]
                    val+=htab[100]
                    i-=90
                else:
                    val+=htab[50]
                    i-=50
            elif i >= 10:
                if i >= 40:
                    val+=htab[10]
                    val+=htab[50]
                    i-=40
                else:
                    val+=htab[10]
                    i-=10
            elif i >= 5:
                if i >= 9:
                    val+=htab[1]
                    val+=htab[10]
                    i-=9
                else:
                    val+=htab[5]
                    i-=5
            elif i >= 1:
                if i >=4:
                    val+=htab[1]
                    val+=htab[5]
                    i-=4
                else:
                    val+=htab[1]
                    i-=1
        return val
                
                
                
                
        
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stacker = []
        for i in s:
            buffer = []
            if i != ')':
                stacker.append(i)
            else:
                while stacker[len(stacker)-1] != '(':
                    a = stacker.pop()
                    buffer.append(a)
                stacker.pop()
                for i in buffer:
                    stacker.append(i)
        return ''.join(stacker)
        
    
                
            
            
            


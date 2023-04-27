class Solution:
    def simplifyPath(self, path: str) -> str:
        x = path.split("/")
        print(x)
        stack = []
        for i in x:
            if i != '..' and i != '' and i != '.':
                stack.append(i)
            elif i == '..':
                if stack != []:
                    stack.pop()
        x = '/'
        for i in stack:
            x+=i
            x+='/'
        if len(x) > 1:
            return x[:-1]
        else:
            return x
            
            
            
        
        
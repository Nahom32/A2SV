from math import floor
class Solution:
    def add(self,a,b):
        return a+b
    def multiply(self,a,b): 
        return a*b
    def divide(self,a,b):
        return int(a/b)
    def subtract(self,a,b): 
        return a-b
    
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        for i in tokens:
            if i in operators:
                first = stack.pop()
                second = stack.pop()
                result = operators[i](second,first)
                stack.append(result)
            else:
                stack.append(int(i))
        return stack.pop()

        
            
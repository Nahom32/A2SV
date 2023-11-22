class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_array = []
        for i in range(1,n+1):
            if i%3 == 0 and i % 5 == 0:
                fizz_array.append("FizzBuzz")
            elif i%3 == 0:
                fizz_array.append("Fizz")
            elif i%5 == 0:
                fizz_array.append("Buzz")
            else:
                fizz_array.append(str(i))
        return fizz_array
            
        
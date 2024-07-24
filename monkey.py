class A:
    def add(self,a,b):
        return a + b

def multiply(a,b):
    return a * b

A.add = multiply

print(A.add(2,3))
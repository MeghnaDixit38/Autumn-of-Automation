import math
class Complex():

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def display(self):
        if self.b>0:
            print(f"{self.a}+{self.b}i")
        else:
            print(f"{self.a}{self.b}i")
    def add(self,obj):
        return Complex(self.a + obj.a, self.b + obj.b)
    def subtract(self,obj): 
        return Complex(self.a - obj.a, self.b - obj.b)
    def modulus(self):
        return math.sqrt((self.a)**2+ (self.b)**2)
    def multiply(self,obj):
        return Complex(self.a *obj.a - self.b*obj.b, self.a*obj.b+self.b*obj.a)
    def conjugate(self):
        return Complex(self.a,-self.b)
 



    
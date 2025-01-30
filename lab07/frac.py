
def gcd(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return abs(a)

class Frac:
    def __init__(self,numer,denom):
        mgm = gcd(numer,denom)
        self.numer = int(numer / mgm)
        self.denom = int(denom / mgm)

        if self.denom < 0:
            self.denom = -self.denom
            self.numer = -self.numer
    def __str__(self):
        return f"{self.numer}/{self.denom}"
    
    def add(self, other):
        return Frac(self.numer*other.denom + self.denom*other.numer, self.denom*other.denom)
    
    def sub(self,other):
        return Frac(self.numer*other.denom - self.denom*other.numer, self.denom*other.denom)
    
    def mul(self,other):
        return Frac(self.numer*other.numer, self.denom*other.denom)
    
    def div(self,other):
        return Frac(self.numer*other.denom, self.denom*other.numer)
    
    def __add__(self,other):
        return self.add(other)
    
    def __sub__(self,other):
        return self.sub(other)
    
    def __mul__(self,other):
        return self.mul(other)
    
    def __truediv__(self,other):
        return self.div(other)

#Addera
x = Frac(1, 6)
y = Frac(1, 6)
z = x.add(y)
print(f"{x} + {y} = {z}")

#Subtrahera
x = Frac(2, 3)
y = Frac(1, 6)
z = x.sub(y)
print(f"{x} - {y} = {z}")

#Multiplicera
x = Frac(2, 5)
y = Frac(3, 4)
z = x.mul(y)
print(f"{x} * {y} = {z}") 

#Dividera
x = Frac(3, 7)
y = Frac(5, 2)
z = x.div(y)
print(f"{x} / {y} = {z}")



x = 1/3 + 1/3 + 1/6 + 1/6
print(x)

x = Frac(1,3)
x = x.add(x)
y = Frac(1,6)
y = y.add(y)
z = x.add(y)
print(z) 

x = (1/3) + (1/3) + (1/6) * (1/6)
print(x)

x = Frac(1,3)
x = x.add(x)
y = Frac(1,6)
y = y.mul(y)
z = x.add(y)
print(z)

# 1/3 + 1/3 + 1/6 + 1/6
x = Frac(1,3)
y = Frac(1,6)
print(x + x + y + y)

# 2/3 - 1/6 
x = Frac(2, 3)
y = Frac(1, 6)
print (x-y)

# 3/7 / 5/2

x = Frac(3, 7)
y = Frac(5, 2)
print (x/y) 

# (1/3) + (1/3) + (1/6) * (1/6)
x = Frac(1,3)
y = Frac(1,6)
print (x+x+y*y)



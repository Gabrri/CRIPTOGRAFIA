##Sea s la cantidad de n´umeros primos entre 15 y 43155. Encuentre s.
import math

def es_primo(num):
    if num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

a = 15
b = 43155
m=0

for i in range(a,b+1,2):
    bl = es_primo(i)
    if bl == True:
        m = m+1

######################################################################


def primitivo(p):
    c= 0
    for j in range(2,3):
        y = p**j
        while y % 4 == 1:
            c = c+1
    return(c)

p = 4

for i in range(2,p-1):
    a = primitivo(i)
    print("el orden de "+str(i)+"es"+str(a))

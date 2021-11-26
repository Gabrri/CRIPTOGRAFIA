
# Input un entero m

def FindST(mm1):
    cont = 0
    num = mm1
    while mm1 % 2 != 1:
        cont += 1
        mm1 = mm1/2
    return cont, num/2**cont


def RabinMiller(m):
    if m%2 != 0:
        mm1 = m-1
        S, T = FindST(mm1)
        for b in range(2,m):
            y = (b**T)%(m)
            if y%m == 1:
                return "Primo"
            else:
                for i in range(0,S):
                    if y%m == m-1:
                        return "Primo"
                    else:
                        y = (y**2)%m
            return "Compuesto"
    else:
        return "Compuesto"
    

totalprime = 0
for i in range(15,43156):
    if(RabinMiller(i) == "Primo"):
        totalprime += 1





print(RabinMiller(13))
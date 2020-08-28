CODIGO PUNTO 3:\\
    \item Alfabeto0 = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,\\"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,\\"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}\\
Alfabeto1 = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i"\\,9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s"\\,19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
def decript(a,b,subc):\\
    # max = a\\
    # min = b\\
    # if()\\
    mcd,a_1,b_1 = xgcd(a,26)\\
    m = ((a_1)*(subc-b)) % 26\\
    return m\\

def encript(a,b,m):\\
    c = (a*m+b) %26\\
    return c;\\

def decriptAll(a,b,c):\\
    c = c.lower()\\
    cod = []\\
    m = ""\\
    for i in c:\\
        # print(cod)\\
        cod.append(int(decript(a,b,Alfabeto0[i])))\\
    for i in cod:\\
        m = m + Alfabeto1[i]\\
    return m\\
def encriptAll(a,b,m):\\

    m = m.lower()\\
    cod = []\\
    c = ""\\
    for i in m:\\
        cod.append(encript(a,b,Alfabeto0[i]))\\
    for i in cod:\\
        c = c + Alfabeto1[i]\\
    return c\\
def xgcd(a, b):\\
    Args:\\
        a: mcd(a,b)=resultado\\
        b: mcd(a,b)=resultado\\
    Returns:\\
        Returns mcd(a,b) and (u0,v0)\\
    if b == 0:\\
        return 0,1,0\\

    u0 = 1\\
    u1 = 0\\
    v0 = 0\\
    v1 = 1\\

    while b != 0:\\
        q = a//b\\
        r = a - b * q\\
        u = u0 - q * u1\\
        v = v0 - q * v1\\
        a = b\\
        b = r\\
        u0 = u1\\
        u1 = u\\
        v0 = v1\\
        v1 = v\\

    return  a, u0, v0\\
def inversos(a,b):\\
    r =[a,b]\\
    res = int(r[len(r)-2]/r[len(r)-1])\\
    qi = [res]\\
    while(r[len(r)-1]!= 1):\\
        div = r[len(r)-2]-r[len(r)-1]\\
        r.append(div)\\
        res = int(r[len(r)-2]/r[len(r)-1])\\
        qi.append(res)\\
    #calculemos s_i que es el inverso de a\\
    ai = [1,0]\\
    for i in range(len(qi)-1):\\
        s = ai[len(ai)-2]- qi[i]*ai[len(ai)-1]\\
        ai.append(s)\\

    bi = [0,1]\\
    for i in range(len(qi)-1):\\
        t = bi[len(bi)-2]- qi[i]*bi[len(bi)-1]\\
        bi.append(t)\\
    for i in range(len(r)):\\
        print(r[i],"    ",  qi[i-1],   "  ", ai[i])\\
    return ai[len(ai)-1], bi[len(bi)-1]\\
mcd,a_1,b_1= xgcd(1234,357)\\
m = ""\\
#Punto 3\\
# message = "DUSUTCSUTKYUCEDUPCKHUNCDUYKCHYKUQDUUPKTSCTKYUDUPCKHUN\\CDUSUTCSUTKYUGUIEE"\\
# mensajeDesEncriptado =\\
decriptAll(15,20,message)\\
# print(mensajeDesEncriptado)\\

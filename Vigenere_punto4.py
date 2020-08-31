Alfabeto0 = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

Alfabeto1 = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
Ingles = 0.066


#Calcular el periodo j de k
def getMatrix(longitud,mEncriptado):
    matrices = []
    for p in range(1,10):
        matrix = []
        for k in range(p):
            matrix.append([])
        for i in range(longitud):
            mod = i%(p)
            matrix[mod].append(mEncriptado[i])
        matrices.append(matrix)
    return matrices
def getprob(submatrix):
    probabilidades = []
    for fila in submatrix:
        n = len(fila)
        probabilidad = {}
        probabilidad['a'] = fila.count('a')/n
        probabilidad['b'] = fila.count('b')/n
        probabilidad['c'] = fila.count('c')/n
        probabilidad['d'] = fila.count('d')/n
        probabilidad['e'] = fila.count('e')/n
        probabilidad['f'] = fila.count('f')/n
        probabilidad['g'] = fila.count('g')/n
        probabilidad['h'] = fila.count('h')/n
        probabilidad['i'] = fila.count('i')/n
        probabilidad['j'] = fila.count('j')/n
        probabilidad['k'] = fila.count('k')/n
        probabilidad['l'] = fila.count('l')/n
        probabilidad['m'] = fila.count('m')/n
        probabilidad['n'] = fila.count('n')/n
        probabilidad['o'] = fila.count('o')/n
        probabilidad['p'] = fila.count('p')/n
        probabilidad['q'] = fila.count('q')/n
        probabilidad['r'] = fila.count('r')/n
        probabilidad['s'] = fila.count('s')/n
        probabilidad['t'] = fila.count('t')/n
        probabilidad['u'] = fila.count('u')/n
        probabilidad['v'] = fila.count('v')/n
        probabilidad['w'] = fila.count('w')/n
        probabilidad['x'] = fila.count('x')/n
        probabilidad['y'] = fila.count('y')/n
        probabilidad['z'] = fila.count('z')/n
        probabilidades.append(probabilidad)
    return probabilidades
def getindiceDeCoincidencia(submatrix, longitud):
    probabilidads = getprob(submatrix)
    fec = []
    for fila in range(len(submatrix)):
        sum = 0
        for i in Alfabeto0.keys():
            sum+= probabilidads[fila][i]**2
        fec.append(sum)
    suma=0
    for i in fec:
        suma+= i
    promIndice = suma/len(submatrix)
    error = (Ingles - promIndice)**2
    return error

def getPeriod(mEncriptado):
    longitud = len(mEncriptado)
    m = getMatrix(longitud,mEncriptado)
    errores = []
    for submatrix in m:
        errores.append(getindiceDeCoincidencia(submatrix, longitud))
    periodo = 0
    min = 1000
    #print(errores)
    for i in range(len(errores)):
        if(errores[i]<min):
            min = errores[i]
            periodo = i
    return (m[periodo])
#Terminamos de calcular j(el periodo)

#Vamos a atacar
def getFrec(submatrix):
    frecuencias = []
    for fila in submatrix:
        frecuencia = []
        frecuencia.append(fila.count('a'))
        frecuencia.append(fila.count('b'))
        frecuencia.append(fila.count('c'))
        frecuencia.append(fila.count('d'))
        frecuencia.append(fila.count('e'))
        frecuencia.append(fila.count('f'))
        frecuencia.append(fila.count('g'))
        frecuencia.append(fila.count('h'))
        frecuencia.append(fila.count('i'))
        frecuencia.append(fila.count('j'))
        frecuencia.append(fila.count('k'))
        frecuencia.append(fila.count('l'))
        frecuencia.append(fila.count('m'))
        frecuencia.append(fila.count('n'))
        frecuencia.append(fila.count('o'))
        frecuencia.append(fila.count('p'))
        frecuencia.append(fila.count('q'))
        frecuencia.append(fila.count('r'))
        frecuencia.append(fila.count('r'))
        frecuencia.append(fila.count('s'))
        frecuencia.append(fila.count('t'))
        frecuencia.append(fila.count('u'))
        frecuencia.append(fila.count('v'))
        frecuencia.append(fila.count('w'))
        frecuencia.append(fila.count('x'))
        frecuencia.append(fila.count('y'))
        frecuencia.append(fila.count('z'))
        frecuencias.append(frecuencia)
    return frecuencias
def get3options(fila):
    fila2=[]
    letras_eta = []
    for i in range(len(fila)):
        fila2.append(fila[i])
    e = max(fila2)
    idx_e = fila2.index(e)
    fila2.pop(idx_e)
    idx_t = max(fila2)
    fila2.pop(idx_t)
    if(idx_t>=idx_e):
        idx_t+=1

    idx_a = max(fila2)
    if(idx_a>=idx_e):
        idx_a+=1
    if(idx_a>=idx_t):
        idx_a+=1
    letras_eta.append(idx_e)
    letras_eta.append(idx_t)
    letras_eta.append(idx_a)
    return letras_eta

def findLetter(frecuencia):
    print("Esta es la fila")
    fila =[]
    for i in range(26):
        x = frecuencia[i] +  frecuencia[(i+4)%26] + frecuencia[(i+19)%26]
        fila.append(x)
    options = get3options(fila)
    letra = [Alfabeto1[options[0]],Alfabeto1[options[1]],Alfabeto1[options[2]]]
    return letra
def attack(texto):
    elegida = getPeriod(texto.lower())
    frecuencias = getFrec(elegida)
    clave = []
    for i in range(len(elegida)):
        clave.append(findLetter(frecuencias[i]))
        print("La clave es")
    print(clave)
    clavefin = ""
    for i in clave:
        clavefin+=i[0]
    return clavefin
#Mensaje encriptado
texto = "IEHAFMLYYNNOXAAYLJENRLROVNLVIAGOZMOYESEFELEHNTLXAVDPYTUECPLVVPOWUOXJOHMLJKAOHMYGHPYAZEZQAANLMEYLPPAADESIFMLTDRNDSEYIGPDJIESNBOESEETSZUTHEEHNNEZLBVPLNQBPWOIEOMYZE"
print(attack(texto))

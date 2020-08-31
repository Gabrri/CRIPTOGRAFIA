# codigo 4 punto de la primera tarea
Alfabeto0 = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
Alfabeto1 = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
frecuenciasIngles = {"a":0.082, "b": 0.015, "c":0.028,"d":0.043,"e":0.127, "f": 0.022, "g":0.020, "h": 0.061, "i": 0.070, "j": 0.002,"k":0.008, "l": 0.040, "m":0.024, "n":0.067, "o":0.075, "p": 0.019, "q": 0.001, "r":0.060, "s":0.063,"t":0.091,"u":0.028,"v":0.010,"w":0.023,"x":0.001,"y":0.020,"z":0.001}
Ingles = 0.066






#Calcular el periodo j de k
llave = "Hola"


def getMatrix(longitud,mEncriptado):
    matrices = []
    for p in range(1,100):
        matrix = []
        for k in range(p):
            matrix.append([])
        for i in range(longitud):
            mod = i%(p)
            matrix[mod].append(mEncriptado[i])
        matrices.append(matrix)
    return matrices
def getFrec(submatrix):
    frecuencias = []
    for fila in submatrix:
        n = len(fila)
        frecuencia = {}
        frecuencia['a'] = fila.count('a')/n
        frecuencia['b'] = fila.count('b')/n
        frecuencia['c'] = fila.count('c')/n
        frecuencia['d'] = fila.count('d')/n
        frecuencia['e'] = fila.count('e')/n
        frecuencia['f'] = fila.count('f')/n
        frecuencia['g'] = fila.count('g')/n
        frecuencia['h'] = fila.count('h')/n
        frecuencia['i'] = fila.count('i')/n
        frecuencia['j'] = fila.count('j')/n
        frecuencia['k'] = fila.count('k')/n
        frecuencia['l'] = fila.count('l')/n
        frecuencia['m'] = fila.count('m')/n
        frecuencia['n'] = fila.count('n')/n
        frecuencia['o'] = fila.count('o')/n
        frecuencia['p'] = fila.count('p')/n
        frecuencia['q'] = fila.count('q')/n
        frecuencia['r'] = fila.count('r')/n
        frecuencia['s'] = fila.count('s')/n
        frecuencia['t'] = fila.count('t')/n
        frecuencia['u'] = fila.count('u')/n
        frecuencia['v'] = fila.count('v')/n
        frecuencia['w'] = fila.count('w')/n
        frecuencia['x'] = fila.count('x')/n
        frecuencia['y'] = fila.count('y')/n
        frecuencia['z'] = fila.count('z')/n
        frecuencias.append(frecuencia)
    return frecuencias

def getindiceDeCoincidencia(submatrix, longitud):
    frecuencias = getFrec(submatrix)
    fec = []
    for fila in range(len(submatrix)):
        sum = 0
        for i in Alfabeto0.keys():
            sum+= frecuencias[fila][i]**2
        fec.append(sum)
    suma=0
    for i in fec:
        suma+= i
    promIndice = suma/len(submatrix)
    #print(promIndice)
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
    return (m[periodo+1])
#Terminamos de calcular j(el periodo)
#Empezamos a hacer el ataque ._.
    # [    [filashift 1]  ]
    # [    [filashift 2]   ]
    # [    [filashift 3]   ]
    # [    [filashift 4]   ]
    # [    [filashift 5]   ]
    # [    [filashift 6]   ]
def shift(fila,p):
    fila2 = []
    for i in fila:
        x = (Alfabeto0[i]-p)%26
        # print(x)
        fila2.append(Alfabeto1[x])
    # print("Este es fila2")
    # print(fila2)
    return fila2
#
def realShift(shifteos):
    idxAlphabet = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    min = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
    i = 0

    for shift in shifteos:
        if(frecuenciasIngles['a']- shift['a'] < min[0]):
            min[0] = shift['a']
            idxAlphabet[0] = i
        if(frecuenciasIngles['b']- shift['b'] < min[1]):
            min[1] = shift['b']
            idxAlphabet[1] = i
        if(frecuenciasIngles['c']- shift['c'] < min[2]):
            min[2] = shift['c']
            idxAlphabet[2] = i
        if(frecuenciasIngles['d']- shift['d'] < min[3]):
            min[3] = shift['d']
            idxAlphabet[3] = i
        if(frecuenciasIngles['e']- shift['e'] < min[4]):
            min[4] = shift['e']
            idxAlphabet[4] = i
        if(frecuenciasIngles['f']- shift['f'] < min[5]):
            min[5] = shift['f']
            idxAlphabet[5] = i
        if(frecuenciasIngles['g']- shift['g'] < min[6]):
            min[6] = shift['g']
            idxAlphabet[6] = i
        if(frecuenciasIngles['h']- shift['h'] < min[7]):
            min[7] = shift['h']
            idxAlphabet[7] = i
        if(frecuenciasIngles['i']- shift['i'] < min[8]):
            min[8] = shift['i']
            idxAlphabet[8] = i
        if(frecuenciasIngles['j']- shift['j'] < min[9]):
            min[9] = shift['j']
            idxAlphabet[9] = i
        if(frecuenciasIngles['k']- shift['k'] < min[10]):
            min[10] = shift['k']
            idxAlphabet[10] = i
        if(frecuenciasIngles['l']- shift['l'] < min[11]):
            min[11] = shift['l']
            idxAlphabet[11] = i
        if(frecuenciasIngles['m']- shift['m'] < min[12]):
            min[12] = shift['m']
            idxAlphabet[12] = i
        if(frecuenciasIngles['n']- shift['n'] < min[13]):
            min[13] = shift['n']
            idxAlphabet[13] = i
        if(frecuenciasIngles['o']- shift['o'] < min[14]):
            min[14] = shift['o']
            idxAlphabet[14] = i
        if(frecuenciasIngles['p']- shift['p'] < min[15]):
            min[15] = shift['p']
            idxAlphabet[15] = i
        if(frecuenciasIngles['q']- shift['q'] < min[16]):
            min[16] = shift['q']
            idxAlphabet[16] = i
        if(frecuenciasIngles['r']- shift['r'] < min[17]):
            min[17] = shift['r']
            idxAlphabet[17] = i
        if(frecuenciasIngles['s']- shift['s'] < min[18]):
            min[18] = shift['s']
            idxAlphabet[18] = i
        if(frecuenciasIngles['t']- shift['t'] < min[19]):
            min[19] = shift['t']
            idxAlphabet[19] = i
        if(frecuenciasIngles['u']- shift['u'] < min[20]):
            min[20] = shift['u']
            idxAlphabet[20] = i
        if(frecuenciasIngles['v']- shift['v'] < min[21]):
            min[21] = shift['v']
            idxAlphabet[21] = i
        if(frecuenciasIngles['w']- shift['w'] < min[22]):
            min[22] = shift['w']
            idxAlphabet[22] = i
        if(frecuenciasIngles['x']- shift['x'] < min[23]):
            min[23] = shift['x']
            idxAlphabet[23] = i
        if(frecuenciasIngles['y']- shift['y'] < min[24]):
            min[24] = shift['y']
            idxAlphabet[24] = i
        if(frecuenciasIngles['z']- shift['z'] < min[25]):
            min[25] = shift['z']
            idxAlphabet[25] = i
        i+=1
    real = moda(idxAlphabet)

    return real[0]


def nose(matrix):
    print("Este es matrix 0")
    print(matrix[0])
    final=[]
    for nfila in range(3):
        filas = []
        for i in range(25):
            filas.append(shift(matrix[nfila],i))
        print("Este es filas")
        print(filas)
        shifteos = getFrec(filas)
        print(shifteos)
        real = realShift(shifteos)
        final.append(filas[real])
    print("Este es final")
    print(final)

def moda(datos):
    repeticiones = 0
    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n
    moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia
    for i in datos:
        n = datos.count(i) # Devuelve el número de veces que x aparece enla lista.
        if n == repeticiones and i not in moda:
            moda.append(i)
    if len(moda) != len(datos):
        return moda
    else:
        print ('No hay moda')
# texto ="HelloMiNameIsJhanCarlosCeliMaldonadoAndILikeToEatPizzaWithMyFriendsAndILikeToGoToTheParkToSeeMyFavoritePetCallsJuanCamilo"
texto = "IEHAFMLYYNNOXAAYLJENRLROVNLVIAGOZMOYESEFELEHNTLXAVDPYTUECPLVVPOWUOXJOHMLJKAOHMYGHPYAZEZQAANLMEYLPPAADESIFMLTDRNDSEYIGPDJIESNBOESEETSZUTHEEHNNEZLBVPLNQBPWOIEOMYZE"
print(len(texto))

periodo = getPeriod(texto.lower())
nose(periodo)

from settings import *

def escala(keyI,scaleType,typek):
    type = []
    scale = []
    mod = []

    if keyI in extra:
        key = extrc[extra.index(keyI)]
    else:
        key = keyI

    keyList = list(key)

    scaleType = scaleType

    if typek == None:
        if 'b' in key or key.upper() == 'F':
            type = typeA
        else:
            type = typeB
    else:
        if typek == 'b':
            type = typeA
        else:
            type = typeB

    index = type.index(key)

    for i in scaleType:
        scale.append(type[(i+index)%12])

    return [scale,type]

def afinacao(notas,typek):
    notas = list(notas)
    type = typek
    cordas = []

    if type == typeA:
        type2 = typeB
    else:
        type2 = typeA

    for i in range(len(notas)):
        if notas[i] == '#' or notas[i] == 'b':
            notas[i-1] += notas[i]

    for i in notas:
        if i == '#' or i == 'b':
            notas.remove(i)
    
    for i in range(len(notas)):
        if notas[i] in extra:
            notas[i] = extrc[extra.index(notas[i])]


    for i in notas:
        corda_notas = []

        if i in type:
            index = type.index(i)
        else:
            index = type2.index(i)

        for j in range(25):
            
            corda_notas.append(type[(j+index)%12])
        
        cordas.append(corda_notas)

    return cordas

def escalaGuita(keyI,afn,type):
    force = keyI
    typek = None
    if keyI in extra:
        key = extrc[extra.index(keyI)]

    else:
        key = keyI

    if len(keyI) > 1:
        typek = list(keyI)[1]

    scale = escala(key,type,typek)
    cordas = afinacao(afn,scale[1])

    for i in cordas:
        pO = ''
        for j in range(len(i)):
            if i[j] not in scale[0]:
                    i[j] = ''

            if i[j] == key:
                i[j] = force

    return cordas

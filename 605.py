def revisar_lados(array, position):

    result = {}

    if position - 1 >= 0:
        result['detrás'] = array[position - 1]
    else:
        result['detrás'] = None

    if position + 1 < len(array):
        result['adelante'] = array[position + 1]
    else:
        result['adelante'] = None

    return result

# Ejemplo de uso
# mi_lista = [1,0,0,0,1]
# mi_lista =  [1,0,1,0,1]
# mi_lista =   [1,0,1,0]
# mi_lista =   [0,0,0]
# mi_lista = [0,0,1,0,1]
# mi_lista = [1,0,0,0,1,0,0]
jardin = [1,0]

# Cantidad a plantar
n = 2


contador = 0
for i in range(len(jardin)):
    resultado = revisar_lados(jardin, i)

    if jardin[i] == 0:
        if resultado['detrás'] != 1 and resultado['adelante'] != 1:
            contador += 1
            jardin[i]= 1

print(contador)


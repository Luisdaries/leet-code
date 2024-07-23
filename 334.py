nums = [1,5,0,4,1,3]
# nums = [9,10,5,11,10,9,8]
# nums = [14,22,21,11,90]

filtrada = []
filtrada2 = []
j = 0
result = False
def myfunc(i, j, arreglo):
            contar = 1
            array = []
            auxiliar= i
            array.append(arreglo[i])
            while j < len(arreglo):
                if arreglo[i] < arreglo[j]:
                    array.append(arreglo[j])
                    contar = contar + 1
                    arreglo[i] = arreglo[j]
                j += 1
            return array

for i in range(len(nums)):

            lista = myfunc(i, j, nums)

            filtrada.append(lista)

            j += 1

for lista in filtrada:


    print(lista)
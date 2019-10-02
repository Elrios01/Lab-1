def hallar_moda(numeros, dato_repetido):
    cont = 0
    cantidad_numeros = len(numeros)
    for i in range(cantidad_numeros):
        if dato_repetido == numeros [i]:
            cont = cont + 1
    
    return cont

dato_repetido = input("Ingrese el numero que quiere saber cuantas veces se repite en el arreglo: ")
dato_repetido = int(dato_repetido)

numeros = [1, 6, 2, 8, 3, 7, 3, 4, 6, 9, 10]

contar = hallar_moda(numeros, dato_repetido)
print(contar)

from hallar_moda import contar

arreglo = [2,3,2,30,20,8,9,10,8,3,5,3,20,8,9,9]

numeros_contados = []
moda = 0
cantidad_moda = 0

for num inarreglo:
  if 
    cantidad = contar(numeros, dato_repetido)
  if cantidad > cantidad_moda:
    moda = num
    cantidad_moda = cantidad
  numeros_contados.append(num)
print("La moda es: ", moda)
    
    

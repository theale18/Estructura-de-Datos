"""
Escribir la funcion cantidadPrimos(arreglo), que retorna la cantidad de numeros primos
que forman parte de un Arreglo. Las soluciones que NO sean RECURSIVAS no seran
tomadas en cuenta

Ej. si
arreglo1 = [5,10,9,8,13,21]    =>    cantidadPrimos(arreglo1) = 2

Se puede asumir que ya tiene la funcion esPrimo(n) que devuelve Verdadero cuando n
es Primo
"""

import numpy as np

def primo(n):
            # Check if the number is less than
            # or equal to 1, return False if it is
    if n <= 1:
        return False

# Recorre todos los números desde 2 hasta la raíz cuadrada de n (redondeado hacia abajo al entero más cercano)
    for i in range(2, int(n**0.5)+1):
        
# If n is divisible by any of these numbers, return False
        if n % i == 0:
            return 0
            
# If n is not divisible by any of these numbers, return True
    return 1



#               1 1   1   1      1      1
arr = np.array([2,3,4,5,6,7,8,10,11,12,13])


# el arreglo no esta vacio
def contarPrimos(arr):
  cant = primo(arr[0])
  if len(arr) > 1:
      
# arr[1:] devuelve el mismo arreglo sin el 1er elemento (arr[0])
    cant = cant + contarPrimos(arr[1:])
  return cant

print(contarPrimos(arr))

#  18/09/23

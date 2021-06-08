#Ejercicio 1

#Ejercicio 2
#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

#Funcion para el area del circulo
def areacirculo(radio):
   
    pi = 3.1416
    return pi*radio**2

#Funcion para el area del cilindro
def cilindro(radio, altura):
   
    return area_circulo(radio)*altura_cilindro
   
print("El volumen del cilindro es:")
print(volumen_cilindro(3,5))

#Ejercicio 3
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

#Nota se estalblece lista para usar los numeros de la media
def lista(lista):
    
    media = (lista[0] + lista[1] + lista[2] + lista[3] + lista[4])/5
    return media

li = [0,0,0,0,0]
lista[0] = int(input("Ingrese su primer numero: "))
lista[1] = int(input("Ingrese su segundo número: "))
lista[2] = int(input("Ingrese su tercer número: "))
lista[3] = int(input("Ingrese su cuarto número: "))
lista[4] = int(input("Ingrese su quinto número: "))
   
print(f"Lista {lista[0]}, {lista[1]}, {lista[2]}, {lista[3]} y {lis[4]}, la media es: {lista(li)}")
   
#Ejercicio 4
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def square(listas):
    #Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list1 = []
    for i in listas:
        list1.append(i**2)
    return list1
print("La lista de numeros enteros es la siguiente: ")
print(square([1, 2, 3, 4, 5]))
print("La lista de numeros cuadrados es la siguiente: ")
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

#Ejercicio 5

#Ejercicio 6
#Ejercicio 7
#Ejercicio 8

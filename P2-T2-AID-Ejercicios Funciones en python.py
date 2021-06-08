#Ejercicio 1
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA 
#y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
def funcion(factur, iva=21):
    
    return factur + iva/100

print("Total de iva ",funcion(1000,10))
print("Total ",funcion(1000))

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
#Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
#PRIMERO minimocomundiv
def calalcularmcd(numm1,numm2):
    mcd = 1
    if numm1 % numm2 == 0:
        return numm2
    for k in range(int(numm1/2), 0, -1):
        if numm1 % a == 0 and numm2 % a == 0:
            mcd = a
            break
    return mcd

def calcularmcm(numer1,numer2):

#Este es para el minimocomun multiplo
  if numer1 > numer2:
    m = numer1
  else:
    m = numer2
  while (m % numer1 != 0) or (m % numer2 != 0):
        m += 1
  return m



#Ejercicio 7
#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

def bin(num1):
    totalbin = "{0:b}".format(num1)
    return totalbin

def dec(num2):
    totaldec = int(str(num2), 2)
    return totaldec
    
#formula fin
print("CONVERTIDOR")
num1 = int(input("Digita un numero decimal: "))
num2 = int(input("Digita un número binario: "))

print(f"Número en binario: {bin(num1)}")
print(f"Número en decimal: {dec(num2)}"    
    
    
#Ejercicio 8
#Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

-#definir binario a decimal
def numerobinario(numero1):
    totalbininario = "{0:b}".format(numero1)
    return total_bin
    
numero1 = int(input("Ingresa un numero decimal: "))
int(f"Conversion en binario: {numerobinario(numero1)}")
#decimal a binario
def decimal(numeros):
    totaldecimal = int(str(numero2), 2)
    return totaldecimal
    
numero2 = int(input("Ingresa un número binario: "))
print(f"Convertir en decimal: {decimal(numero2)}")




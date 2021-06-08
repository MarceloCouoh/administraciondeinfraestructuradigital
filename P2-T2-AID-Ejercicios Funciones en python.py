#Ejercicio 1

#Ejercicio 2
#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
def area_circulo(radio):
   
    formula_pi = 3.1416
    return formula_pi*radio**2

def volumen_cilindro(radio, altura_cilindro):
   
    return area_circulo(radio)*altura_cilindro

print(volumen_cilindro(3,5))

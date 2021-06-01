#Llamamos las funciones declaradas en otro archivo
from FuncionesExternas import *

#Invocamos las funciones
funcion1()

#Invocamos la otra función
Q = input("Introduzca un dato:  ")
W = input("Introduzca otro dato:  ")

print(funcion2(Q,W))

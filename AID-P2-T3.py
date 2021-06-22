#!/usr/bin/env python
# coding: utf-8

# #Ejercicio 1
# #Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%.

# In[ ]:


import pandas as pd


# In[ ]:


inicial = int(input('Escriba el año inicial: '))
final = int(input('Escriba el año final: '))
venta = {}
for i in range(inicial, final+1):
    venta[i] = float(input('Escriba las ventas anuales,' + str(i) +': '))
venta = pd.Series(venta)
print('Venta\n', venta)
print('Venta con descuento\n', venta*0.9)


# In[ ]:





# #Ejercicio 2
# #Escribir una función que reciba un diccionario con las notas de los alumnos en curso en un examen y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.

# In[ ]:


import pandas as pd


# In[ ]:


def diccionario(notas):
    notas = pd.serie(notas)
    estadisticas = pd.serie([notas.min(), notas.max(), 
                              notas.mean(), notas.std()], index=['Min', 'Max', 'Media', 'Desviación típica'])
    return estadisticas

notas = {'Marcelo':10, 'Reyna':9.5, 'Caleb':7, 
         'Itzayane': 9, 'Alessandra': 8.5}
print(diccionario(notas))


# In[ ]:





# #Ejercicio 3
# Escribir una función que reciba undiccionario con las notas de los alumnos en curso en un examen y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.

# In[ ]:


import pandas as pd


# In[ ]:


def diccionario2(notas):
    notas = pd.Series(notas)
     
    return notas[notas >= 5].sort_values(ascending=False)
notas = {'Marcelo':10, 'Reyna':9.5, 'Caleb':7, 
         'Itzayane': 9, 'Alessandra': 8.5}
print(diccionario2(notas))


# In[ ]:





# #Ejercicio 4
# #Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:
# #Mes      Ventas  Gastos 
# #Enero    30500   22000
# #Febrero  35600   23400
# #Marzo    28300   18100
# #Abril    33900   20700
# 

# In[ ]:


import pandas as pd


# In[ ]:


diccionarioD = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
                   'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
form = pd.DataFrame(diccionarioD)
print(form)


# In[ ]:





# # Ejercicio 5
# #Escribir una función que reciba un DataFrame con el formato del ejercicio anterior, una lista de meses, ydevuelva el balance (ventas -gastos) total en los meses indicados.

# In[ ]:


import pandas as pd


# In[ ]:


diccionarioD= {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
                   'Ventas':[30500, 35600, 28300, 33900], 
                   'Gastos':[22000, 23400, 18100, 20700]}

form = pd.DataFrame(diccionario_dat)

def balance(form, meses):
    form['Balance'] = form.Ventas - form.Gastos
    return form[form.Mes.isin(meses)].Balance.sum()

print(balance(form, ['Enero','Abril']))


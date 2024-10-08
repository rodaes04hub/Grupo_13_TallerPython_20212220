# -*- coding: utf-8 -*-
"""GRUPO_13_Tarea2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15qB_2asL15cuCmg4iTrQYQngbU6FLCfg

Ejercicio I
"""

import pandas as pd

data_ciudades = {'ciudad': ['lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo', 'Piura', 'Iquitos', 'Huancayo', 'Tacna', 'Pucallpa'],
    'Habitantes': [1047996, 100169, 92331, 428450, 305717, 484475, 441649, 385098, 294395, 283734],
    'Area_km2': [2672.28, 1545.77, 1487.7, 116.5, 279.89, 6217.26, 368.9, 109.19, 59.4, 483.44],
    'Altitud_m': [154, 2325, 34, 3399, 29, 29, 106, 3271, 562, 156],
    'Densidad_poblacion_por_km2': [3924, 64.8, 62.1, 3673, 1091.6, 77.9, 1196, 3528.6, 4966, 587.2]}

nfo = pd.DataFrame(data_ciudades)

print(nfo)

"""Ejercicio 2"""

import pandas as pd
data_ciudades_2 = { 'ciudad':['lima','Arequipa','Trujillo','Cusco','Chiclayo','Piura','Iquitos','Huancayo','Tacna','Pucallpa'],
                'Genticilicio':['Limense','Arequipeño','Trujillano','Cusqueño','Chiclayano','Piurano','Iqueño','Huancaino','Tacneño','Pucallpeño'],
                  'Provincia':['Lima','Arequipa','Trujillo','Cusco','Chiclayo','Piura','Maynas','Huancayo','Tacna','Coronel Portillo'],
                   'Región':['Lima','Arequipa','La libertad','Cusco','Lambayeque','Piura','Loreto','Junín','Tacna','Ucayali']}

nombres = pd.DataFrame(data_ciudades_2)
print(nombres)

"""Ejercicio 3

cuando queremos realizar el inner merge, no sale toda el cuadro fusionado en una sola linea, sino uno debajo del otro, sin embargo, se esta intentando verificar que no haya duplicados en la clave comun, pero aun así no funciona, evidencia abajo
"""

nfo=nfo.drop_duplicates(subset=['ciudad'])
nombres=nombres.drop_duplicates(subset=['ciudad'])

cuadro_1=pd.merge(nfo, nombres, on='ciudad', how='inner')
print(cuadro_1)

"""Ejercicio 4
La minima densidad poblacional es 62.1 y corresponde a la ciudad de trujillo y la maxima es 4966.0 y corresponde a la ciudad de Tacna

ejercicio 5
"""

!pip install numpy

import numpy as np

!pip install matplotlib

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(x=cuadro_1['ciudad'], height=cuadro_1['Habitantes'], color='darkred')
ax.set_xlabel('ciudad')
ax.set_ylabel('habitantes')
ax.set_title('numero de habitantes por ciudad en Peru')
ax.tick_params(axis='x', rotation=90)
plt.show()

"""ejercicio 6"""

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(cuadro_1['Altitud_m'], cuadro_1['Habitantes'], color='darkblue')
ax.set_title('relacion entre altitud y numero de habitantes de las ciudades en Peru')
ax.set_xlabel('altitud(m)')
ax.set_ylabel('habitantes(n)')
plt.show()
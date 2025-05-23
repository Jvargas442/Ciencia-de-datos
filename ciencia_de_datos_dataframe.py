# -*- coding: utf-8 -*-
"""Ciencia de Datos:Dataframe

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xs8mlr5T28ibwLqRbUdRDChI_7M6xwbF
"""

import numpy as np
import pandas as pd

#Convertir de lista a dataframe
ventas=pd.Series([22,15,70])
ventas

ventas=pd.Series([22,15,70],index=["Enero","Febrero","Marzo"])
ventas

ventas[0]

ventas["Enero"]

ventas.dtype

#Para visualizacion de valores
ventas.index

ventas.values

ventas.name="Ventas 2025"
ventas

ventas.index.name="Meses"
ventas

ventas.shape

diccionario={"Enero":22,"Febrero":15,"Marzo":70}
type(diccionario)

ventas1=pd.Series(diccionario)
ventas1

alex=pd.Series(diccionario,index=["Enero","Febrero","Marzo","Abril"])
alex

medidas=pd.DataFrame(
    {"Humedad":[41,20,30,80],
     "Salinidad":[22,15,30,80],
     "Sensorica":["si","no","no","no"],
     "Acidez":["alta","media","baja","baja"],
     "PH":[1,7,14,13]},
    index=["LA Ureña","Paso Chico","La Laguna","Los Teres"])
medidas

medidas.index.name="Veredas"
medidas

medidas[["Humedad","PH"]]

medidas.axes

medidas.values

medidas.shape

"""###Ejercicios
dado los siguientes diccionarios, convertirlos en datagramas y usar todos los metodos aprendidos

```

elementos={"número atómico": [1,6,47,88],
"Masa atómica": [1,12,107,226],
"Familia": ["No metal", "No metal", "Metal", "Metal"]}

```

Agregar como registros el nombre de los elementos

2. Convertir en dataframe el siguiente conjunto de medidas


```
medida_2020={"Ag":2,"Au":5, "Cu":3,"Pt:2}
medida_2021={"Ag":4,"Au":3,"Cu":6,"Pt:1}
medida_2022={"Ag":8,"Au":2,"Cu":15,"Pt:0}
medida_2023={"Ag":5,"Au":1,"Cu":0,"Pt:5}
medida_2024={"Ag":7,"Au":0,"Cu":3,"Pt:2}
medida_2025={"Ag":9,"Au": 1, "Cu": 3, "Pt:5}
```

Tenga en cuenta que los registros son los meses de medida y las features deben ser los elementos
"""

import pandas as pd

elementos = {"número atómico": [1, 6, 47, 88],
            "Masa atómica": [1, 12, 107, 226],
            "Familia": ["No metal", "No metal", "Metal", "Metal"]}
df_elementos = pd.DataFrame(elementos)
df_elementos

df_elementos["número atómico"].dtype

df_elementos["Masa atómica"].dtype

df_elementos["Familia"].dtype

df_elementos.index

df_elementos.values

df_elementos.name = "Tabla de Elementos"
df_elementos

df_elementos.index.name = "Elementos"
df_elementos

df_elementos = pd.DataFrame(elementos, index=["Hidrógeno", "Carbono", "Plata", "Radio"])
df_elementos

import pandas as pd

medida_2020 = {"Ag": 2, "Au": 5, "Cu": 3, "Pt": 2}
medida_2021 = {"Ag": 4, "Au": 3, "Cu": 6, "Pt": 1}
medida_2022 = {"Ag": 8, "Au": 2, "Cu": 15, "Pt": 0}
medida_2023 = {"Ag": 5, "Au": 1, "Cu": 0, "Pt": 5}
medida_2024 = {"Ag": 7, "Au": 0, "Cu": 3, "Pt": 2}
medida_2025 = {"Ag": 9, "Au": 1, "Cu": 3, "Pt": 5}

medidas = {
    "2020": medida_2020,
    "2021": medida_2021,
    "2022": medida_2022,
    "2023": medida_2023,
    "2024": medida_2024,
    "2025": medida_2025
}

df_medidas = pd.DataFrame(medidas)

df_medidas = df_medidas.T
df_medidas
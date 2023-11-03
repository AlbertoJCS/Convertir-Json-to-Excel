import json
import pandas as pd
import os

ruta = r"D:\python\Convertir\convertir.json"
ruta2 = r"D:\python\Convertir"

# Abrir el archivo JSON y cargar su contenido
with open(ruta, 'r', encoding='UTF-8') as archivo_json:
    data = json.load(archivo_json)

# Crear el DataFrame y guardar como Excel en la misma carpeta
df = pd.DataFrame(data)
excel_ruta = os.path.join(ruta2, 'data.xlsx')
df.to_excel(excel_ruta, index=False)
df.to_excel('data.xlsx', index=False)
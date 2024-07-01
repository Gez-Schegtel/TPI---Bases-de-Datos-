import csv
import random
from faker import Faker

# Inicializar Faker en español
faker = Faker('es_ES')

# Nombre del archivo CSV con los datos de Declaracion_Jurada
archivo_declaracion_jurada = 'declaracion_jurada.csv'

# Leer los iddj del archivo de Declaracion_Jurada
iddj_list = []
with open(archivo_declaracion_jurada, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        iddj_list.append(int(row['iddj']))

# Generar datos para la tabla Carga_Horaria
carga_horaria_data = [
    {
        'dia': faker.day_of_week(),
        'lugar': faker.city(),
        'horario': faker.time(),
        'nombre_catedra': faker.job(),
        'iddj': iddj
    }
    for iddj in iddj_list
]

# Nombre del archivo CSV para la tabla Carga_Horaria
archivo_carga_horaria = 'carga_horaria.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_carga_horaria = ['dia', 'lugar', 'horario', 'nombre_catedra', 'iddj']

# Crear y escribir los datos en el archivo CSV
with open(archivo_carga_horaria, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_carga_horaria)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(carga_horaria_data)  # Escribir los datos

print(f"{len(iddj_list)} registros generados y exportados a {archivo_carga_horaria}")

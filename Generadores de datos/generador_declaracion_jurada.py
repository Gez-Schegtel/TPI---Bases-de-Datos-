import csv
import random
from faker import Faker

fake = Faker('es_ES')

# Nombre del archivo CSV con los datos de Profesores
archivo_profesores = 'profesores.csv'

# Leer los DNI del archivo de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(row['dni'])

# Número de registros a crear.
num_records = 20

# Comprobar que se leyeron suficientes DNIs
if len(dni_list) < num_records:
    raise ValueError("El archivo 'profesores.csv' no contiene suficientes registros de DNI.")

# Generar datos para la tabla Declaracion_Jurada
declaracion_jurada_data = []

for _ in range(num_records):
    declaracion_jurada_data.append({
        'iddj': fake.unique.random_int(min=1000, max=1000*num_records),
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Declaracion_Jurada
archivo_declaracion_jurada = 'declaracion_jurada.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_declaracion_jurada = ['iddj', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_declaracion_jurada, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_declaracion_jurada)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(declaracion_jurada_data)  # Escribir los datos

print(f"{len(declaracion_jurada_data)} registros generados y exportados a {archivo_declaracion_jurada}")
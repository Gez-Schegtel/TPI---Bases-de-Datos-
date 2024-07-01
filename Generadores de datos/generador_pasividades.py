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

# Generar datos para la tabla Pasividades
pasividades_data = []
for iddj in iddj_list:
    pasividades_data.append({
        'regimen': faker.random_element(elements=('AFP', 'IPS', 'Caja Militar', 'Docente')),
        'iddj': iddj,
        'desde': faker.date_this_decade(),
        'causa': faker.sentence(nb_words=3),
        'suspendido': random.choice([True, False]),
        'institucion_abonante': faker.company()
    })

# Nombre del archivo CSV para la tabla Pasividades
archivo_pasividades = 'pasividades.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_pasividades = ['regimen', 'iddj', 'desde', 'causa', 'suspendido', 'institucion_abonante']

# Crear y escribir los datos en el archivo CSV
with open(archivo_pasividades, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_pasividades)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(pasividades_data)  # Escribir los datos

print(f"{len(iddj_list)} registros generados y exportados a {archivo_pasividades}")

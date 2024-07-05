import csv
import random
from faker import Faker

# Inicializar Faker en español
faker = Faker('es_ES')

# Nombre del archivo CSV con los datos de Profesores
archivo_profesores = 'profesores.csv'

# Leer los DNIs del archivo de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(row['dni'])

# Número de registros a generar
num_records = 20

# Verificar que hay suficientes registros en el archivo
if len(dni_list) < num_records:
    raise ValueError(f"El archivo '{archivo_profesores}' no contiene suficientes registros.")

# Generar datos para la tabla Publicaciones
publicaciones_data = []
for _ in range(num_records):
    publicaciones_data.append({
        'titulo': faker.sentence(nb_words=5),
        'autores': faker.name(),
        'referencia_bibliografica': faker.sentence(),
        'año': faker.random_int(min=1950, max=2024),  # Año entre 2000 y 2023
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Publicaciones
archivo_publicaciones = 'publicaciones.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_publicaciones = ['titulo', 'autores', 'referencia_bibliografica', 'año', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_publicaciones, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_publicaciones)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(publicaciones_data)  # Escribir los datos

print(f"{len(publicaciones_data)} registros generados y exportados a {archivo_publicaciones}")

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
        dni_list.append(int(row['dni']))

# Número de registros a generar
num_records = 20

# Verificar que hay suficientes registros en el archivo
if len(dni_list) < num_records:
    raise ValueError(f"El archivo '{archivo_profesores}' no contiene suficientes registros.")

# Generar datos para la tabla Idiomas
idiomas_data = []
for _ in range(num_records):
    idiomas_data.append({
        'idioma': faker.language_name(),
        'nivel': faker.random_element(elements=('Básico', 'Intermedio', 'Avanzado')),
        'certificacion': faker.word(),
        'institucion': faker.company(),
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Idiomas
archivo_idiomas = 'idiomas.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_idiomas = ['idioma', 'nivel', 'certificacion', 'institucion', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_idiomas, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_idiomas)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(idiomas_data)  # Escribir los datos

print(f"{len(idiomas_data)} registros generados y exportados a {archivo_idiomas}")

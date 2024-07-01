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
num_records = 100

# Verificar que hay suficientes registros en el archivo
if len(dni_list) < num_records:
    raise ValueError(f"El archivo '{archivo_profesores}' no contiene suficientes registros.")

# Generar datos para la tabla Titulos
titulos_data = []
for _ in range(num_records):
    desde_date = faker.date_between(start_date='-30y', end_date='-1y')  # Fecha desde hace 30 años hasta hace 1 año
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d')  # Fecha hasta desde la fecha desde hasta ayer
    titulos_data.append({
        'nivel': faker.random_element(elements=('Grado', 'Maestría', 'Doctorado')),
        'titulo_obtenido': faker.job(),
        'institucion': faker.company(),
        'desde': desde_date,
        'hasta': hasta_date,
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Titulos
archivo_titulos = 'titulos.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_titulos = ['nivel', 'titulo_obtenido', 'institucion', 'desde', 'hasta', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_titulos, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_titulos)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(titulos_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_titulos}")

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

# Generar datos para la tabla Cursos_y_Conferencias
cursos_data = []
for _ in range(num_records):
    desde_date = faker.date_between(start_date='-10y', end_date='-1y')  # Fecha desde hace 10 años hasta hace 1 año
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d')  # Fecha hasta desde la fecha desde hasta ayer
    cursos_data.append({
        'nombre': faker.sentence(nb_words=3),
        'descripcion': faker.text(max_nb_chars=200),
        'institucion': faker.company(),
        'desde': desde_date,
        'hasta': hasta_date,
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Cursos_y_Conferencias
archivo_cursos = 'cursos_y_conferencias.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_cursos = ['nombre', 'descripcion', 'institucion', 'desde', 'hasta', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_cursos, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_cursos)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(cursos_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_cursos}")

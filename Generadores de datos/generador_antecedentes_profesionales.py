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

# Generar datos para la tabla Antecedentes_Profesionales
antecedentes_data = []
for _ in range(num_records):
    desde_date = faker.date_between(start_date='-20y', end_date='-1y')  # Fecha desde hace 20 años hasta hace 1 año
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d')  # Fecha hasta desde la fecha desde hasta ayer
    antecedentes_data.append({
        'empresa_anterior': faker.company(),
        'tipo_actividad': faker.job(),
        'cargo': faker.word(),
        'desde': desde_date,
        'hasta': hasta_date,
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Antecedentes_Profesionales
archivo_antecedentes = 'antecedentes_profesionales.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_antecedentes = ['empresa_anterior', 'tipo_actividad', 'cargo', 'desde', 'hasta', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_antecedentes, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_antecedentes)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(antecedentes_data)  # Escribir los datos

print(f"{len(antecedentes_data)} registros generados y exportados a {archivo_antecedentes}")
import csv
import random
from faker import Faker

# Inicializar Faker en español
faker = Faker('es_ES')

# Nombre del archivo CSV con los datos de Actividades_y_Antecedentes
archivo_actividades = 'actividades_y_antecedentes.csv'

# Leer los DNIs y dedicaciones de la tabla Actividades_y_Antecedentes
dni_dedicacion_list = []
with open(archivo_actividades, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_dedicacion_list.append({
            'dni': int(row['dni']),
            'dedicacion': row['dedicacion']
        })

# Número de registros a generar
num_records = 100

# Verificar que hay suficientes registros en la tabla
if len(dni_dedicacion_list) < num_records:
    raise ValueError(f"La tabla '{archivo_actividades}' no contiene suficientes registros.")

# Generar datos para la tabla Antecedentes_Docentes
antecedentes_docentes_data = []
for _ in range(num_records):
    desde_date = faker.date_between(start_date='-20y', end_date='-1y') 
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d') 
    record = random.choice(dni_dedicacion_list)
    antecedentes_docentes_data.append({
        'unidad_academica': faker.company(),
        'cargo': faker.job(),
        'dedicacion': record['dedicacion'],
        'dni': record['dni'],
        'desde': desde_date,
        'hasta': hasta_date,
        'id_antecedente': faker.unique.random_int(min=1, max=1000)
    })

# Nombre del archivo CSV para la tabla Antecedentes_Docentes
archivo_antecedentes_docentes = 'antecedentes_docentes.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_antecedentes_docentes = ['unidad_academica', 'cargo', 'dedicacion', 'dni', 'desde', 'hasta', 'id_antecedente']

# Crear y escribir los datos en el archivo CSV
with open(archivo_antecedentes_docentes, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_antecedentes_docentes)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(antecedentes_docentes_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_antecedentes_docentes}")
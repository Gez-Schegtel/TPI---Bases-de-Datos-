import csv
import random
from faker import Faker

# Inicializar Faker en español
faker = Faker('es_ES')

# Nombre del archivo CSV con los datos de Actividades_y_Antecedentes
archivo_actividades = 'actividades_y_antecedentes.csv'

# Leer los DNIs de la tabla Actividades_y_Antecedentes
dni_list = []
with open(archivo_actividades, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(int(row['dni']))

# Número de registros a generar
num_records = 100

# Verificar que hay suficientes registros en la tabla
if len(dni_list) < num_records:
    raise ValueError(f"La tabla '{archivo_actividades}' no contiene suficientes registros.")

# Generar datos para la tabla Antecedentes_Extension_Universitaria
extension_data = []
for _ in range(num_records):
    desde_date = faker.date_between(start_date='-20y', end_date='-1y')  # Fecha desde hace 20 años hasta hace 1 año
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d')  # Fecha hasta desde la fecha desde hasta ayer
    extension_data.append({
        'acciones': faker.catch_phrase(),
        'cargo': faker.job(),
        'dedicacion': faker.random_element(elements=('Investigación', 'Docencia', 'Gestión')),
        'dni': random.choice(dni_list),
        'desde': desde_date,
        'hasta': hasta_date,
        'id_antecedente': faker.unique.random_int(min=1, max=1000)
    })

# Nombre del archivo CSV para la tabla Antecedentes_Extension_Universitaria
archivo_extension = 'antecedentes_extension_universitaria.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_extension = ['acciones', 'cargo', 'dedicacion', 'dni', 'desde', 'hasta', 'id_antecedente']

# Crear y escribir los datos en el archivo CSV
with open(archivo_extension, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_extension)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(extension_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_extension}")
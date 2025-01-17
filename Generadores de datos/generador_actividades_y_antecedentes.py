import csv
import random
from faker import Faker
from faker.exceptions import UniquenessException

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

# Generar datos para la tabla Actividades_y_Antecedentes
actividades_data = []
for _ in range(num_records):

    # Intentar generar valores únicos con múltiples intentos
    max_attempts = 100000
    for _ in range(max_attempts):
        try:
            id_antecedente = faker.unique.random_int(min=1, max=num_records)
            break
        except UniquenessException:
            faker.unique.clear() # Es necesario "reiniciar el generador" cuando hay alguna falla
    else:
        raise Exception("No se pudieron generar valores únicos después de múltiples intentos.")

    desde_date = faker.date_between(start_date='-20y', end_date='-1y')  # Fecha desde hace 20 años hasta hace 1 año
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d')  # Fecha hasta desde la fecha desde hasta ayer
    actividades_data.append({
        'dedicacion': faker.random_element(elements=('Investigación', 'Docencia', 'Gestión')),
        'dni': random.choice(dni_list),
        'desde': desde_date,
        'hasta': hasta_date,
        'id_antecedente': id_antecedente
    })

# Nombre del archivo CSV para la tabla Actividades_y_Antecedentes
archivo_actividades = 'actividades_y_antecedentes.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_actividades = ['dedicacion', 'dni', 'desde', 'hasta', 'id_antecedente']

# Crear y escribir los datos en el archivo CSV
with open(archivo_actividades, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_actividades)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(actividades_data)  # Escribir los datos

print(f"{len(actividades_data)} registros generados y exportados a {archivo_actividades}")

import csv
import random
from faker import Faker

# Inicializar Faker en español (aunque no hace falta en este caso especificar el idoma porque vamos a generar solamente números en este programa).
fake = Faker('es_ES')

# Nombre del archivo CSV con los datos de Profesores
archivo_profesores = 'profesores.csv'

# Número de registros a generar
num_records = 1500

# Leer los DNI del archivo de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(row['dni'])

# Comprobar que se leyeron suficientes DNIs
if len(dni_list) < num_records:
    raise ValueError("El archivo 'profesores.csv' no contiene suficientes registros de DNI.")

# Seleccionar 50 DNI únicos para la tabla Seguro_de_Vida (no debería ser necesario porque se supone que ya son únicos)
dni_list = random.sample(dni_list, num_records)

# Generar datos para la tabla Seguro_de_Vida
# ¡Atenión! No controlamos "UniquenessException" porque los registros a generar no son muchos.
seguro_vida_data = []
idsv_set = set()  # Conjunto para asegurar unicidad de idsv. Es para usar después con "zip".

while len(idsv_set) < num_records:
    idsv_set.add(fake.unique.random_int(min=1, max=5000))

for idsv, dni in zip(idsv_set, dni_list):
    seguro_vida_data.append({
        'idsv': idsv,
        'dni': dni
    })

# Nombre del archivo CSV para la tabla Seguro_de_Vida
archivo_seguro_vida = 'seguro_de_vida.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_seguro_vida = ['idsv', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_seguro_vida, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_seguro_vida)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(seguro_vida_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_seguro_vida}")
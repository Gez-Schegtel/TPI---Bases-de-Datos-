import csv
import random
from faker import Faker

# Inicializar Faker en español
fake = Faker('es_ES')

# Nombre del archivo CSV con los datos de Profesores
archivo_profesores = 'profesores.csv'

# Leer los DNI del archivo de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(int(row['dni']))

# Número de registros a generar
num_records = 50

# Comprobar que se leyeron suficientes DNIs
if len(dni_list) < num_records:
    raise ValueError("El archivo 'profesores.csv' no contiene suficientes registros de DNI.")

# Seleccionar 50 DNI únicos para la tabla Obra_Social
dni_list = random.sample(dni_list, num_records)

# Generar datos para la tabla Obra_Social
# ¡Atenión! No controlamos "UniquenessException" porque los registros a generar no son muchos.
obra_social_data = []
idos_set = set()  # Conjunto para asegurar unicidad de idos. Es para usar después con "zip".
while len(idos_set) < num_records:
    idos_set.add(fake.unique.random_int(min=1, max=1000))

#idos_list = list(idos_set)  # Convertir el conjunto a lista para iterar. ¡Atención! No es necesario, podemos usar el "set" directamente.

for dni, idos in zip(dni_list, idos_set):
    obra_social_data.append({
        'dni': dni,
        'idos': idos
    })

# Nombre del archivo CSV para la tabla Obra_Social
archivo_obra_social = 'obra_social.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_obra_social = ['dni', 'idos']

# Crear y escribir los datos en el archivo CSV
with open(archivo_obra_social, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_obra_social)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(obra_social_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_obra_social}")

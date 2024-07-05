import csv
import random
from faker import Faker

# Inicializar Faker en español (aunque no hace falta en este caso especificar el idoma porque vamos a generar solamente números en este programa).
fake = Faker('es_ES')

# Nombre del archivo CSV con los datos de Profesores
archivo_profesores = 'profesores.csv'

# Leer los DNI del archivo de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(row['dni'])

# Número de registros a generar
num_records = 20

# Comprobar que se leyeron suficientes DNIs
if len(dni_list) < num_records:
    raise ValueError("El archivo 'profesores.csv' no contiene suficientes registros de DNI.")

# Generar datos para la tabla Seguro_de_Vida
# ¡Atenión! No controlamos "UniquenessException" porque los registros a generar no son muchos.
seguro_vida_data = []

for dni in dni_list:
    num_idsv = random.randint(1, 3) # Generamos entre 1 y 3 "idsv" por cada DNI.
    for _ in range(num_idsv):
        seguro_vida_data.append({
            'dni': dni,
            'idsv': fake.unique.random_int(min=1, max=50000) # El valor máximo puede convertirse en un inconveniente si hay muchos "dni's". Controlar.
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

print(f"{len(seguro_vida_data)} registros generados y exportados a {archivo_seguro_vida}")
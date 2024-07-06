import csv
import random
from faker import Faker
from faker.exceptions import UniquenessException

# Inicializar Faker en español
fake = Faker('es_ES')

# Número de registros a generar
num_records = 20

# Nombre del archivo CSV con los datos de Profesores
archivo_profesores = 'profesores.csv'

# Leer los DNI del archivo de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(int(row['dni']))

# Comprobar que se leyeron suficientes DNIs
if len(dni_list) < num_records:
    raise ValueError("El archivo 'profesores.csv' no contiene suficientes registros de DNI.")

# Generar datos para la tabla Obra_Social
obra_social_data = []

for _ in range(num_records):

    # Intentar generar valores únicos con múltiples intentos
    max_attempts = 100000
    for _ in range(max_attempts):
        try:
            idos = fake.unique.random_int(min=1000, max=num_records*1000)
            break
        except UniquenessException:
            fake.unique.clear() # Es necesario "reiniciar el generador" cuando hay alguna falla
    else:
        raise Exception("No se pudo generar valores únicos después de múltiples intentos.")

    obra_social_data.append({
        'dni': random.choice(dni_list), # Hacemos un random.choice así podemos modelar el hecho de un mismo "dni" pueda tener más de una obra social.
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

print(f"{len(obra_social_data)} registros generados y exportados a {archivo_obra_social}")

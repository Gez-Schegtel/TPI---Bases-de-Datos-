import csv
import random
from faker import Faker

# Inicializar Faker en español
fake = Faker('es_ES')

# Nombre del archivo CSV con los datos de Obra Social
archivo_obra_social = 'obra_social.csv'

# Leer los idos del archivo de Obra Social
idos_list = []
with open(archivo_obra_social, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        idos_list.append(int(row['idos']))

# Número de registros a generar
num_records = 20

# Comprobar que se leyeron suficientes idos
if len(idos_list) < num_records:
    raise ValueError("El archivo 'obra_social.csv' no contiene suficientes registros de idos.")

# Generar datos para la tabla Dependencia
dependencia_data = []
obra_social_data = ['INSSSEP', 'ACCORD']

for _ in range(num_records):
    dependencia_data.append({
        'nombre': fake.company(),
        'cargo': fake.job(),
        'año_alta': fake.date_between(start_date='-20y', end_date='today').strftime('%Y-%m-%d'),
        'obra_social': random.choice(obra_social_data),
        'observacion': fake.sentence(),
        'idos': random.choice(idos_list)
    })

# Nombre del archivo CSV para la tabla Dependencia
archivo_dependencia = 'dependencia.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_dependencia = ['nombre', 'cargo', 'año_alta', 'obra_social', 'observacion', 'idos']

# Crear y escribir los datos en el archivo CSV
with open(archivo_dependencia, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_dependencia)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(dependencia_data)  # Escribir los datos

print(f"{len(dependencia_data)} registros generados y exportados a {archivo_dependencia}")

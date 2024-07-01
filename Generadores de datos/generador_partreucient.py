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

# Generar datos para la tabla Participacion_Reuniones_Cientificas
participacion_data = []
for _ in range(num_records):
    participacion_data.append({
        'titulo': faker.catch_phrase(),
        'participacion': faker.random_element(elements=('Orador', 'Asistente', 'Moderador')),
        'fecha': faker.date_between(start_date='-5y', end_date='today'),  # Fecha en los últimos 5 años hasta hoy
        'dni': random.choice(dni_list)
    })

# Nombre del archivo CSV para la tabla Participacion_Reuniones_Cientificas
archivo_participacion = 'participacion_reuniones_cientificas.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_participacion = ['titulo', 'participacion', 'fecha', 'dni']

# Crear y escribir los datos en el archivo CSV
with open(archivo_participacion, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_participacion)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(participacion_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_participacion}")

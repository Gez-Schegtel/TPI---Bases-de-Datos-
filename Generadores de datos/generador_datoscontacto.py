import csv
import random
from faker import Faker
fake = Faker('es_ES')

num_records = 200

archivo_profesores = 'profesores.csv'

dni_list = list()
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(row['dni'])

if len(dni_list) < num_records:
    raise ValueError("No hay suficientes registros en el archivo 'profesores.csv'.")


dni_list = random.sample(dni_list, num_records)
contactos_data = []

for _ in range(num_records):
    contactos_data.append({
        'email': fake.unique.email(),
        'tipo_email': fake.random_element(elements=('Personal', 'Trabajo')),
        'telefono': fake.phone_number(),
        'tipo_telefono': fake.random_element(elements=('Personal', 'Trabajo')),
        'id_contacto': fake.unique.random_int(min=1, max=1000),
        'dni': random.choice(dni_list)
    })

archivo_contactos = 'datos_contacto.csv'

cabecera_contactos = ['email', 'tipo_email', 'telefono', 'tipo_telefono', 'id_contacto', 'dni']

with open(archivo_contactos, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabecera_contactos)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(contactos_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_contactos}")
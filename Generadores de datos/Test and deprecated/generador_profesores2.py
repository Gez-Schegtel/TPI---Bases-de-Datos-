"""
¡Atención! Este programa puede llegar a ocupar mucha memoria RAM.
"""

import csv
from faker import Faker
import random
from faker.exceptions import UniquenessException

# Crear una instancia de Faker
fake = Faker('es_ES')  # Usar el local de España para datos más realistas en español

# Lista de barrios predefinidos (puedes modificarla según tus necesidades)
barrios = ['Centro', 'Norte', 'Sur', 'Este', 'Oeste', 'Barrio 1', 'Barrio 2', 'Barrio 3']
domicilios = ['Laboral', 'Personal', 'Otro']
estados_civiles = ['Soltero', 'Casado', 'Divorciado', 'Viudo']
sexos = ['F', 'M']
pisos = [None, '1A', '2B', '3C', '4D']

# Nombre del archivo CSV
archivo_profesores = 'profesores2.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_profesores = [
    'dni', 'tipo_domicilio', 'fecha_nacimiento', 'nombre', 'apellido', 'localidad', 
    'departamento', 'provincia', 'numero', 'piso', 'codigo_postal', 'calle', 
    'edad', 'cuil', 'inicio_actividad', 'estado_civil', 'sexo', 'barrio', 'legajo'
]

# Cantidad de registros a generar
cantidad_registros = 4500000

# Lista en la que se almacenarán los datos para luego escribirlos en el archivo CSV
datos_profesores = []

# Generar datos aleatorios
for _ in range(cantidad_registros):
    # Intentar generar valores únicos con múltiples intentos
    max_attempts = 100000
    for _ in range(max_attempts):
        try:
            dni = fake.unique.random_int(min=10000000, max=99999999)
            cuil = fake.unique.random_int(min=20000000000, max=29999999999)
            legajo = fake.unique.random_int(min=1000, max=9999999)
            break
        except UniquenessException:
            fake.unique.clear() # Es necesario "reiniciar el generador" cuando hay alguna falla
    else:
        raise Exception("No se pudieron generar valores únicos después de múltiples intentos.")

    datos_profesores.append({
        'dni': dni,
        'tipo_domicilio': random.choice(domicilios),
        'fecha_nacimiento': fake.date_of_birth(minimum_age=22, maximum_age=65),
        'nombre': fake.first_name(),
        'apellido': fake.last_name(),
        'localidad': fake.city(),
        'departamento': fake.state(),
        'provincia': fake.state(),
        'numero': random.randint(1, 9999),
        'piso': random.choice(pisos),
        'codigo_postal': random.randint(1000, 9999),
        'calle': fake.street_name(),
        'edad': random.randint(22, 65),
        'cuil': cuil,
        'inicio_actividad': fake.date_between(start_date='-30y', end_date='today'),
        'estado_civil': random.choice(estados_civiles),
        'sexo': random.choice(sexos),
        'barrio': random.choice(barrios),  # Utilizar la lista de barrios predefinidos
        'legajo': legajo
    })

# Crear y escribir los datos en el archivo CSV
with open(archivo_profesores, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_profesores)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(datos_profesores)  # Escribir los datos

print(f"{cantidad_registros} registros generados y exportados a {archivo_profesores}")

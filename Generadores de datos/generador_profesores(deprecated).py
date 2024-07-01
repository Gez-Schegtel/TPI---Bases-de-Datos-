'''
¡Atención! Este código genera valores repetidos de DNI, CUIL y legajo.
'''

import csv
from faker import Faker
import random

# Crear una instancia de Faker
fake = Faker('es_ES')  # Usar el local de España para datos más realistas en español

# Lista de barrios predefinidos (puedes modificarla según tus necesidades)
barrios = ['Centro', 'Norte', 'Sur', 'Este', 'Oeste', 'Barrio 1', 'Barrio 2', 'Barrio 3']

# Generar datos aleatorios
def generar_datos():
    dni = random.randint(10000000, 99999999)
    tipo = random.choice(['Full-time', 'Part-time'])
    fecha_nacimiento = fake.date_of_birth(minimum_age=22, maximum_age=65)
    nombre = fake.first_name()
    apellido = fake.last_name()
    localidad = fake.city()
    departamento = fake.state()
    provincia = fake.state()
    numero = random.randint(1, 9999)
    piso = random.choice([None, '1A', '2B', '3C', '4D'])
    codigo_postal = random.randint(1000, 9999)
    calle = fake.street_name()
    edad = random.randint(22, 65)
    cuil = random.randint(20000000000, 29999999999)
    inicio_actividad = fake.date_between(start_date='-30y', end_date='today')
    estado_civil = random.choice(['Soltero', 'Casado', 'Divorciado', 'Viudo'])
    sexo = random.choice(['M', 'F'])
    barrio = random.choice(barrios)  # Utilizar la lista de barrios predefinidos
    legajo = random.randint(1000, 9999)

    # Devolver valores, manejando el caso del piso como cadena vacía si es None
    return (
        dni, tipo, fecha_nacimiento, nombre, apellido, localidad, departamento, 
        provincia, numero, piso if piso else '', codigo_postal, calle, edad, 
        cuil, inicio_actividad, estado_civil, sexo, barrio, legajo
    )

# Nombre del archivo CSV
archivo_csv = 'profesores.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras = [
    'dni', 'tipo', 'fecha_nacimiento', 'nombre', 'apellido', 'localidad', 
    'departamento', 'provincia', 'numero', 'piso', 'codigo_postal', 'calle', 
    'edad', 'cuil', 'inicio_actividad', 'estado_civil', 'sexo', 'barrio', 'legajo'
]

# Cantidad de registros a generar
cantidad_registros = 50000

# Crear y escribir los datos en el archivo CSV
with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(cabeceras)  # Escribir las cabeceras

    for _ in range(cantidad_registros):
        datos = generar_datos()
        writer.writerow(datos)

print(f"Datos generados y exportados a {archivo_csv}")

import csv
import random
from faker import Faker
from faker.exceptions import UniquenessException

# Crear una instancia de Faker
fake = Faker('es_ES')  # Para datos realistas en español

# Número de registros a generar.
num_records = 20

# Archivos CSV de entrada
archivo_profesores = 'profesores.csv'
archivo_obra_social = 'obra_social.csv'
archivo_seguro_vida = 'seguro_de_vida.csv'

# Leer los datos de Profesores
dni_list = []
with open(archivo_profesores, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni_list.append(int(row['dni']))  # Crea una lista con todos los dni's.

# Comprobar que se leyeron suficientes DNIs
if len(dni_list) < num_records:
    raise ValueError("El archivo 'profesores.csv' no contiene suficientes registros de DNI.")

# Leer los datos de Obra Social y Seguro de Vida y construir un diccionario que relacione dni, idos, y idsv
dni_to_others = {dni: {'idos': set(), 'idsv': set()} for dni in dni_list}

with open(archivo_obra_social, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni = int(row['dni'])
        idos = int(row['idos'])
        if dni in dni_to_others:
            dni_to_others[dni]['idos'].add(idos)

with open(archivo_seguro_vida, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        dni = int(row['dni'])
        idsv = int(row['idsv'])
        if dni in dni_to_others:
            dni_to_others[dni]['idsv'].add(idsv)

# Filtrar dni_list para solo incluir aquellos que tienen al menos un idos o idsv
dni_list = [dni for dni in dni_list if dni_to_others[dni]['idos'] or dni_to_others[dni]['idsv']]

# Generar datos para la tabla Familiar
familiar_data = []
parentescos = ['Padre', 'Madre', 'Hermano', 'Hermana', 'Esposo', 'Esposa', 'Hijo', 'Hija']
tipo_documentos = ['DNI', 'Pasaporte', 'CI']

for _ in range(num_records):
    # Intentar generar valores únicos con múltiples intentos
    max_attempts = 10000
    for _ in range(max_attempts):
        try:
            nro_documento = fake.unique.random_int(min=10000000, max=99999999)
            break
        except UniquenessException:
            fake.unique.clear()
    else:
        raise Exception("No se pudieron generar valores únicos después de múltiples intentos")

    dni = random.choice(dni_list)
    idos = random.choice(list(dni_to_others[dni]['idos'])) if dni_to_others[dni]['idos'] else None  # Puede ser None si no hay idos disponibles
    idsv = random.choice(list(dni_to_others[dni]['idsv'])) if dni_to_others[dni]['idsv'] else None  # Puede ser None si no hay idsv disponibles

    # Convertir None a 'NULL' para evitar espacios vacíos en el archivo CSV
    # Este paso es superimportante, porque si no está, se escribe ",," para cuando las claves son NULL y el script generará un archivo que luego no funciona con el script de carga de datos.
    idos = 'NULL' if idos is None else idos
    idsv = 'NULL' if idsv is None else idsv

    familiar_data.append({
        'apellido': fake.last_name(),
        'parentesco': random.choice(parentescos),
        'tipo_documento': random.choice(tipo_documentos),
        'nro_documento': nro_documento,
        'nombre': fake.first_name(),
        'fecha_nacimiento': fake.date_of_birth(minimum_age=0, maximum_age=100),
        'idos': idos,
        'dni': dni,
        'idsv': idsv,
        'porcentaje': round(random.uniform(10, 100), 2),  # Valor de porcentaje entre 10 y 100
        'domicilio': fake.street_address()  # Reemplazar saltos de línea con espacios
    })

# Nombre del archivo CSV para la tabla Familiar
archivo_familiar = 'familiar.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_familiar = [
    'apellido', 'parentesco', 'tipo_documento', 'nro_documento', 'nombre', 
    'fecha_nacimiento', 'idos', 'dni', 'idsv', 'porcentaje', 'domicilio'
]

# Crear y escribir los datos en el archivo CSV
with open(archivo_familiar, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_familiar)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(familiar_data)  # Escribir los datos

print(f"{len(familiar_data)} registros generados y exportados a {archivo_familiar}")
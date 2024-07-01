import csv
import random 
from faker import Faker

# Inicializo Faker en español
fake = Faker('es_ES')

# Nombre del archivo csv con datos del seguro de vida
archivo_seguro_vida = 'seguro_de_vida.csv'

# Número de archivos a generar
num_records = 50

# Leemos los idsv del archivo 'seguro_de_vida.csv"
idsv_set = set()
with open(archivo_seguro_vida, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        idsv_set.add(int(row['idsv']))

# Comprobar que hay suficientes idsv
if len(idsv_set) < num_records:
    raise ValueError("El archivo 'seguro_de_vida.csv' no tiene suficientes registros de idsv.")

# Generar datos para la tabla de Datos_del_Empleador
datos_del_empleador_data = []
cuit_cuil_set = set()

while len(cuit_cuil_set) < num_records:
    cuit_cuil_set.add(fake.unique.random_int(min=10**10, max=10**11 - 1))

for idsv, cuit_cuil in zip(idsv_set, cuit_cuil_set):
    datos_del_empleador_data.append({
        'cuit_cuil': cuit_cuil,
        'codigo_postal': fake.postcode(),
        'provincia': fake.state(),
        'localidad': fake.state(),
        'departamento': fake.city(),
        'numero': fake.random_int(min=1, max=9),
        'piso': fake.building_number(),
        'calle': fake.street_name(),
        'razon_social': fake.company(),
        'idsv': idsv
    })

# Nombre del archivo CSV para la tabla Datos_del_Empleador
archivo_datos_empleador = 'datos_empleador.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_empleador = ['codigo_postal', 'provincia', 'localidad', 'departamento', 'numero', 'piso', 'calle', 'razon_social', 'cuit_cuil', 'idsv']

# Crear y escribir los datos en el archivo CSV
with open(archivo_datos_empleador, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_empleador)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(datos_del_empleador_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_datos_empleador}")

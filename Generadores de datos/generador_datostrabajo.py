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
num_records = 100

# Comprobar que se leyeron suficientes idos
if len(idos_list) < num_records:
    raise ValueError("El archivo 'obra_social.csv' no contiene suficientes registros de idos.")

# Seleccionar 100  DNI únicos para la tabla Obra_Social
idos_list = random.sample(idos_list, num_records)

# Generar datos para la tabla Datos_Trabajo
datos_trabajo_data = []
tipo_personal_data = ['Docente', 'No Docente']
caracter_data = ['Permanente', 'Contratado']

for idos in idos_list:
    datos_trabajo_data.append({
        'tipo_personal': random.choice(tipo_personal_data),
        'caracter': random.choice(caracter_data),
        'presta_servicio_utn': fake.boolean(),
        'idos': idos
    })

# Nombre del archivo CSV para la tabla Datos_Trabajo
archivo_datos_trabajo = 'datos_trabajo.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_datos_trabajo = ['tipo_personal', 'caracter', 'presta_servicio_utn', 'idos']

# Crear y escribir los datos en el archivo CSV
with open(archivo_datos_trabajo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_datos_trabajo)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(datos_trabajo_data)  # Escribir los datos

print(f"{num_records} registros generados y exportados a {archivo_datos_trabajo}")

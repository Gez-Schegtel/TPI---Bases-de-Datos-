import csv
import random
from faker import Faker

# Inicializar Faker en español
faker = Faker('es_ES')

# Nombre del archivo CSV con los datos de Declaracion_Jurada
archivo_declaracion_jurada = 'declaracion_jurada.csv'

# Leer los iddj del archivo de Declaracion_Jurada
iddj_list = []
with open(archivo_declaracion_jurada, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        iddj_list.append(int(row['iddj']))

# Generar datos para la tabla Tareas_No_Estatales
tareas_no_estatales_data = []
for iddj in iddj_list:
    tareas_no_estatales_data.append({
        'fecha_ingreso': faker.date_this_decade(),
        'lugar_presta_servicio': faker.company(),
        'autonomia': random.choice(['Sí', 'No']),
        'relacion_dependencia': random.choice(['Dependiente', 'Independiente']),
        'funcion': faker.job(),
        'iddj': iddj
    })

# Nombre del archivo CSV para la tabla Tareas_No_Estatales
archivo_tareas_no_estatales = 'tareas_no_estatales.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_tareas_no_estatales = ['fecha_ingreso', 'lugar_presta_servicio', 'autonomia',
                                 'relacion_dependencia', 'funcion', 'iddj']

# Crear y escribir los datos en el archivo CSV
with open(archivo_tareas_no_estatales, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_tareas_no_estatales)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(tareas_no_estatales_data)  # Escribir los datos

print(f"{len(iddj_list)} registros generados y exportados a {archivo_tareas_no_estatales}")

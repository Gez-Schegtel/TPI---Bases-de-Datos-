import csv
import random
from faker import Faker

# Inicializar Faker en español
faker = Faker('es_ES')

# Nombre del archivo CSV con los datos de Actividades_y_Antecedentes
archivo_actividades = 'actividades_y_antecedentes.csv'

# Leer los DNIs, dedicaciones y id_antecedente de la tabla Actividades_y_Antecedentes
antecedentes_list = []
with open(archivo_actividades, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        antecedentes_list.append({
            'dni': int(row['dni']),
            'dedicacion': row['dedicacion'],
            'id_antecedente': int(row['id_antecedente'])
        })

# Número de registros a generar
num_records = 20

# Verificar que hay suficientes registros en la tabla
if len(antecedentes_list) < num_records:
    raise ValueError(f"La tabla '{archivo_actividades}' no contiene suficientes registros.")

# Generar datos para la tabla Actividad_e_Investigacion
actividad_investigacion_data = []
pares_generados = set()

while len(actividad_investigacion_data) < num_records:
    desde_date = faker.date_between(start_date='-20y', end_date='-1y')
    hasta_date = faker.date_between(start_date=desde_date, end_date='-1d')
    antecedente = random.choice(antecedentes_list)
    
    # Crear un par de (dni, id_antecedente) para verificar duplicados
    par = (antecedente['dni'], antecedente['id_antecedente'])
    
    if par not in pares_generados:
        pares_generados.add(par)
        actividad_investigacion_data.append({
            'categoria': faker.word(),
            'area_principal': faker.catch_phrase(),
            'dedicacion': antecedente['dedicacion'],
            'dni': antecedente['dni'],
            'desde': desde_date,
            'hasta': hasta_date,
            'id_antecedente': antecedente['id_antecedente']
        })

# Nombre del archivo CSV para la tabla Actividad_e_Investigacion
archivo_actividad_investigacion = 'actividad_e_investigacion.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_actividad_investigacion = ['categoria', 'area_principal', 'dedicacion', 'dni', 'desde', 'hasta', 'id_antecedente']

# Crear y escribir los datos en el archivo CSV
with open(archivo_actividad_investigacion, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_actividad_investigacion)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(actividad_investigacion_data)  # Escribir los datos

print(f"{len(actividad_investigacion_data)} registros generados y exportados a {archivo_actividad_investigacion}")

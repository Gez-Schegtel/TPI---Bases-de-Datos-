import csv
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
        iddj_list.append(row['iddj'])

# Generar datos para la tabla Datos_de_Cargo
datos_cargo_data = []
for iddj in iddj_list:
    datos_cargo_data.append({
        'cargo': faker.job(),
        'iddj': iddj,
        'calle': faker.street_name(),
        'provincia': faker.state(),
        'reparticion': faker.company(),
        'dependencia': faker.company_suffix(),
        'cumple_horarios': faker.random_element(elements=('Sí', 'No')),
        'organismo': faker.company(),
        'localidad_cargo': faker.city(),
        'numero': faker.random_number(digits=3)
    })

# Nombre del archivo CSV para la tabla Datos_de_Cargo
archivo_datos_cargo = 'datos_de_cargo.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras_datos_cargo = ['cargo', 'iddj', 'calle', 'provincia', 'reparticion', 'dependencia',
                         'cumple_horarios', 'organismo', 'localidad_cargo', 'numero']

# Crear y escribir los datos en el archivo CSV
with open(archivo_datos_cargo, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=cabeceras_datos_cargo)
    writer.writeheader()  # Escribir las cabeceras
    writer.writerows(datos_cargo_data)  # Escribir los datos

print(f"{len(datos_cargo_data)} registros generados y exportados a {archivo_datos_cargo}")

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

# Generar datos aleatorios
def generar_datos():
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

    tipo_domicilio = random.choice(domicilios)
    fecha_nacimiento = fake.date_of_birth(minimum_age=22, maximum_age=65)
    nombre = fake.first_name()
    apellido = fake.last_name()
    localidad = fake.city()
    departamento = fake.state()
    provincia = fake.state()
    numero = random.randint(1, 9999)
    piso = random.choice(pisos)
    codigo_postal = random.randint(1000, 9999)
    calle = fake.street_name()
    edad = random.randint(22, 65)
    inicio_actividad = fake.date_between(start_date='-30y', end_date='today')
    estado_civil = random.choice(estados_civiles)
    sexo = random.choice(sexos)
    barrio = random.choice(barrios)  # Utilizar la lista de barrios predefinidos

    # Devolver valores, manejando el caso del piso como cadena vacía si es None
    return (
        dni, tipo_domicilio, fecha_nacimiento, nombre, apellido, localidad, departamento, 
        provincia, numero, piso if piso else '', codigo_postal, calle, edad, 
        cuil, inicio_actividad, estado_civil, sexo, barrio, legajo
    )

# Nombre del archivo CSV
archivo_csv = 'profesores.csv'

# Cabeceras de las columnas en el archivo CSV
cabeceras = [
    'dni', 'tipo_domicilio', 'fecha_nacimiento', 'nombre', 'apellido', 'localidad', 
    'departamento', 'provincia', 'numero', 'piso', 'codigo_postal', 'calle', 
    'edad', 'cuil', 'inicio_actividad', 'estado_civil', 'sexo', 'barrio', 'legajo'
]

# Cantidad de registros a generar
cantidad_registros = 4500000

# Crear y escribir los datos en el archivo CSV
with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(cabeceras)  # Escribir las cabeceras

    for _ in range(cantidad_registros):
        datos = generar_datos()
        writer.writerow(datos)

print(f"{cantidad_registros} registros generados y exportados a {archivo_csv}")

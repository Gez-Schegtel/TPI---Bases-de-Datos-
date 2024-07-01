# TPI---Bases-de-Datos-
Trabajo práctico integrador de la cátedra de Bases de Datos - UTN Facultad Regional Resistencia.
```ascii
 _______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
## Nuestra elección de SGBD
mariadb  Ver 15.1 Distrib 10.6.18-MariaDB, for debian-linux-gnu (x86_64) using  EditLine wrapper

## Generación de datos
Entrar a la carpeta "Generadores de datos", la misma se encuentra bajo el mismo directorio que este archivo. Luego ejecutar el script "generador_total.sh". Esto nos permitirá tener todos los datos necesarios para realizar consultas sobre la base de datos.

## Creación de esquemas
Con el script "database_creation_script.sql" se crean todas las relaciones

## Carga de datos
Hay un script para cargar todos los datos que estén en los archivos CSV bajo el directorio "Generador de datos". Sin embargo, hay que ajustar las dirección en ´LOAD DATA LOCAL INFILE´ para que funcione.

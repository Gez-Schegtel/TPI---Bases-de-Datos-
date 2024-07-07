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

## Creación de esquemas
Con el script "database_creation_script.sql" que se encuentra bajo el directorio 'Creación y carga de datos' se crean todas las relaciones con sus respectivas restricciones.

La base de datos resultante de la ejecución del mismo se llamará `TPI`.

## Carga de datos
Para que la base de datos posea información que permita hacer consultas, se pueden utilizar los archivos CSV que están en el directorio 'Generadores de datos'.

Estos archivos se pueden importar con el script `load_data.sql` o gráficamente haciendo uso de la herramientas de administración y diseño de bases de datos de su preferencia.

> ¡Atención! Para que el script `load_data.sql` funcione correctamente, es necesario ajustar la dirección a los archivos CSV para que coincida con el directorio donde se han alojado al descargar o clonar este repositorio.

## Generación de datos
También existe la opción de crear datos aleatorios, ajustando la cantidad de filas a generar para cada tabla. Para conseguirlo se puede ejecutar el script 'generador_total.sh', ubicado bajo el directorio 'Generadores de datos'. 

> Es necesario tener Python y la librería `Faker` para que el script generador funcione.

## Información extra
* Para el desarrollo de este trabajamos utilizamos el software de administración de bases de datos `DBeaver`.
* Los códigos en Python fueron desarrollados y testeados en entornos GNU/Linux Ubuntu y Debian.
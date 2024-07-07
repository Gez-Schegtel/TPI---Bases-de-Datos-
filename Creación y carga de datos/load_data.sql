
/*
 * 
 * ¡ATENCIÓN! Para que este script funcione correctamente, hay que ajustar la dirección a los archivos CSV.
 * 
 * LOAD DATA LOCAL INFILE '/dirección/.../archivo.csv'
 * 
 */

/* Selecciona la base de datos */
USE TPI;

/* Cargar datos desde los archivos CSV a las tablas correspondientes */
LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/profesores.csv'
INTO TABLE Profesores
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/obra_social.csv'
INTO TABLE Obra_Social
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/dependencia.csv'
INTO TABLE Dependencia
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/datos_trabajo.csv'
INTO TABLE Datos_Trabajo
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/seguro_de_vida.csv'
INTO TABLE Seguro_de_Vida
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/familiar.csv'
INTO TABLE Familiar
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/participacion_reuniones_cientificas.csv'
INTO TABLE Participacion_Reuniones_Cientificas
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/publicaciones.csv'
INTO TABLE Publicaciones
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/antecedentes_profesionales.csv'
INTO TABLE Antecedentes_Profesionales
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/titulos.csv'
INTO TABLE Titulos
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/idiomas.csv'
INTO TABLE Idiomas
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/cursos_y_conferencias.csv'
INTO TABLE Cursos_y_Conferencias
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/actividades_y_antecedentes.csv'
INTO TABLE Actividades_y_Antecedentes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/antecedentes_extension_universitaria.csv'
INTO TABLE Antecedentes_Extension_Universitaria
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/actividad_e_investigacion.csv'
INTO TABLE Actividad_e_Investigacion
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/antecedentes_docentes.csv'
INTO TABLE Antecedentes_Docentes
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/datos_empleador.csv'
INTO TABLE Datos_del_Empleador
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/datos_contacto.csv'
INTO TABLE Datos_de_Contacto
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/declaracion_jurada.csv'
INTO TABLE Declaracion_Jurada
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/carga_horaria.csv'
INTO TABLE Carga_Horaria
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/datos_de_cargo.csv'
INTO TABLE Datos_de_Cargo
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/pasividades.csv'
INTO TABLE Pasividades
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE '/home/juani/Descargas/TPI---Bases-de-Datos-/Generadores de datos/tareas_no_estatales.csv'
INTO TABLE Tareas_No_Estatales
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- Inserción de datos

INSERT INTO Profesores(dni, tipo_domicilio, fecha_nacimiento, nombre, apellido, localidad, departamento, provincia, numero, piso, codigo_postal, calle, edad, cuil, inicio_actividad, estado_civil, sexo, barrio, legajo) 
VALUES (23123125,'Particular','1987-02-12','Josefa','Miranda','Resistencia','San Fernando','Chaco',1029,'1',3500,'Perugorría',37,20231231253,'2020-03-12', 'Soltera', 'X','Barrio Itatí',45564) 

INSERT INTO Idiomas(idioma, nivel, certificacion, institucion, dni) 
VALUES ('Inglés','B2','Oxford','Oxford',23123125)

INSERT INTO Familiar(tipo_documento, nro_documento, nombre, apellido, parentesco, domicilio, fecha_nacimiento,dni)
VALUES ('DNI',40122321,'Pepe','Miranda','Hermano','Alvear 1234','1992-08-03',23123125)

INSERT INTO Datos_de_Contacto(id_contacto, email, tipo_email,tipo_telefono,telefono, dni)
VALUES(123, 'josefamiranda@gmail.com', 'gmail','particular',3624128128, 23123125)

INSERT INTO Obra_Social (dni,idos)
VALUES(23123125,12873)

--Modificacion de datos
UPDATE Profesores
SET legajo = legajo + 20000
WHERE codigo_postal >= 3500

UPDATE Datos_de_Contacto
SET id_contacto = id_contacto + 12034
WHERE dni >4000000 AND tipo_email = 'gmail'

UPDATE Dependencia
SET observacion = 'Observación actualizada'
WHERE idos IN (
    SELECT idos
    FROM Obra_Social
    WHERE dni = 44556677
);

UPDATE Profesores
SET departamento = 'Ciencias Sociales', codigo_postal = 12345
WHERE nombre = 'Juan' AND apellido = 'Pérez';

UPDATE Profesores
SET inicio_actividad = '2020-01-01'
WHERE dni IN (
    SELECT dni
    FROM Datos_Trabajo
    WHERE presta_servicio_utn = 'True'
);

 --Borrado de filas

DELETE FROM Dependencia
WHERE idos IN (
    SELECT idos
    FROM Obra_Social
    WHERE dni IN (
        SELECT dni
        FROM Profesores
        WHERE departamento = 'Matemáticas'
    )
);

DELETE FROM Cursos_y_Conferencias
WHERE institucion = 'UTN' AND desde >= '2020-01-01' AND hasta <= '2021-12-31';

DELETE FROM Antecedentes_Profesionales
WHERE dni IN (
    SELECT dni
    FROM Profesores
    WHERE edad > 60
)
AND empresa_anterior = 'Tomé & Asociados S.Coop.';

DELETE FROM Familiar
WHERE localidad = 'Córdoba' AND porcentaje < 10;

DELETE FROM Datos_del_Empleador
WHERE cuit_cuil = 20304050607 AND idsv NOT IN (
    SELECT idsv
    FROM Seguro_de_Vida
);

--Consultas SELECT


-- 1) Listado de docentes que viven en una provincia distinta de aquella en la que trabajan.
SELECT *
FROM Profesores p INNER JOIN Declaracion_Jurada dj ON p.dni = dj.dni INNER JOIN Datos_de_Cargo dc ON dc.iddj = dj.iddj
WHERE p.provincia <> dc.provincia;


-- 2) Listado de docentes que poseen títulos de posgrado y no realizan tareas de investigación
SELECT *
FROM Profesores p
WHERE p.dni IN (
    SELECT DISTINCT t.dni
    FROM Titulos t
    WHERE t.nivel LIKE 'Maestría' OR t.nivel LIKE 'Doctorado'
)
AND p.dni NOT IN (
    SELECT DISTINCT a.dni
    FROM Actividad_e_Investigacion a
);

--3)Informar promedio de edad de los docentes que poseen más de 10 años de antecedentes como docentes:

SELECT AVG(p.edad) AS promedio_edad
FROM Profesores p
WHERE p.dni IN (
    SELECT ap.dni
    FROM Antecedentes_Docentes ap
    WHERE DATEDIFF(CURDATE(), ap.desde) >= 3650  -- 10 años en días aproximadamente
);
-- 4) Listar DNI y nombre de los docentes que presentaron más de un cargo docente en las declaraciones juradas de los últimos 3 años
 
-- 5) Listado de docentes cuya carga horaria supera las 20 horas semanales, en función de la última declaración jurada presentada:
SELECT p.dni
FROM Profesores p NATURAL JOIN Declaracion_Jurada d
WHERE d.fecha = (
    SELECT MAX(c.horario)
    FROM Carga_Horaria c
    WHERE
)

-- 6) Apellido y nombre de aquellos docentes que poseen la máxima cantidad de cargos docentes actualmente:

-- 7) Listado de docentes solteros/as (sin esposa/o e/o hijos a cargo en la obra social):
SELECT *
FROM Profesores p
WHERE p.dni NOT IN (
    SELECT DISTINCT f.dni
    FROM Familiar f
    WHERE f.parentesco IN ('Esposa', 'Esposo', 'Hijo', 'Hija')
);


-- 8) Cantidad de docentes cuyos hijos a cargo son todos menores de 10 años:
SELECT COUNT(DISTINCT p.dni) AS cantidad
FROM Profesores p
WHERE p.dni IN (
    SELECT DISTINCT f.dni
    FROM Familiar f
    WHERE YEAR(f.fecha_nacimiento) > YEAR(CURDATE()) - 10
);


-- 9) Informar aquellos docentes que posean alguna persona del grupo familiar a cargo en la obra social que no es beneficiario del seguro de vida obligatorio:

--10) Informar la cantidad de individuos asegurados por provincia:

SELECT d.provincia, COUNT(DISTINCT sv.dni) AS cantidad_individuos
FROM Datos_del_Empleador d
JOIN Seguro_de_Vida sv ON d.idsv = sv.idsv
GROUP BY d.provincia;

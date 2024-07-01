
-- Inserción de datos

INSERT INTO Profesores(dni, tipo_domicilio, fecha_nacimiento, nombre, apellido, localidad, departamento, provincia, numero, piso, codigo_postal, calle, edad, cuil, inicio_actividad, estado_civil, sexo, barrio, legajo) 
VALUES (23123125,'Particular','1987-02-12','Josefa','Miranda','Resistencia','San Fernando','Chaco',1029,'1',3500,'Perugorria',37,20231231253,'2020-03-12', 'Soltera', 'X','Barrio Itatí',45564) 

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


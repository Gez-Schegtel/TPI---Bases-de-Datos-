
/* Inserción de datos. */

INSERT INTO Profesores(dni, tipo_domicilio, fecha_nacimiento, nombre, apellido, localidad, departamento, provincia, numero, piso, codigo_postal, calle, edad, cuil, inicio_actividad, estado_civil, sexo, barrio, legajo) 
VALUES (23123125,'Particular','1987-02-12','Julio','Cortázar','París','Lingüística','Montmartre',1029,'1',3500,'Bordeaux',37,20231231253,'2020-03-12', 'Soltero', 'M','Parisiennes',45564);


INSERT INTO Familiar(apellido, parentesco, tipo_documento, nro_documento, nombre, fecha_nacimiento, idos, dni, idsv, porcentaje, domicilio)
VALUES ('Pizarnik', 'Hermana', 'DNI', 19555009, 'Alejandra', '1936-05-29', NULL, 23123125, NULL, 64.00, '1 Rue Victor Cousin 75005 Paris Francia');


INSERT INTO Datos_de_Contacto(email, tipo_email, telefono, tipo_telefono, id_contacto, dni)
SELECT 'jcort@proton.me', 'Personal', 3777892312, 'Personal', 1233982, p.dni
FROM Profesores AS p
WHERE p.nombre LIKE '%Julio%' AND p.apellido LIKE '%Cortázar%';


INSERT INTO Antecedentes_Profesionales(empresa_anterior, tipo_actividad, cargo, desde, hasta, dni)
SELECT 'Editorial Planeta', 'Escritor', 'Editor', '1989-11-09', NULL, p.dni
FROM Profesores AS p
WHERE p.dni = 23123125;


INSERT INTO Participacion_Reuniones_Cientificas(fecha, participacion, titulo, dni)
SELECT '2004-07-14', 'Orador', 'Lingüísitca según Chomsky', p.dni
FROM Profesores AS p
WHERE p.dni = 23123125;


/* Modificación de datos. */

UPDATE Profesores
SET legajo = legajo + 10000000
WHERE codigo_postal >= 3500;


UPDATE Datos_de_Contacto
SET id_contacto = id_contacto + 12034
WHERE dni > 80000000 AND tipo_email LIKE 'Trabajo';


UPDATE Datos_de_Contacto
SET tipo_email = 'Trabajo'
WHERE dni = 23123125 AND tipo_email LIKE 'Personal';

/* Revisar */
UPDATE Dependencia
SET observacion = 'Observación actualizada'
WHERE idos IN (
    SELECT idos 
    FROM Obra_Social
    WHERE dni = 39387376
);

/* Revisar */
UPDATE Profesores
SET departamento = 'Literatura', codigo_postal = 3450
WHERE dni = 23123125;


UPDATE Profesores
SET inicio_actividad = '2020-01-01'
WHERE dni IN (
    SELECT dni
    FROM Datos_Trabajo
    WHERE presta_servicio_utn = 'True'
);






/* Creamos la base de datos si no existe y luego la seleccionamos. */
CREATE DATABASE IF NOT EXISTS TPI;
USE TPI;

CREATE TABLE Profesores (
    dni INT PRIMARY KEY,
    tipo_domicilio VARCHAR(255),
    fecha_nacimiento DATE,
    nombre VARCHAR(255),
    apellido VARCHAR(255),
    localidad VARCHAR(255),
    departamento VARCHAR(255),
    provincia VARCHAR(255),
    numero INT,
    piso VARCHAR(255),
    codigo_postal INT,
    calle VARCHAR(255),
    edad INT,
    cuil BIGINT,
    inicio_actividad DATE,
    estado_civil VARCHAR(255),
    sexo CHAR(1),
    barrio VARCHAR(255),
    legajo INT UNIQUE
);

CREATE TABLE Obra_Social (
    dni INT NOT NULL,
    idos INT PRIMARY KEY,
    CONSTRAINT fk_obra_social_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Dependencia (
    nombre VARCHAR(255),
    cargo VARCHAR(255),
    año_alta DATE,
    obra_social VARCHAR(255),
    observacion VARCHAR(255),
    idos INT,
    PRIMARY KEY (nombre, idos),
    CONSTRAINT fk_dependencia_idos FOREIGN KEY (idos) REFERENCES Obra_Social(idos) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Datos_Trabajo (
    tipo_personal VARCHAR(255),
    caracter VARCHAR(255),
    presta_servicio_utn VARCHAR(255),
    idos INT UNIQUE,
    PRIMARY KEY (tipo_personal, caracter, idos),
    CONSTRAINT fk_datos_trabajo_idos FOREIGN KEY (idos) REFERENCES Obra_Social(idos) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Seguro_de_Vida (
    idsv INT PRIMARY KEY,
    dni INT NOT NULL,
    CONSTRAINT fk_seguro_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Familiar (
    apellido VARCHAR(255),
    parentesco VARCHAR(255),
    tipo_documento VARCHAR(255),
    nro_documento INT,
    nombre VARCHAR(255),
    fecha_nacimiento DATE,
    idos INT,
    dni INT,
    idsv INT,
    porcentaje REAL,
    domicilio VARCHAR(255),
    PRIMARY KEY (nro_documento, dni),
    CONSTRAINT fk_familiar_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_familiar_idos FOREIGN KEY (idos) REFERENCES Obra_Social(idos),
    CONSTRAINT fk_familiar_idsv FOREIGN KEY (idsv) REFERENCES Seguro_de_Vida(idsv)
);

CREATE TABLE Participacion_Reuniones_Cientificas (
    titulo VARCHAR(255),
    participacion VARCHAR(255),
    fecha DATE,
    dni INT,
    PRIMARY KEY (titulo, dni),
    CONSTRAINT fk_participacion_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Publicaciones (
    titulo VARCHAR(255),
    autores VARCHAR(255),
    referencia_bibliografica VARCHAR(255),
    año INT,
    dni INT,
    PRIMARY KEY (titulo, dni),
    CONSTRAINT fk_publicaciones_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Antecedentes_Profesionales (
    empresa_anterior VARCHAR(255),
    tipo_actividad VARCHAR(255),
    cargo VARCHAR(255),
    desde DATE,
    hasta DATE,
    dni INT,
    PRIMARY KEY (empresa_anterior, dni),
    CONSTRAINT fk_antecedentes_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Titulos (
    nivel VARCHAR(255),
    titulo_obtenido VARCHAR(255),
    institucion VARCHAR(255),
    desde DATE,
    hasta DATE,
    dni INT,
    PRIMARY KEY (titulo_obtenido, dni),
    CONSTRAINT fk_titulos_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Idiomas (
    idioma VARCHAR(255),
    nivel VARCHAR(255),
    certificacion VARCHAR(255),
    institucion VARCHAR(255),
    dni INT,
    PRIMARY KEY (idioma, dni),
    CONSTRAINT fk_idiomas_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Cursos_y_Conferencias (
    nombre VARCHAR(255),
    descripcion VARCHAR(255),
    institucion VARCHAR(255),
    desde DATE,
    hasta DATE,
    dni INT,
    PRIMARY KEY (nombre, dni),
    CONSTRAINT fk_cursos_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Actividades_y_Antecedentes (
    dedicacion VARCHAR(255),
    dni INT,
    desde DATE,
    hasta DATE,
    id_antecedente INT,
    PRIMARY KEY (id_antecedente, dni),
    CONSTRAINT fk_actividades_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Antecedentes_Extension_Universitaria (
    acciones VARCHAR(255),
    cargo VARCHAR(255),
    dedicacion VARCHAR(255),
    dni INT,
    desde DATE,
    hasta DATE,
    id_antecedente INT,
    PRIMARY KEY (id_antecedente, dni),
    CONSTRAINT fk_extension_id_antecedente FOREIGN KEY (id_antecedente) REFERENCES Actividades_y_Antecedentes(id_antecedente) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_extension_dni FOREIGN KEY (dni) REFERENCES Actividades_y_Antecedentes(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Actividad_e_Investigacion (
    categoria VARCHAR(255),
    area_principal VARCHAR(255),
    dedicacion VARCHAR(255),
    dni INT,
    desde DATE,
    hasta DATE,
    id_antecedente INT,
    PRIMARY KEY (id_antecedente, dni),
    CONSTRAINT fk_investigacion_id_antecedente FOREIGN KEY (id_antecedente) REFERENCES Actividades_y_Antecedentes(id_antecedente) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_investigacion_dni FOREIGN KEY (dni) REFERENCES Actividades_y_Antecedentes(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Antecedentes_Docentes (
    unidad_academica VARCHAR(255),
    cargo VARCHAR(255),
    dedicacion VARCHAR(255),
    dni INT,
    desde DATE,
    hasta DATE,
    id_antecedente INT,
    PRIMARY KEY (id_antecedente, dni),
    CONSTRAINT fk_docentes_id_antecedente FOREIGN KEY (id_antecedente) REFERENCES Actividades_y_Antecedentes(id_antecedente) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_docentes_dni FOREIGN KEY (dni) REFERENCES Actividades_y_Antecedentes(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Datos_del_Empleador (
    codigo_postal INT(5),
    provincia VARCHAR(255),
    localidad VARCHAR(255),
    departamento VARCHAR(255),
    numero INT,
    piso INT(2),
    calle VARCHAR(255),
    razon_social VARCHAR(255),
    cuit_cuil BIGINT,
    idsv INT,
    PRIMARY KEY (cuit_cuil, idsv),
    CONSTRAINT fk_empleador_idsv FOREIGN KEY (idsv) REFERENCES Seguro_de_Vida(idsv) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Datos_de_Contacto (
    email VARCHAR(255) UNIQUE,
    tipo_email VARCHAR(255),
    telefono VARCHAR(255) UNIQUE,
    tipo_telefono VARCHAR(255),
    id_contacto INT UNIQUE,
    dni INT,
    PRIMARY KEY (id_contacto, dni),
    CONSTRAINT fk_contacto_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Declaracion_Jurada (
    iddj INT PRIMARY KEY,
    dni INT NOT NULL,
    CONSTRAINT fk_declaracion_dni FOREIGN KEY (dni) REFERENCES Profesores(dni) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE Carga_Horaria (
    dia VARCHAR(255),
    lugar VARCHAR(255),
    horario VARCHAR(255),
    nombre_catedra VARCHAR(255),
    horas_clase INT,
    iddj INT,
    PRIMARY KEY (dia, horario, nombre_catedra, iddj),
    CONSTRAINT fk_carga_iddj FOREIGN KEY (iddj) REFERENCES Declaracion_Jurada(iddj) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Datos_de_Cargo (
    cargo VARCHAR(255),
    iddj INT,
    calle VARCHAR(255),
    provincia VARCHAR(255),
    reparticion VARCHAR(255),
    dependencia VARCHAR(255),
    cumple_horarios VARCHAR(255),
    organismo VARCHAR(255),
    localidad_cargo VARCHAR(255),
    numero INT,
    PRIMARY KEY (cargo, iddj),
    CONSTRAINT fk_cargo_iddj FOREIGN KEY (iddj) REFERENCES Declaracion_Jurada(iddj) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Pasividades (
    regimen VARCHAR(255),
    iddj INT,
    desde VARCHAR(255),
    causa VARCHAR(255),
    suspendido VARCHAR(255), -- Acá no lo modelamos como "BOOLEAN" porque dicho tipo de dato se traduce como un TINYINT
    institucion_abonante VARCHAR(255),
    PRIMARY KEY (regimen, iddj),
    CONSTRAINT fk_pasividades_iddj FOREIGN KEY (iddj) REFERENCES Declaracion_Jurada(iddj) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Tareas_No_Estatales (
    fecha_ingreso DATE,
    lugar_presta_servicio VARCHAR(255),
    tipo_dependencia VARCHAR(255),
    funcion VARCHAR(255),
    iddj INT,
    PRIMARY KEY (lugar_presta_servicio, iddj),
    CONSTRAINT fk_tareas_iddj FOREIGN KEY (iddj) REFERENCES Declaracion_Jurada(iddj) ON DELETE CASCADE ON UPDATE CASCADE
);

/*Creación de base de datos*/
CREATE DATABASE slsm_db;
USE slsm_db;

/*Creación de tablas*/
CREATE TABLE usuarios (
	id_usuario INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(80),
    apellidos VARCHAR(80),
    correo VARCHAR(80),
    id_rol INT,
    contrasena VARCHAR(100),
    contrasena_hash VARCHAR(150),
    PRIMARY KEY(id_usuario)
);

CREATE TABLE roles (
	id_rol INT NOT NULL AUTO_INCREMENT,
    nombre_rol VARCHAR(20),
    PRIMARY KEY(id_rol)
);

CREATE TABLE historiales_medicos (
	id_historial INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    fecha_nacimiento DATE,
    altura FLOAT,
    numero_telefono VARCHAR(20),
    genero VARCHAR(15),
    peso FLOAT,
    pregunta1_sec2 VARCHAR(2),
    pregunta2_sec2 INT,
    pregunta3_sec2 VARCHAR(2),
    pregunta4_sec2 FLOAT,
    pregunta5_sec2 INT,
    pregunta6_sec2 VARCHAR(2),
    pregunta7_sec2 VARCHAR(200),
    pregunta8_sec2 INT,
    pregunta9_sec2 INT,
    pregunta10_sec2 VARCHAR(200),
    pregunta11_sec2 VARCHAR(200),
    pregunta12_sec2 VARCHAR(200),
    pregunta13_sec2 VARCHAR(200),
    pregunta1_sec3 VARCHAR(2),
    pregunta2_sec3 INT,
    pregunta3_sec3 VARCHAR(2),
    pregunta4_sec3 VARCHAR(200),
    pregunta5_sec3 VARCHAR(2),
    pregunta6_sec3 INT,
    pregunta7_sec3 VARCHAR(2),
    pregunta8_sec3 VARCHAR(200),
    pregunta9_sec3 VARCHAR(2),
    pregunta10_sec3 INT,
    pregunta11_sec3 VARCHAR(2),
    pregunta12_sec3 VARCHAR(200),
    pregunta13_sec3 VARCHAR(2),
    pregunta14_sec3 INT,
    pregunta15_sec3 VARCHAR(2),
    pregunta16_sec3 VARCHAR(200),
    pregunta17_sec3 VARCHAR(200),
    pregunta1_sec4 VARCHAR(2),
    pregunta2_sec4 VARCHAR(2),
    pregunta3_sec4 VARCHAR(2),
    pregunta4_sec4 VARCHAR(2),
    pregunta5_sec4 VARCHAR(200),
    pregunta6_sec4 VARCHAR(2),
    pregunta7_sec4 VARCHAR(2),
    pregunta8_sec4 VARCHAR(2),
    pregunta9_sec4 VARCHAR(2),
    pregunta10_sec4 VARCHAR(2),
    pregunta11_sec4 VARCHAR(2),
    pregunta12_sec4 VARCHAR(2),
    pregunta13_sec4 VARCHAR(2),
    pregunta14_sec4 VARCHAR(200),
    pregunta15_sec4 VARCHAR(2),
    pregunta16_sec4 VARCHAR(2),
    pregunta17_sec4 VARCHAR(2),
    pregunta18_sec4 VARCHAR(2),
    pregunta19_sec4 VARCHAR(2),
    pregunta20_sec4 VARCHAR(2),
    pregunta21_sec4 VARCHAR(2),
    pregunta22_sec4 VARCHAR(200),
    pregunta1_sec5 VARCHAR(2),
    pregunta2_sec5 VARCHAR(200),
    pregunta3_sec5 VARCHAR(2),
    pregunta4_sec5 VARCHAR(40),
    pregunta5_sec5 VARCHAR(2),
    pregunta6_sec5 VARCHAR(2),
    pregunta7_sec5 VARCHAR(40),
    pregunta1_sec6 INT,
    pregunta2_sec6 VARCHAR(80),
    pregunta3_sec6 VARCHAR(2),
    pregunta4_sec6 VARCHAR(2),
    pregunta5_sec6 VARCHAR(2),
    pregunta6_sec6 VARCHAR(2),
    pregunta1_sec7 VARCHAR(2),
    pregunt2_sec7 VARCHAR(2),
    pregunta3_sec7 VARCHAR(200),
    pregunta4_sec7 VARCHAR(2),
    pregunta1_ext VARCHAR(2),
    pregunta2_ext VARCHAR(200),
    pregunta3_ext VARCHAR(200),
    pregunta4_ext VARCHAR(200),
    pregunta5_ext VARCHAR(200),
    pregunta6_ext VARCHAR(200),
    PRIMARY KEY(id_historial) 
);

ALTER TABLE historiales_medicos
	MODIFY pregunta3_ext VARCHAR(200);

ALTER TABLE historiales_medicos
	MODIFY pregunta5_ext VARCHAR(200);

ALTER TABLE historiales_medicos
	MODIFY pregunta2_sec6 VARCHAR(200);
    
ALTER TABLE historiales_medicos
	MODIFY pregunta6_ext VARCHAR(200);

CREATE TABLE hojas_evolucion_medico (
	id_hojas INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    fecha_registro DATE,
    peso FLOAT,
    IMC FLOAT,
    grasa_viseral FLOAT,
    porcentaje_musculo FLOAT,
    abdomen FLOAT,
    ejercicio INT,
    horas_sueno INT,
    talla FLOAT,
    grasa_corporal FLOAT,
    edad_metabolica INT,
    calorias INT,
    glucosa FLOAT,
    comida_chatarra VARCHAR(15),
    calidad_sueno VARCHAR(15),
    notas VARCHAR(200),
    PRIMARY KEY(id_hojas)
);

CREATE TABLE avances_usuarios (
	id_avance INT NOT NULL AUTO_INCREMENT,
    id_usuario INT,
    fecha_registro DATE,
    pregunta1_sec1 INT,
    notas1_sec1 VARCHAR(200),
    notas2_sec1 VARCHAR(200),
    pregunta1_sec2 INT,
    notas1_sec2 VARCHAR(200),
    notas2_sec2 VARCHAR(200),
    pregunta1_sec3 INT,
    notas1_sec3 VARCHAR(200),
    notas2_sec3 VARCHAR(200),
    pregunta1_sec4 INT,
    notas1_sec4 VARCHAR(200),
    notas2_sec4 VARCHAR(200),
    pregunta1_sec5 INT,
    notas1_sec5 VARCHAR(200),
    notas2_sec5 VARCHAR(200),
    pregunta1_sec6 INT,
    notas1_sec6 VARCHAR(200),
    notas2_sec6 VARCHAR(200),
    pregunta1_sec7 VARCHAR(200),
    PRIMARY KEY(id_avance)
);

/*
--- CONSULTAS ---
*/

/*Visualizacion de tablas*/
SHOW TABLES;

/*Cambiar nombre de un campo*/
/*ALTER TABLE usuarios CHANGE rol id_rol INT;*/

/*Agregar datos*/
INSERT INTO roles (nombre_rol)
VALUES ('Especialista'), ('Paciente');

/*Eliminar una fila
DELETE FROM `slsm_db`.`usuarios` WHERE (`id_usuario` = '7');
*/

ALTER TABLE hojas_evolucion_medico
	MODIFY calidad_sueno VARCHAR(18);
    
ALTER TABLE hojas_evolucion_medico
	MODIFY comida_chatarra VARCHAR(18);

/*Consulta*/
SELECT * FROM usuarios;
SELECT * FROM roles;
SELECT * FROM historiales_medicos;
SELECT * FROM avances_usuarios;
SELECT * FROM hojas_evolucion_medico;

/*Consulta*/
SELECT * FROM usuarios WHERE id_rol = 1;
SELECT * FROM usuarios WHERE id_rol = 2;

SELECT * FROM hojas_evolucion_medico WHERE fecha_registro = '2023-10-16';

SELECT DISTINCT EXTRACT(YEAR FROM fecha_registro) FROM avances_usuarios;

SELECT DISTINCT EXTRACT(YEAR FROM a.fecha_registro), EXTRACT(YEAR FROM b.fecha_registro)
FROM avances_usuarios AS a
INNER JOIN hojas_evolucion_medico AS b;

SELECT MAX(fecha_registro) FROM hojas_evolucion_medico WHERE id_usuario = 6;

SELECT * FROM hojas_evolucion_medico WHERE id_usuario = 6 AND fecha_registro = (SELECT MAX(fecha_registro) FROM	hojas_evolucion_medico);

SELECT * 
FROM hojas_evolucion_medico 
WHERE id_usuario = 1 AND fecha_registro = (SELECT MAX(fecha_registro) FROM hojas_evolucion_medico);

SELECT *
FROM hojas_evolucion_medico AS a
INNER JOIN
(
	SELECT  id_usuario, MAX(fecha_registro) AS fecha_max
	FROM hojas_evolucion_medico
	GROUP BY id_usuario
) AS b 
ON a.id_usuario = b.id_usuario AND a.fecha_registro = b.fecha_max
WHERE a.id_usuario = 6;

SELECT * FROM hojas_evolucion_medico AS a INNER JOIN(SELECT id_usuario, MAX(fecha_registro) AS fecha_max FROM hojas_evolucion_medico GROUP BY id_usuario) AS b ON a.id_usuario = b.id_usuario AND a.fecha_registro = b.fecha_max WHERE a.id_usuario = 6;
 
SELECT 
	id_usuario,
    nombre,
    apellidos
FROM 
	usuarios
WHERE 
	CONCAT(nombre, " ", apellidos) LIKE '%ADOLFO%';
    

SELECT 
	id_usuario,
    CONCAT(nombre, " ", apellidos) AS nombre_completo
FROM 
	usuarios
WHERE 
    id_rol = 2 AND CONCAT(nombre, " ", apellidos) LIKE '%ADOLFO%';
    
SELECT id_usuario, CONCAT(nombre, " ", apellidos) AS nombre_completo FROM usuarios WHERE id_rol = 2 AND CONCAT(nombre, " ", apellidos) LIKE '%ADOLFO%';


SELECT 
	usuarios.id_usuario,
    usuarios.nombre,
    usuarios.apellidos,
    roles.nombre_rol 
FROM 
	usuarios,
    roles
WHERE
	usuarios.id_rol = roles.id_rol;
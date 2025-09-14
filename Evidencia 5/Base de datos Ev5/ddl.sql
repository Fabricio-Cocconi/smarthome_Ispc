-- Script DDL para la base de datos SmartHome
-- Compatible con editores online MySQL

-- Tabla rol
CREATE TABLE rol (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL
);

-- Tabla usuario
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES rol(id)
);

-- Tabla dispositivo
CREATE TABLE dispositivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    estado BOOLEAN DEFAULT FALSE,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- Tabla automatizacion
CREATE TABLE automatizacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(255),
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

-- Tabla regla_automatizacion
CREATE TABLE regla_automatizacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    automatizacion_id INT,
    condicion VARCHAR(255),
    accion VARCHAR(255),
    descripcion VARCHAR(255),
    FOREIGN KEY (automatizacion_id) REFERENCES automatizacion(id)
);

-- Tabla automatizacion_dispositivo
CREATE TABLE automatizacion_dispositivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    automatizacion_id INT,
    dispositivo_id INT,
    accion VARCHAR(100),
    FOREIGN KEY (automatizacion_id) REFERENCES automatizacion(id),
    FOREIGN KEY (dispositivo_id) REFERENCES dispositivo(id)
);

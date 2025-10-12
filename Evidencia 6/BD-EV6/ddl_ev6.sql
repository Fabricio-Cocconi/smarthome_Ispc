-- Estructura de base de datos para SmartHome
-- Motor: MySQL

CREATE DATABASE IF NOT EXISTS smarthome;
USE smarthome;

-- Tabla de roles
CREATE TABLE rol (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de usuarios
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contrasena VARCHAR(255) NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES rol(id)
);

-- Tabla de dispositivos
CREATE TABLE dispositivo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    estado BOOLEAN DEFAULT FALSE,
    usuario_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

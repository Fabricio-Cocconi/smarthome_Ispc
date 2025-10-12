-- DML SmartHome - Evidencia 6
-- Copiar desde la linea 12 hasta el final para ejecutar en un IDE online como OneCompiler o RunSQL
-- Motor: MySQL

USE smarthome;

-- Cargamos datos iniciales para probar el sistema SmartHome

-- Roles del sistema
-- El admin puede hacer CRUD de dispositivos
-- El usuario comun solo puede consultar
INSERT INTO rol (nombre) VALUES 
('admin'), 
('estandar');

-- Usuarios del sistema
-- Juan y Carlos son administradores, los demas son usuarios comunes
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES
('Juan', 'pass1', 1),
('Maria', 'pass2', 2),
('Pedro', 'pass3', 2),
('Lucia', 'pass4', 2),
('Carlos', 'pass5', 1);

-- Dispositivos agregados por los administradores
-- Los usuarios comunes no crean dispositivos, solo pueden verlos
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES
('Luz Living', 'luz', 1, 1),
('Camara Entrada', 'camara', 1, 1),
('Cafetera', 'electrodomestico', 0, 1),
('Sensor Movimiento', 'sensor', 1, 5),
('Ventilador', 'electrodomestico', 0, 5),
('Luz Cocina', 'luz', 1, 5);

-- Consultas simples para revisar las tablas

-- Ver roles registrados
SELECT * FROM rol;

-- Ver usuarios junto a su rol
SELECT 
    u.id, 
    u.nombre, 
    r.nombre AS rol 
FROM usuario u
JOIN rol r ON u.rol_id = r.id;

-- Ver dispositivos con su estado
SELECT * FROM dispositivo;

-- Consultas multitabla utiles

-- 1. Mostrar los dispositivos y el nombre del admin que los creo
SELECT 
    d.nombre AS dispositivo, 
    d.tipo, 
    d.estado, 
    u.nombre AS administrador
FROM dispositivo d
JOIN usuario u ON d.usuario_id = u.id
JOIN rol r ON u.rol_id = r.id
WHERE r.nombre = 'admin';

-- 2. Ver cuantos dispositivos tiene cada usuario
SELECT 
    u.nombre AS usuario, 
    COUNT(d.id) AS cantidad_dispositivos
FROM usuario u
LEFT JOIN dispositivo d ON u.id = d.usuario_id
GROUP BY u.id;

-- Fin del script DML
-- Hasta aca se cargan los datos y se hacen las consultas basicas para la evidencia 6

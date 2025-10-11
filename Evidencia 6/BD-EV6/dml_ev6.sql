-- DML SmartHome - Evidencia 6
-- Copiar desde la linea 1 hasta el final para ejecutar en un IDE online como OneCompiler o RunSQL

USE smarthome;

-- Cargamos algunos datos iniciales del sistema SmartHome

-- Roles del sistema, uno para administradores y otro para usuarios comunes
INSERT INTO rol (nombre) VALUES 
('admin'), 
('estandar');

-- Usuarios basicos para probar el login desde Python
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES
('Juan', 'pass1', 1),
('Maria', 'pass2', 2),
('Pedro', 'pass3', 2),
('Lucia', 'pass4', 2),
('Carlos', 'pass5', 1);

-- Dispositivos registrados por distintos usuarios
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES
('Luz Living', 'luz', 1, 1),
('Camara Entrada', 'camara', 1, 1),
('Cafetera', 'electrodomestico', 0, 2),
('Sensor Movimiento', 'sensor', 1, 3),
('Ventilador', 'electrodomestico', 0, 4),
('Luz Cocina', 'luz', 0, 5);

-- Automatizaciones creadas por los usuarios
INSERT INTO automatizacion (nombre, descripcion, usuario_id) VALUES
('Modo Noche', 'Apagar luces despues de las 23', 1),
('Modo Desayuno', 'Encender luces de cocina y cafetera a las 7', 2),
('Modo Seguridad', 'Activar camaras si hay movimiento', 1),
('Modo Ahorro', 'Apagar ventilador si no hay personas', 4);

-- Reglas que pertenecen a las automatizaciones anteriores
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion) VALUES
(1, 'hora > 23', 'apagar luces'),
(2, 'hora = 7', 'encender cafetera'),
(3, 'movimiento detectado', 'activar camaras'),
(4, 'sin movimiento', 'apagar ventilador');

-- Consultas simples para revisar el contenido de cada tabla

-- Ver todos los roles
SELECT * FROM rol;

-- Ver todos los usuarios registrados
SELECT * FROM usuario;

-- Ver todos los dispositivos
SELECT * FROM dispositivo;

-- Ver todas las automatizaciones
SELECT * FROM automatizacion;

-- Consultas multitabla con sentido para el sistema

-- 1. Listar los dispositivos junto con el nombre del usuario al que pertenecen
SELECT 
    d.id, 
    d.nombre AS dispositivo, 
    d.tipo, 
    d.estado, 
    u.nombre AS propietario
FROM dispositivo d
JOIN usuario u ON d.usuario_id = u.id;

-- 2. Ver las automatizaciones creadas por cada usuario
SELECT 
    a.nombre AS automatizacion, 
    a.descripcion, 
    u.nombre AS usuario
FROM automatizacion a
JOIN usuario u ON a.usuario_id = u.id;

-- Fin del script DML
-- Hasta aca llegan los datos de prueba y las consultas

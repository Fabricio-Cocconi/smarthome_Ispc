-- Datos iniciales para SmartHome

USE smarthome;

-- Roles
INSERT INTO rol (nombre) VALUES ('admin'), ('estandar');

-- Usuarios
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES
('Juan', 'pass1', 1),
('Maria', 'pass2', 2),
('Pedro', 'pass3', 2),
('Lucia', 'pass4', 2),
('Carlos', 'pass5', 1);

-- Dispositivos
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES
('Luz Living', 'luz', 1, 1),
('Cámara Entrada', 'camara', 1, 1),
('Cafetera', 'electrodomestico', 0, 2),
('Sensor Movimiento', 'sensor', 1, 3),
('Ventilador', 'electrodomestico', 0, 4),
('Luz Cocina', 'luz', 0, 5);

-- Automatizaciones
INSERT INTO automatizacion (nombre, descripcion, usuario_id) VALUES
('Modo Noche', 'Apagar luces después de las 23:00', 1),
('Modo Desayuno', 'Encender luces de cocina y cafetera a las 7:00', 2),
('Modo Seguridad', 'Activar cámaras si hay movimiento', 1),
('Modo Ahorro', 'Apagar ventilador si no hay personas', 4);

-- Reglas (ejemplos)
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion) VALUES
(1, 'hora > 23', 'apagar luces'),
(2, 'hora = 7', 'encender cafetera'),
(3, 'movimiento detectado', 'activar camaras'),
(4, 'sin movimiento', 'apagar ventilador');

-- Consultas simples
SELECT * FROM rol;
SELECT * FROM usuario;
SELECT * FROM dispositivo;
SELECT * FROM automatizacion;

-- Consultas multitabla útiles
/* 1. Ver los dispositivos junto a su propietario */
SELECT d.id, d.nombre AS dispositivo, d.tipo, d.estado, u.nombre AS propietario
FROM dispositivo d
JOIN usuario u ON d.usuario_id = u.id;

/* 2. Ver automatizaciones por usuario */
SELECT a.nombre AS automatizacion, a.descripcion, u.nombre AS usuario
FROM automatizacion a
JOIN usuario u ON a.usuario_id = u.id;

/* 3. Mostrar qué automatizaciones tienen reglas configuradas */
SELECT a.nombre AS automatizacion, COUNT(r.id) AS cantidad_reglas
FROM automatizacion a
LEFT JOIN regla_automatizacion r ON a.id = r.automatizacion_id
GROUP BY a.id;

/* 4. Ver qué dispositivos pertenecen a usuarios administradores */
SELECT d.nombre AS dispositivo, u.nombre AS admin
FROM dispositivo d
JOIN usuario u ON d.usuario_id = u.id
JOIN rol r ON u.rol_id = r.id
WHERE r.nombre = 'admin';

-- Subconsultas útiles
/* Usuarios que tienen más de un dispositivo */
SELECT nombre FROM usuario
WHERE id IN (SELECT usuario_id FROM dispositivo GROUP BY usuario_id HAVING COUNT(*) > 1);

/* Automatizaciones que pertenecen a usuarios con rol admin */
SELECT nombre FROM automatizacion
WHERE usuario_id IN (SELECT id FROM usuario WHERE rol_id = 1);

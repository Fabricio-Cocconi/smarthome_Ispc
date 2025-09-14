-- Script DML para insertar datos iniciales y consultas de cada tabla
-- Compatible con MySQL

-- Insertar roles 
INSERT INTO rol (nombre) VALUES ('admin');
INSERT INTO rol (nombre) VALUES ('estandar');

-- Insertar usuarios 
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Juan', 'pass1', 1);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Maria', 'pass2', 2);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Pedro', 'pass3', 2);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Ana', 'pass4', 2);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Carlos', 'pass6', 2);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Diego', 'pass8', 1);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Lucia', 'pass9', 2);
INSERT INTO usuario (nombre, contrasena, rol_id) VALUES ('Tomas', 'pass10', 1);

-- Insertar dispositivos 
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Luz Salon', 'luz', 1, 1);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Cafetera', 'cafetera', 0, 2);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Camara Entrada', 'camara', 1, 1);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Luz Cocina', 'luz', 0, 3);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Luz Dormitorio', 'luz', 1, 4);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Camara Comedor', 'camara', 1, 5);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Sensor Movimiento', 'sensor', 1, 6);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Luz Baño', 'luz', 0, 7);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Ventilador', 'ventilador', 0, 8);
INSERT INTO dispositivo (nombre, tipo, estado, usuario_id) VALUES ('Persiana', 'persiana', 0, 1);

-- Insertar automatizaciones 
INSERT INTO automatizacion (nombre, descripcion, usuario_id) VALUES ('Modo Noche', 'Apagar luces por la noche', 1);
INSERT INTO automatizacion (nombre, descripcion, usuario_id) VALUES ('Modo Desayuno', 'Encender luces de cocina y cafetera', 2);
INSERT INTO automatizacion (nombre, descripcion, usuario_id) VALUES ('Alarma Seguridad', 'Activar camaras al detectar movimiento', 1);

-- Insertar reglas de automatizacion 
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion, descripcion) VALUES (1, 'hora > 22', 'apagar luces', 'Apagar luces de noche');
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion, descripcion) VALUES (1, 'usuario ausente', 'activar alarma', 'Activar alarma si usuario ausente');
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion, descripcion) VALUES (2, 'hora = 7', 'encender luces cocina', 'Encender luces de cocina');
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion, descripcion) VALUES (2, 'hora = 7', 'encender cafetera', 'Encender cafetera');
INSERT INTO regla_automatizacion (automatizacion_id, condicion, accion, descripcion) VALUES (3, 'movimiento detectado', 'activar camara', 'Activar camara al detectar movimiento');

-- Insertar automatizacion_dispositivo 
INSERT INTO automatizacion_dispositivo (automatizacion_id, dispositivo_id, accion) VALUES (1, 1, 'apagar');
INSERT INTO automatizacion_dispositivo (automatizacion_id, dispositivo_id, accion) VALUES (2, 2, 'encender');

-- Consultas de cada tabla
SELECT * FROM rol;
SELECT * FROM usuario;
SELECT * FROM dispositivo;
SELECT * FROM automatizacion;
SELECT * FROM regla_automatizacion;
SELECT * FROM automatizacion_dispositivo;

# Proyecto SmartHome - Evidencia 6

**Grupo 18**  
**Integrante:** Fabricio Andres Cocconi Huenz - DNI 46708260  
**Carrera:** TSDS - Tecnicatura Superior en Desarrollo de Software  
**Cohorte 2025 - ISPC**

Este trabajo pertenece a la evidencia 6 de Programacion I.  
La idea fue seguir mejorando el proyecto SmartHome que se vino desarrollando en las entregas anteriores.  
En esta parte se aplico el patron DAO y se ordeno el sistema en capas para que el codigo sea mas limpio y facil de mantener.

---

## Objetivo general

El objetivo principal fue lograr un sistema que simule un hogar inteligente donde se puedan manejar usuarios y dispositivos desde un menu por consola.  
Todo el sistema esta hecho en Python y conectado a una base de datos MySQL.  
El enfoque fue usar buenas practicas y una estructura modular, separando las partes que manejan datos de las que manejan la logica del programa.

---

## Que tiene esta version

- Clases de dominio que representan usuarios, dispositivos y automatizaciones  
- Clases DAO que se encargan del acceso a la base de datos  
- Conexion real con MySQL usando una clase dedicada  
- Menus mejorados y mas faciles de leer tanto para usuario comun como para administrador  
- Sistema de inicio de sesion con usuarios cargados en la base  
- Estructura de carpetas ordenada por tipo de archivo  

---

## Estructura del proyecto

POO-SmartHome/
│
├── app/
│ ├── dominio/ -> Clases de negocio
│ ├── dao/ -> Clases DAO e interfaces
│ ├── conn/ -> Conexion con MySQL
│ └── main.py -> Programa principal con los menus
│
├── BD-Evidencia-6/ -> Scripts SQL (DDL y DML)
│ └── README.md -> Guia para ejecutar los scripts
│
└── README.md -> Este archivo con la descripcion general

---

## Como probar el sistema

1. Crear la base `smarthome` ejecutando primero el archivo `ddl.sql`  
2. Luego insertar los datos con el archivo `dml.sql`  
3. Abrir `main.py` y ejecutar el programa con  
4. Iniciar sesion con alguno de los usuarios cargados.  
Por ejemplo:  
- Usuario: Juan / Contraseña: pass1 (admin)  
- Usuario: Maria / Contraseña: pass2 (estandar)

El menu cambia segun el tipo de usuario que inicie sesion.

---

## Cambios respecto a las entregas anteriores

En esta version el sistema ya esta completo.  
Se agrego la conexion con MySQL y se aplico el patron DAO para separar las funciones.  
Tambien se mejoro la experiencia del menu para que sea mas natural y simple de usar.  
No se incluyo el registro de usuarios nuevos ni el cambio de rol porque no era obligatorio en esta entrega.  
El foco fue mantener el codigo modular, ordenado y facil de entender.

---

## Resumen

El proyecto SmartHome ahora esta totalmente funcional y con persistencia real de datos.  
Usa Python y MySQL de forma integrada y sigue una estructura pensada para proyectos reales.  
Se puede ejecutar sin configuraciones complicadas y refleja el trabajo hecho a lo largo de todas las evidencias.  

Este archivo busca explicar de forma sencilla como esta armado el sistema y que se logro con esta ultima version.

# SmartHome - Base de datos Evidencia 6

Esta carpeta contiene todo lo necesario para crear y probar la base de datos del proyecto SmartHome.  
Los archivos estan listos para ser usados tanto en MySQL local como en plataformas online.  
El objetivo fue mantener la base simple, ordenada y facil de probar sin instalar nada extra.

---

## Archivos incluidos

- **ddl.sql** → crea la base de datos y todas las tablas necesarias  
- **dml.sql** → inserta los datos iniciales y contiene algunas consultas de prueba  

---

## Como probar los scripts online

Si no queres instalar MySQL, podes usar paginas que permiten ejecutar SQL desde el navegador, como:

- [OneCompiler (MySQL)](https://onecompiler.com/mysql)  
- [RunSQL](https://runsql.com)

### Pasos para ejecutar

1. Abri el sitio de tu preferencia  
2. Copia y pega **desde la linea 7 hasta el final** del archivo `ddl.sql`  
3. Ejecuta el script para crear la base y las tablas  
4. Despues copia y pega **desde la linea 9 hasta el final** del archivo `dml.sql`  
5. Ejecuta el segundo script para insertar los datos y ver las consultas  

Vas a poder ver las tablas, los registros y los resultados directamente en la plataforma sin hacer configuraciones raras.

---

## Contenido de los scripts

El **archivo `ddl.sql`** crea las tablas principales:

- `usuario`  
- `rol`  
- `dispositivo`  
- `automatizacion`  
- `regla_automatizacion`

Cada tabla tiene su clave primaria, relaciones y tipos de datos basicos.

El **archivo `dml.sql`** agrega datos iniciales y algunas consultas que muestran la informacion relacionada entre usuarios, dispositivos y automatizaciones.  
No se incluyeron subconsultas porque no eran obligatorias para esta evidencia, pero se agregaron algunas consultas multitabla que tienen sentido para el sistema.

---

## Motor de base de datos

El proyecto fue desarrollado y probado usando **MySQL**.  
Si usas OneCompiler o RunSQL, asegurate de elegir *MySQL* como motor antes de ejecutar los scripts.  
Si estas trabajando localmente, podes usar cualquier version reciente de MySQL o XAMPP.

---

## Notas finales

Estos scripts fueron pensados para acompañar la parte de programacion hecha en Python.  
Permiten crear rapidamente la base `smarthome` y probar la conexion desde el sistema usando el patron DAO.  
Con esto se completa la parte de base de datos de la evidencia 6 y se asegura que el sistema funcione de punta a punta.

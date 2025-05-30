# 🗃️ CRUD de Clientes con Python y MySQL

Este proyecto es una aplicación de escritorio construida con **Python**, usando **Tkinter** para la interfaz gráfica y **MySQL** como base de datos. Permite gestionar un listado de clientes con operaciones básicas CRUD (Crear, Leer, Actualizar, Eliminar).


## 🧰 Tecnologías utilizadas

- Python 3.x
- Tkinter (interfaz gráfica)
- MySQL (base de datos relacional)
- `mysql-connector-python` (para conectarse a MySQL)

## ⚙️ Funcionalidades

- ✅ Crear registros de clientes.
- 📋 Mostrar todos los registros en una tabla (`Treeview`).
- ✏️ Editar registros existentes.
- ❌ Eliminar registros.
- Interfaz gráfica intuitiva y funcional.

## 📁 Estructura del proyecto
```bash
📦 crud-clientes/
├── pythonMySql.py # Código principal de la interfaz
├── Clientes.py # Contiene la clase CClientes con lógica de base de datos
├── Conexion.py # Módulo para conexión a la base de datos MyS
```
## 🗄️ Requisitos

- Python 3.x
- Servidor MySQL activo
- Instalar el conector de MySQL:
```bash
pip install mysql-connector-python
```
## 🧱 Estructura de la tabla en MySQL

```bash
CREATE DATABASE clientesbd;

USE clientesbd;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombres VARCHAR(50),
    apellidos VARCHAR(50),
    sexo VARCHAR(20)
);

```

## 🔧 Mejoras sugeridas
- Validación de entradas antes de guardar/modificar.

- Filtro/búsqueda por nombre o apellido.

- Mejorar el estilo visual (temas de Tkinter).

- Exportar datos a CSV.

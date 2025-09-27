# PowerLab - Sistema de Gestión de Gimnasios

Este proyecto es una práctica de **Programación Orientada a Objetos en Python**, cuyo objetivo es diseñar e implementar un sistema básico de gestión para la cadena de gimnasios *PowerLab*. El sistema se ejecuta en consola e implementa menús interactivos para la administración de sucursales, instructores, clientes, mediciones, rutinas y clases grupales.

---

## 📌 Objetivos

* Aplicar principios de POO en Python.
* Diseñar e implementar clases con atributos, métodos y relaciones.
* Utilizar colecciones (listas) para manejar objetos.
* Implementar cálculos específicos: IMC, recomendaciones de proteínas y vasos de agua.
* Construir un menú en consola para interactuar con el sistema.

---

## 📂 Estructura del Proyecto

```
PowerLab/
│── main.py                # Punto de entrada con el menú principal
│── clases/
│   ├── Sucursal.py        # Clase Sucursal
│   ├── Instructor.py      # Clase Instructor
│   ├── Cliente.py         # Clase Cliente
│   ├── Medicion.py        # Clase Medicion
│   ├── Rutina.py          # Clase Rutina
│   ├── ClaseGrupal.py     # Clase Clase Grupal
│   └── CRUD.py            # Funciones auxiliares para operaciones CRUD
```

---

## 🏗️ Funcionalidades principales

1. **Gestión de Sucursales**

   * Registrar, listar, buscar, actualizar y eliminar sucursales.

2. **Gestión de Instructores**

   * Registrar instructores por sucursal.
   * Listar y buscar instructores.

3. **Gestión de Clientes**

   * Registrar clientes en una sucursal.
   * Asignarles un instructor.
   * Listar, buscar, actualizar y eliminar clientes.

4. **Registro de Mediciones**

   * Añadir mediciones periódicas a un cliente.
   * Calcular y mostrar reporte con IMC, clasificación, recomendación de proteínas y vasos de agua.
   * Guardar historial de hasta 10 mediciones por cliente.

5. **Gestión de Clases Grupales**

   * Crear clases grupales en una sucursal (máx. 8 por sucursal).
   * Matricular clientes (máx. 3 por cliente y respetando capacidad).

6. **Generación de Rutinas**

   * Crear rutinas de entrenamiento personalizadas para un cliente.
   * Dividir ejercicios por áreas musculares: pecho y tríceps, bíceps, piernas y espalda.

---

## ⚙️ Requisitos

* Python 3.8 o superior
* Sistema operativo con soporte para ejecución en consola (Windows, Linux, MacOS)

---

## ▶️ Ejecución

Desde la carpeta principal del proyecto:

```bash
python main.py
```

Esto abrirá el menú principal en consola con las siguientes opciones:

```
1. Gestión de Sucursales
2. Gestión de Instructores
3. Gestión de Clientes
4. Registro de Mediciones
5. Gestión de Clases Grupales
6. Generar Rutinas
7. Salir
```

---

## 📖 Notas finales

* El proyecto trabaja completamente en **memoria**: los datos no se guardan en archivos o bases de datos.
* El enfoque principal es demostrar el uso de **POO, relaciones entre clases y CRUD básico en consola**.
* Se implementaron validaciones simples para cupos, límites de clases y cantidad de mediciones.

---

✍️ Proyecto desarrollado como práctica académica de Programación Orientada a Objetos (Python).

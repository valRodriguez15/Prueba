# Documentación del Proyecto

## 1. Arquitectura
Patrón Arquitectónico Modelo-Vista-Plantilla 
Describiendo estos conceptos:
  1. Modelo: Representa una estructura en donde se definen los atributos
  y la lógica de negocio, esto permite la interacción con las bases de datos.
  2. Vista: Gestiona la lógica de presentación, se definen los puntos de
  interacción con el usuario. Estas vistas se resumen en funciones que reciben
  y envian solicitudes y respuestas a la web.
  3. Plantilla: Define la presentación de los datos, estas son archivos .HTML
  que pueden contener etiquetas de plantilla Django para mostrar datos dinámicos.

### Tecnologías Usadas
1. Backend
    - Django: Framework para el desarrollo backend (Framework Principal).
    - Django REST Framework (DRF) Para la API
    - SQLite: Base de datos por defecto.
    - Swagger / ReDoc: Documentación de la API
    - Autenticación con usuarios personalizados (users.User)
2. Frontend
   - HTML: Estructura de las plantillas en las categorias.
   - CSS: Estilos y diseño responsivo, incluyendo Bootstrap 5.3
   
## 2. Endpoints
Se encuentran definidos en http://127.0.0.1:8000/docs/

## 3. Manual de Ejecución
Root url: http://127.0.0.1:8000/categories/
### Instrucciones de Instalación
- Python 3.8+
- pip

En Windows:
1. Crear un entorno virtual: python -m venv env
2. Activar el entorno virtual: .\envs\env\Scripts\activate
3. Instalar dependencias: pip install -r requirements.txt

### Ejecutar el Proyecto
1. Realizar migraciones: python manage.py migrate

### Crear un Superusuario (Opcional)
1. Crear usuario: python manage.py createsuperuser

### Pruebas
1. Ejecutar pruebas: python manage.py test

### Ejecutar
1. Ejecutar el servidor: python manage.py runserver


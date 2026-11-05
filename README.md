# Certamen N°2 - Fundación Patrimonio Vivo
**Asignatura:** EIN082B - Taller de Lenguaje de Programación  
**Carrera:** Ingeniería en Informática | Universidad Técnica Federico Santa María  
**Estudiante:** Luciano Yáñez  
**Profesor/a:** Pamela Gatica Caballero  

---

## Descripción del Proyecto
Aplicación web desarrollada con Python y Django Framework para la Fundación Patrimonio Vivo, orientada a identificar, documentar y difundir lugares de valor patrimonial, histórico y cultural a lo largo de Chile.

El sistema cuenta con un catálogo público dinámico clasificado por categorías, y un área de gestión interna protegida con control de acceso granular y seguridad basada en roles y permisos.

---

## Matriz de Requisitos Funcionales

| Código | Requisito | Estado | Implementación |
| :--- | :--- | :--- | :--- |
| **RF01** | Página principal | Cumplido | Presentación institucional, estadísticas de registros y accesos directos (`/`) |
| **RF02** | Catálogo patrimonial | Cumplido | Listado dinámico de lugares con imágenes y especificaciones técnicas (`/catalogo/`) |
| **RF03** | Detalle de lugar | Cumplido | Ficha individual completa de cada lugar registrado (`/lugar/<id>/`) |
| **RF04** | Categorías | Cumplido | Listado de clasificación patrimonial con conteo dinámico de lugares (`/categorias/`) |
| **RF05** | Filtro | Cumplido | Filtrado de lugares por categoría (`/catalogo/categoria/<id>/`) |
| **RF06** | Administración | Cumplido | Django Admin personalizado con filtros laterales, buscador y paginación (`/admin/`) |
| **RF07** | Interfaz | Cumplido | Bootstrap 5, plantillas reutilizables (`base.html`) y recursos estáticos desacoplados (`estilos.css`) |
| **RF08** | Inicio de sesión | Cumplido | Login de usuarios mediante módulo de autenticación nativo de Django (`/login/`) |
| **RF09** | Cierre de sesión | Cumplido | Cierre de sesión seguro mediante petición POST (`/logout/`) |
| **RF10** | Acceso restringido | Cumplido | Sección de gestión patrimonial protegida mediante decorador `@login_required` (`/gestion/`) |
| **RF11** | Autorización | Cumplido | Formularios para agregar y modificar lugares patrimoniales condicionados a permisos específicos |
| **RF12** | Control de acceso | Cumplido | Protección estricta con `@permission_required(..., raise_exception=True)` que genera una excepción HTTP 403 Forbidden al intentar acceder por URL directa sin contar con los permisos requeridos |

---

## Guía de Instalación y Ejecución

Instrucciones para desplegar y ejecutar el proyecto en un entorno local:

### 1. Clonar el repositorio y acceder al directorio
```bash
git clone https://github.com/TU_USUARIO/CER2-YANEZLUCIANO.git
cd CER2-YANEZLUCIANO
```

### 2. Crear y activar el entorno virtual
En Linux / macOS:
```bash
python3 -m venv env
source env/bin/activate
```
En Windows:
```bash
python -m venv env
env\Scripts\activate
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar las migraciones del esquema de base de datos
```bash
python manage.py migrate
```

### 5. Cargar los datos de prueba (Fixtures)
```bash
python manage.py loaddata datos_iniciales.json
```

### 6. Configurar usuarios y roles de prueba
```bash
python manage.py crear_usuarios
```

### 7. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```
La aplicación se encuentra disponible en: `http://127.0.0.1:8000/`

---

## Credenciales y Matriz de Pruebas de Usuarios

El comando `crear_usuarios` genera los siguientes perfiles para validar el control de acceso:

* **Usuario: admin**
  * **Contraseña:** `admin123`
  * **Rol:** Superusuario
  * **Permisos:** Acceso total al panel de administración (`/admin/`), catálogo público y área de gestión interna.

* **Usuario: gestor**
  * **Contraseña:** `gestor123`
  * **Rol:** Grupo Gestores de Patrimonio
  * **Permisos:** Acceso al Área de Gestión (`/gestion/`). Cuenta con permisos `add_lugarpatrimonial` y `change_lugarpatrimonial` para crear y editar lugares patrimoniales.

* **Usuario: lector**
  * **Contraseña:** `lector123`
  * **Rol:** Usuario Consultor (Regular)
  * **Permisos:** Usuario autenticado en modo solo lectura en `/gestion/`. No visualiza botones para agregar ni editar. Si intenta ingresar por URL directa a `/gestion/crear/`, el sistema retorna error `403 Forbidden` (cumpliendo el requisito RF12).

* **Visitante Anónimo**
  * **Contraseña:** Ninguna
  * **Rol:** Visitante General
  * **Permisos:** Acceso exclusivo a vistas públicas. Si intenta acceder a `/gestion/`, es redirigido automáticamente a la pantalla de login (cumpliendo el requisito RF10).

---

## Arquitectura y Modelo de Datos

El diseño de datos cumple con el diagrama propuesto en el certamen, implementando dos modelos relacionados mediante clave foránea (ForeignKey):

* **Categoria:**
  * `id`: Clave primaria autoincremental.
  * `nombre`: CharField(max_length=100).
  * `descripcion`: TextField().

* **LugarPatrimonial:**
  * `id`: Clave primaria autoincremental.
  * `nombre`: CharField(max_length=200).
  * `descripcion`: TextField().
  * `ubicacion`: CharField(max_length=200).
  * `anio_construccion`: PositiveIntegerField().
  * `imagen`: URLField(max_length=500).
  * `categoria`: ForeignKey hacia `Categoria` con `on_delete=models.CASCADE` y `related_name='lugares'`.
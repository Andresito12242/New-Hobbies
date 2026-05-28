# New Hobbies - Sistema de Recomendación Semántico 🎯

## 📝 Descripción del Proyecto
El proyecto consiste en el desarrollo de un sistema de recomendación de hobbies personalizados que, mediante el uso de tecnologías de la web semántica, permita identificar actividades según los intereses, rasgos y preferencias del usuario. 

A diferencia de sistemas tradicionales, este modelará relaciones conceptuales entre habilidades, intereses y tipos de actividades (como senderismo o cerámica), utilizando estructuras semánticas que permitan la inferencia de recomendaciones no evidentes. El sistema será capaz de sugerir hobbies novedosos partiendo de relaciones indirectas entre características del usuario y propiedades de las actividades.

## 👥 Equipo de Desarrollo
* Andrés Felipe Montoya
* Maria Ximena Osorno

## 🎯 Objetivos
* **General:** Desarrollar un sistema de recomendación de hobbies basado en tecnologías de la web semántica capaz de inferir actividades personalizadas a partir de la relación entre intereses, habilidades y perfiles de usuario.
* **Específicos:** * Diseñar una ontología que represente hobbies, habilidades, intereses y características del usuario.
  * Implementar mecanismos de inferencia que generen recomendaciones a partir de relaciones directas e indirectas.
  * Desarrollar una interfaz gráfica para la interacción del usuario con el sistema.

## 🏗️ Ontología y Diseño Semántico
El diseño se basa en el namespace principal `http://www.newhobbies.org/ontology/` y consta de las siguientes clases conceptuales:
* `Persona`: El usuario que interactúa con el sistema.
* `Hobbie`: La actividad final a recomendar.
* `Interes`: Gustos temáticos explícitos.
* `Habilidad`: Capacidades o destrezas requeridas o poseídas.
* `Nivel`: Grado de exigencia o experiencia (físico, técnico, etc.).
* `Rasgo`: Características de personalidad (creatividad, socialización, etc.).

**Propiedades de relación (Object Properties):** `tieneInteres`, `poseeHabilidad`, `tieneRasgo`, `requiereInteres`, `requiereHabilidad`.

## 🧠 Implementación de Agentes Inteligentes
El núcleo del proyecto se divide en dos agentes integrados con tecnologías de la Web Semántica:
1. **Agente de Perfil de Usuario:** Captura las preferencias a través de la interfaz web en Django. Utilizando la librería **RDFLib**, transforma estos datos relacionales en tripletas semánticas (Sujeto - Predicado - Objeto) y las almacena dinámicamente en un archivo local (`perfiles_usuarios.ttl`).
2. **Agente de Recomendación:** Al solicitar una sugerencia, este agente carga el grafo del usuario y el catálogo base de actividades (`hobbies_base.ttl`). Mediante **consultas SPARQL**, infiere y recupera los hobbies cuyos requisitos de habilidades e intereses hacen "match" exacto con el perfil del usuario, devolviendo el resultado a la vista de Django.

## 🚀 Tecnologías
* **Backend:** Python y framework Django.
* **Web Semántica:** Librería RDFLib y lenguaje de consultas SPARQL.
* **Frontend:** HTML5 y CSS3 con soporte de Bootstrap 5.

## 📈 Estado del Proyecto
- [x] **Fase de Diseño:** Definición de objetivos, descripción y clases de la ontología.
- [x] **Entorno de Desarrollo:** Configuración de Django, entorno virtual y estructura del proyecto.
- [x] **Control de Acceso:** Implementación de sistema de autenticación (Login/Registro) con interfaz limpia.
- [x] **Interfaz de Usuario:** Implementación del formulario de captura de preferencias.
- [x] **Persistencia Semántica:** Integración de RDFLib para mapear y guardar preferencias en formato RDF/Turtle (`.ttl`).
- [x] **Agente de Recomendación:** Implementación de lógica de inferencia mediante consultas SPARQL y conexión con la UI.
- [x] **Control de Versiones:** Repositorio documentado y sincronizado en GitHub.

## 💻 Instrucciones de Ejecución Local

**1. Clonar el repositorio**
```text
git clone [https://github.com/Andresito12242/New-Hobbies.git](https://github.com/Andresito12242/New-Hobbies.git)
cd New-Hobbies
```

**2. Crear y activar el entorno virtual**
```text
python -m venv venv
# Windows: venv\Scripts\activate | Mac/Linux: source venv/bin/activate
```

**3. Instalar dependencias y ejecutar**
```text
pip install django rdflib
python manage.py runserver
```

El proyecto estará disponible en: http://127.0.0.1:8000/
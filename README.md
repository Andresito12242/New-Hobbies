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

## 🏗️ Ontología (Clases Principales)
El diseño se basa en las siguientes clases conceptuales:
* `Persona`: El usuario que interactúa con el sistema.
* `Hobbie`: La actividad final a recomendar.
* `Interes`: Gustos temáticos explícitos.
* `Habilidad`: Capacidades o destrezas requeridas o poseídas.
* `Nivel`: Grado de exigencia o experiencia (físico, técnico, etc.).
* `Rasgo`: Características de personalidad (creatividad, socialización, etc.).

## 🚀 Tecnologías
* **Backend:** Python y el framework Django.
* **Web Semántica:** Librería RDFLib para la manipulación de grafos y modelos RDF.
* **Frontend:** HTML5 y CSS con soporte de Bootstrap.

## 📈 Estado del Proyecto (Avances Actuales)
- [x] **Fase de Diseño:** Definición de objetivos, descripción y clases de la ontología.
- [x] **Entorno de Desarrollo:** Configuración de Django, entorno virtual y estructura del proyecto.
- [x] **Interfaz de Usuario (Agente de Perfil):** Implementación del formulario de captura de preferencias en Django.
- [x] **Control de Versiones:** Repositorio inicial configurado y sincronizado en GitHub.
- [ ] **Persistencia Semántica:** Integración de RDFLib para guardar preferencias en formato RDF/Turtle.
- [ ] **Agente de Recomendación:** Implementación de lógica de inferencia mediante consultas SPARQL.

## 💻 Instrucciones de Ejecución Local

**1. Clonar el repositorio**
```text
git clone [https://github.com/Andresito12242/New-Hobbies.git](https://github.com/Andresito12242/New-Hobbies.git)
cd New-Hobbies
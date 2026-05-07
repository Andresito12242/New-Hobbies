# New Hobbies - Sistema de Recomendación Semántico 🎯

[cite_start]El proyecto tratará del desarrollo de un sistema de recomendación de hobbies personalizados que, mediante el uso de tecnologías de la web semántica, permita identificar actividades según los intereses, rasgos y preferencias del usuario[cite: 57, 60]. 

[cite_start]A diferencia de sistemas tradicionales, nuestro sistema modelará relaciones conceptuales utilizando estructuras semánticas que permitan la inferencia de recomendaciones no evidentes, recomendando hobbies novedosos partiendo de relaciones indirectas entre características del usuario y propiedades de las actividades[cite: 61, 62].

## 👥 Equipo de Desarrollo
* Andrés Felipe Montoya
* Maria Ximena Osorno

## 🧩 Componentes del Sistema

El proyecto integra dos pilares fundamentales:
1. **Agentes Inteligentes**:
   * [cite_start]**Agente de Perfil de Usuario**: Recolecta y actualiza las preferencias del usuario basadas en sus interacciones a través de la interfaz web[cite: 112].
   * [cite_start]**Agente de Recomendación**: Utiliza los perfiles y los datos de contenido semántico para generar recomendaciones personalizadas[cite: 113].
2. **Tecnologías del Web Semántico**:
   * [cite_start]**Modelo RDF y Ontologías OWL**: Representación de datos estructurados para usuarios, actividades y sus relaciones conceptuales[cite: 115, 116].
   * [cite_start]**SPARQL**: Lenguaje de consulta utilizado por el agente de recomendación para navegar las tripletas y extraer conocimiento[cite: 117].

## 🏗️ Ontología (Clases Principales)
[cite_start]El sistema basa sus inferencias en las siguientes clases[cite: 66, 67]:
* `Persona`: El usuario del sistema.
* `Hobbie`: La actividad a recomendar.
* `Interes`: Preferencias temáticas directas.
* `Habilidad`: Capacidades físicas o cognitivas.
* `Nivel`: Grado de exigencia (Ej. principiante, avanzado).
* `Rasgo`: Características de personalidad (Ej. creatividad, socialización).

## 🚀 Tecnologías Utilizadas
* [cite_start]**Backend / Web Framework:** Python con Django[cite: 136, 138].
* **Web Semántica:** RDFLib (Manipulación de grafos en Python).
* **Frontend:** HTML5, CSS3 (Bootstrap).

## 💻 Instrucciones de Ejecución Local

Sigue estos pasos para levantar el entorno de desarrollo en tu máquina:

**1. Clonar el repositorio**
```bash
git clone [https://github.com/TU_USUARIO/New-Hobbies.git](https://github.com/TU_USUARIO/New-Hobbies.git)
cd New-Hobbies
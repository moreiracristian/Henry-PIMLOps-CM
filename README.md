# Sistema de recomendación de relículas con FastAPI 🎥

Este proyecto es una API desarrollada con **FastAPI** que permite realizar diversas consultas sobre una base de datos de películas y obtener recomendaciones analisis basadas en similitudes de géneros combinando procesamiento de datos y machine learning. Está diseñada para explorar datos procesados y proporcionar información útil de manera rápida y eficiente.

---

## Tecnologías Utilizadas 

- **FastAPI**: Framework para la creación de APIs rápidas y eficientes.
- **Pandas**: Procesamiento y manipulación de datos.
- **Scikit-learn**: Modelado y recomendación utilizando `NearestNeighbors`
- **OneHotEncoder**: Codificación de géneros para el modelo de recomendación.
- **Python**: Lenguaje principal del proyecto.

---

## Instalación 🛠️

1. Clona el repositorio:
    ```bash
    git clone https://github.com/moreiracristian/Henry-PIMLOps-CM.git
    cd Henry-PIMLOps-CM
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate    # En Linux/Mac
    venv\Scripts\activate       # En Windows
    ```

3. Instala las dependencias necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4. Asegúrate de que los datos necesarios están en el directorio `data/procesado`:
   - `credits_pilabs.parquet`
   - `movies_pilabs.parquet`

---

## Características principales ✨

1. **Consultas de estadísticas por fechas:**
   - Número de películas estrenadas en un mes o día específico.
   
2. **Búsqueda de detalles de películas:**
   - Score, año de estreno y número de votos.

3. **Análisis de contribución:**
   - Información sobre actores y directores, incluyendo métricas de retorno financiero.

4. **Sistema de recomendación:**
   - Basado en similitudes de género utilizando el algoritmo `Nearest Neighbors`.

---

## Endpoints 🚀

### 1. **Cantidad de Filmaciones por Mes**
    
- Ruta: `/cantidad_filmaciones_mes/{mes}`
- Descripción: Retorna la cantidad de películas estrenadas en un mes específico.
- Ejemplo: `/cantidad_filmaciones_mes/enero`

### 2. **Cantidad de Filmaciones por Día**
    
- Ruta: `/cantidad_filmaciones_dia/{dia}`
- Descripción: Retorna la cantidad de películas estrenadas en un día específico de la semana.
- Ejemplo: `/cantidad_filmaciones_dia/lunes`
    

### 3. **Score de una Película**
    
- Ruta: `/score_titulo/{titulo_de_la_filmacion}`
- Descripción: Muestra el título, año de estreno y popularidad de una película.
- Ejemplo: `/score_titulo/Titanic`
    

### 4. **Votos de una Película**
    
- Ruta: `/votos_titulo/{titulo_de_la_filmacion}`
- Descripción: Retorna la cantidad de votos, promedio y año de estreno de una película.
- Ejemplo: `/votos_titulo/Titanic`
    

### 5. **Información de un Actor**
    
- Ruta: `/get_actor/{nombre_actor}`
- Descripción: Detalla la cantidad de filmaciones, retorno total y promedio de un actor.
- Ejemplo: `/get_actor/Leonardo%20DiCaprio`
    

### 6. **Información de un Director**
    
- Ruta: `/get_director/{nombre_director}`
- Descripción: Proporciona datos de las películas dirigidas por un director, incluyendo presupuesto, ingresos y retorno.
- Ejemplo: `/get_director/Christopher%20Nolan`
    

### 7. **Recomendación de Películas**
    
- Ruta: `/recommend/`
- Parámetros:
    - `movie_title` (str): Título de la película de referencia.
    - `num_recommendations` (int, opcional): Número de recomendaciones (por defecto 5).
- Descripción: Genera una lista de películas similares en base a géneros.
- Ejemplo: `/recommend/?movie_title=Inception&num_recommendations=5`
    
---

## Arquitectura del Proyecto
   
    📁 data/
    └── 📁 procesado/
        ├── credits_pilabs.parquet
        └── movies_pilabs.parquet
    📁 notebooks/
        ├── 📄 etl_credits.ipynb
        ├── 📄 etl_movies.ipynb
        └── 📄 modelo.ipynb
    📁 reports/
        └── 📄 eda.ipynb
    📁 src/
        └── 📄 requirements.txt
    📄 main.py
    
---

## Detalles Técnicos

1. **Preprocesamiento:**

    - Los archivos `parquet` son leídos y procesados con `pandas`
    - La columna `release_date` se convierte a formato `datetime` para consultas temporales.
    - Los géneros son codificados mediante `OneHotEncoder` para alimentar al modelo de recomendaciones.
    
2. **Modelo de Recomendación:**

    - Se utiliza `NearestNeighbors` con métrica de similitud coseno para encontrar películas similares.
    
---

## Requisitos del Sistema 🖥️

- Python 3.9+
- FastAPI
- Pandas
- Scikit-learn
- Archivos parquet con los datos procesados.

---

## Ejecución del Proyecto ▶️

1. Inicia la aplicación FastAPI:
    ```bash
    uvicorn main:app --reload
    ```

2. Accede a la documentación interactiva de la API en: http://127.0.0.1:8000/docs

3. Explora los endpoints y prueba sus funcionalidades.

---

## Autor 🧑‍💻

### PIMLOps Henry
### Proyecto de Cristian Moreira
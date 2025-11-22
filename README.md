# UDB_MLS629
Proyecto de Materia de Machine Learning no Supervisado [MLS629] - Cohorte I - 2025

## Integrantes
Alfredo Argueta Interiano - AI252944
Giovanni Alexander Escobar - EM252920
Ivo Luis Orellana Girón - OG252913
Marlon Alexander Palacios Díaz - PD252876
José Rodrigo López Torres - LT170438


# Proyecto Final: Análisis Avanzado con Aprendizaje No Supervisado 

## 🚀📜 Descripción del Proyecto

Este proyecto consiste en desarrollar un análisis avanzado de aprendizaje no supervisado utilizando un conjunto de datos real de su elección. El objetivo es integrar dos metodologías principales para explorar la estructura subyacente de los datos, justificar las decisiones tomadas y proporcionar insights accionables.

1. Reducción de Dimensionalidad Aplicación: Implementación de al menos dos técnicas diferentes (e.g., PCA, t-SNE, UMAP).Análisis: Realizar una comparación rigurosa, justificar la mejor técnica para la representación de los datos, e incluir visualizaciones interpretables y métricas de evaluación.

2. Clustering (Segmentación) Implementación: Aplicación de al menos dos algoritmos de clustering distintos (e.g., K-means, DBSCAN, Agglomerative Clustering).Evaluación: Evaluación exhaustiva usando múltiples métricas internas (Silueta, Davies-Bouldin, Calinski-Harabasz, etc.).Interpretación: Caracterización detallada de los clusters obtenidos en el contexto del dominio de aplicación.

## 📂 Estructura del repositorio

Aquí un resumen de la organización del proyecto:
├── dataset/ # Datos utilizados en el proyecto
│ ├── Fintech_Trans_Agosto_Octubre_2025.csv # Dataset principal Datos en bruto (sin procesar)
│ └── Fintech_EDA.csv # Datos intermedios luego de limpieza y transformacion solo 3 columnas para segmentacion por monto
│ └── Fintech_Features.csv # Datos preparados para modelos
│
├── documentacion/ # Información adicional y documentación de la investigación
│ └── (Resultados notebooks en formato .html)
│
├── modules/ # Código modularizado (clases, funciones, pipelines)
│ ├── (Funciones de utileria)
│
├── notebooks/ # Notebooks con experimentos, visualizaciones y análisis
│ ├── 01_Exploracion_Inicial.ipynb
│ └── 02_Reduccion_dimensionalidad.ipynb
│ └── 03_Clustering.ipynb
│ └── 04_Experimentos_Segmentacion_por_Montos.ipynb
│
├── LICENSE # Licencia del proyecto (MIT)
│
└── README.md # Este archivo



## 🔧 Instalación

Para correr el proyecto en tu máquina local, sigue estos pasos:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Alex-Palacios/UDB_MLS629.git
    cd UDB_MLS629
    ```

2. Instala las dependencias:

    ```bash
    pip install "nombre_lib"
    ```
    Librerias: 
       * pandas
       * numpy
       * matplotlib
       * seaborn 
       * scipy
       * sklearn
       * umap

## 🚀 Uso

Aquí te dejo algunas formas de usar el proyecto:

- Abre y ejecuta `notebooks/01_Exploracion_Inicial.ipynb` para ver el análisis exploratorio de los datos.
- Usa `notebooks/02_Reduccion_dimensionalidad.ipynb` para correr distintos algoritmos de reducción de dimensiones (PCA T-snet, etc.).
- Usa `notebooks/03_Clustering.ipynb` para correr distintos algoritmos de clustering (K-means, DBSCAN, etc.).

---

## 🧪 Metodología y modelos

Algunos de los métodos que hemos implementado hasta ahora:

- **Reducción de dimensionalidad:** PCA (Análisis de Componentes Principales)
- **Clustering:** K-means, DBSCAN, (otros por definir)
- **Evaluación:** métricas internas como Silhouette, K, etc.
- **Preprocesamiento:** escalado de variables, limpieza de datos faltantes y atípicos.

---

## 📊 Resultados esperados

- Identificar agrupaciones naturales en los datos con clustering no supervisado.  
- Evaluar la calidad de los clusters usando métricas internas.  
- Visualizar los datos reducidos en 2D o 3D con PCA y clusters agrupados.  
- Generar un reporte o documento con hallazgos, limitaciones y recomendaciones.

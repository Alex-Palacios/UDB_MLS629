import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_analysis(df):
    ### Análisis de Correlación
    num_cols = df.columns
    correlation_matrix = df.corr()
    
    # Configura el estilo de la figura
    plt.figure(figsize=(20, 2*len(num_cols)))
    
    # Crea un mapa de calor con seaborn
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    
    # Añade título
    plt.title("Matriz de Correlación")
    
    # Muestra la visualización
    plt.show()



def boxplot_analysis(df):
    num_cols = df.columns

    # Crear subgráficos
    fig, axes = plt.subplots(nrows=len(num_cols), figsize=(10, 2*len(num_cols)))
    
    # Generar boxplots individuales
    for i, col in enumerate(num_cols):
        sns.boxplot(x=df[col], ax=axes[i])
        axes[i].set_title(col)
    
    plt.tight_layout()
    plt.show()
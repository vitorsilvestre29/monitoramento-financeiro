import matplotlib.pyplot as plt
import pandas as pd
from conexaobase import fetch_data

def plot_receita_categoria(df):
    """
    Gráfico de barras para mostrar a receita por categoria.
    """
    plt.figure(figsize=(10, 6))
    df.groupby('categoria')['valor'].sum().plot(kind='bar', color='skyblue')
    plt.title('Receita por Categoria', fontsize=14)
    plt.ylabel('Valor (R$)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

def plot_fluxo(df):
    """
    Gráfico de pizza para mostrar a distribuição do fluxo de caixa.
    """
    plt.figure(figsize=(8, 8))
    df.groupby('categoria')['valor'].sum().plot(kind='pie', autopct='%1.1f%%', startangle=90, cmap='Set2')
    plt.title('Distribuição do Fluxo de Caixa', fontsize=14)
    plt.ylabel('')
    plt.tight_layout()

def plot_dashboard():
    
  
    
    # Carregar dados de Receita
    query_receita = "SELECT * FROM Receita"  
    receita_data = fetch_data(query_receita)
    if receita_data is not None:
        plot_receita_categoria(receita_data)

    # Carregar dados de Fluxo de Caixa
    query_fluxo = "SELECT * FROM Fluxo_Caixa"  
    fluxo_data = fetch_data(query_fluxo)
    if fluxo_data is not None:
        plot_fluxo(fluxo_data)

    # Exibe os gráficos gerados
    plt.show()

# Executar o dashboard
plot_dashboard()

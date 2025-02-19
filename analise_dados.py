import pandas as pd
from conexaobase import fetch_data

def analyze_receita(df):
   
    total_receita = df['valor'].sum()
    print(f"Total de Receita: {total_receita:.2f}")
    return total_receita

def analyze_fluxo(df):
   
    total_fluxo = df['valor'].sum()
    print(f"Total de Fluxo de Caixa: {total_fluxo:.2f}")
    return total_fluxo

def run_analysis():
    query = "SELECT * FROM Receita"
    receita_data = fetch_data(query)
    if receita_data is not None:
        analyze_receita(receita_data)
    
    query = "SELECT * FROM Fluxo_Caixa"
    fluxo_data = fetch_data(query)
    if fluxo_data is not None:
        analyze_fluxo(fluxo_data)

run_analysis()

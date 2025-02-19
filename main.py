from conexaobase import fetch_data
import pandas as pd

def main():
    # Defina as consultas SQL para buscar os dados das tabelas
    query_receita = "SELECT * FROM Receita"  
    query_fluxo = "SELECT * FROM FluxoCaixa"  

    # Chama a função fetch_data para recuperar os dados das tabelas
    receita_data = fetch_data(query_receita)
    fluxo_data = fetch_data(query_fluxo)

    # Verifica se os dados de receita foram recuperados com sucesso
    if receita_data is not None:
        print("Dados da Receita:")
        print(receita_data.head())  # Exibe as primeiras linhas dos dados de Receita

    # Verifica se os dados de fluxo de caixa foram recuperados com sucesso
    if fluxo_data is not None:
        print("Dados do Fluxo de Caixa:")
        print(fluxo_data.head())  # Exibe as primeiras linhas dos dados de Fluxo de Caixa

    # Aqui você pode adicionar mais análises ou visualizações dos dados

if __name__ == "__main__":
    main()

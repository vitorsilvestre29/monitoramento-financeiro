# Monitoramento de Indicadores Financeiros

Este projeto é uma solução para o **monitoramento de indicadores financeiros** usando **SQL Server**, **Python** e **Power BI**. 
Ele permite que os usuários visualizem e analisem dados financeiros, como receita, fluxo de caixa, e outros indicadores importantes para uma empresa. 
O projeto foi desenvolvido para demonstrar habilidades de análise de dados, automação e criação de dashboards interativos.

## Funcionalidades

- **Leitura e Análise de Dados**: Conexão com o banco de dados SQL Server para coleta de dados financeiros.
- **Dashboard Interativo**: Criação de visualizações e indicadores financeiros usando Power BI.
- **Automação com Python**: Scripts para processar e analisar dados financeiros de forma automatizada.

## Tecnologias Usadas

- **SQL Server**: Para armazenamento de dados financeiros.
- **Python**: Para análise de dados e automação.
  - Bibliotecas: `pandas`, `pyodbc`, `matplotlib`
- **Power BI**: Para criação de dashboards interativos.

## Como Executar o Projeto

### Pré-requisitos

1. **Instalar o Python** 
2. **Instalar as dependências do projeto**:
   - Execute o comando abaixo para instalar as bibliotecas necessárias:

     ```bash
     pip install pandas pyodbc matplotlib
     ```

3. **Configuração do SQL Server**:
   - Configure o **SQL Server** e crie as tabelas de dados (`fluxo_caixa`, `receita`, etc.) conforme os scripts fornecidos.
   - Certifique-se de que o banco de dados está acessível para o script Python.
   
### Passos para Executar:

1. Clone o repositório:

   ```bash
   git clone https://github.com/vitorsilvestre29/monitoramento-financeiro.git

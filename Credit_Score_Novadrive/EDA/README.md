# Documentação do Projeto Credit Score Novadrive

Este projeto tem como objetivo realizar a análise de dados de crédito utilizando ferramentas de Python para a geração de relatórios automatizados de análise exploratória de dados (EDA) com as bibliotecas **Pandas Profiling** e **Sweetviz**. Os dados são obtidos de um banco de dados PostgreSQL, manipulados em um DataFrame e armazenados como um arquivo CSV.

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

```
D:\Repositories\Data-Science\Credit_Score_Novadrive\
|
├── data\
│   └── raw_data\
│       └── data.csv                      # Dados exportados do banco
|
├── EDA\
│   ├── eda_reports\
│   │   ├── pandas_profiling_report.html  # Relatório gerado pelo Pandas Profiling
│   │   └── sweetviz_report.html          # Relatório gerado pelo Sweetviz
│   ├── config.yaml                       # Arquivo de configuração do banco de dados
│   ├── const.py                          # Configurações e caminhos do projeto
│   ├── pandas_profiling_analysis.py      # Script para gerar relatório Pandas Profiling
│   └── sweetviz_analysis.py              # Script para gerar relatório Sweetviz
│
├── queries\
│   ├── data_denormalization.sql          # Query SQL para normalização dos dados
│   └── tables_analysis.sql               # Query SQL para análise de tabelas
```

## Dependências

As bibliotecas e ferramentas necessárias para o projeto incluem:

- **Python** (>=3.9)
- **Pandas**
- **Sweetviz**
- **Pandas Profiling**
- **PyYAML**
- **psycopg2**
- **PostgreSQL**

Instale as dependências utilizando:
```bash
pip install pandas sweetviz pandas-profiling pyyaml psycopg2
```

## Configuração do Banco de Dados

O arquivo `config.yaml` contém as credenciais de acesso ao banco de dados PostgreSQL. Certifique-se de configurá-lo corretamente antes de executar os scripts.

Exemplo de `config.yaml`:
```yaml
database_config:
  host: "localhost"
  dbname: "credit_score_db"
  user: "seu_usuario"
  password: "sua_senha"
```

## Descrição dos Arquivos

### 1. `const.py`
Define os caminhos principais do projeto e carrega a consulta SQL a partir de `queries/data_denormalization.sql`.

### 2. `utils.py`
Contém a função `fetch_data_from_db`, responsável por conectar ao banco de dados, executar a consulta SQL e salvar os dados como um arquivo CSV.
- **Conexão com o banco**: utiliza a biblioteca `psycopg2` para estabelecer conexão com o PostgreSQL.
- **Execução da consulta**: executa a SQL fornecida e converte o resultado em um DataFrame do Pandas.
- **Exportação para CSV**: salva os dados em formato CSV para reutilização.

### 3. `pandas_profiling_analysis.py`
Gera o relatório exploratório utilizando **Pandas Profiling** e salva o relatório no diretório `eda_reports`.
- **Função principal**: carrega os dados do arquivo CSV e aplica a ferramenta de análise para gerar o relatório.

### 4. `sweetviz_analysis.py`
Gera o relatório exploratório utilizando **Sweetviz** e salva o relatório no diretório `eda_reports`.
- **Função principal**: carrega os dados, configura a análise e exporta o relatório como HTML.

### 5. `queries/data_denormalization.sql`
Contém a consulta SQL utilizada para buscar e normalizar os dados do banco.
- **Estrutura da query**: desnormaliza tabelas relevantes para facilitar a análise.

## Como Executar

1. **Configurar o Banco de Dados**:
   Certifique-se de que o arquivo `config.yaml` está configurado corretamente com as credenciais do banco.

2. **Executar o Script de Sweetviz**:
   ```bash
   python D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\sweetviz_analysis.py
   ```

3. **Executar o Script de Pandas Profiling**:
   ```bash
   python D:\Repositories\Data-Science\Credit_Score_Novadrive\EDA\pandas_profiling_analysis.py
   ```

4. **Verificar os Relatórios**:
   - **Sweetviz**: `EDA\eda_reports\sweetviz_report.html`
   - **Pandas Profiling**: `EDA\eda_reports\pandas_profiling_report.html`

## Logs e Depuração

Caso algum erro ocorra, verifique os logs gerados pelo `utils.py` e as mensagens de erro exibidas ao executar os scripts.

## Melhorias Futuras

- Limpeza, Tratamento e Pré-Processamento dos Dados para o Modelo.
- Criação do Modelo e Avaliação de Perfomance.
- Desenvolver Aspectos de Explicabilidade.
- Criar API para Servir o Modelo.
- Realizar o Deploy na Web e Testar a API.
- Publicar e melhorar o README.md

## Contato

Para dúvidas ou sugestões, entre em contato com Thiago Alves.

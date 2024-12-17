# Análise Exploratória de Dados com Streamlit

## Descrição do Projeto

Este projeto consiste em uma aplicação web desenvolvida com **Streamlit** para realizar análises exploratórias de dados sobre despesas empenhadas em relação ao **PIB (Produto Interno Bruto)**. A aplicação apresenta diferentes formas de visualização, como resumos estatísticos, histogramas, boxplots e gráficos interativos, permitindo identificar os maiores valores e suas proporções de forma clara e intuitiva.

---

## Funcionalidades Principais

- **Resumo dos Dados**: Estatísticas descritivas sobre as variáveis do conjunto de dados.
- **Distribuição dos Dados**: Visualização com histogramas e boxplots para as variáveis `VALOREMPENHO` (valor empenhado) e `PIB`.
- **Maiores Valores**: Identificação dos maiores valores de despesas empenhadas, PIB e proporção entre valor empenhado e PIB, por município.

---

## Estrutura do Código

### Configuração Inicial

- **Título da Página e Layout**: Configurações iniciais do Streamlit.

```python
st.set_page_config(page_title="Análise Exploratória de Dados", layout="wide")
st.title("Despesas empenhadas e relação com o PIB")
```

### Carregamento dos Dados

- **Função `load_data`**: Carrega o arquivo CSV, calcula a proporção `VALOREMPENHO/PIB` e utiliza o cache para otimizar o desempenho.

```python
@st.cache_data
def load_data():
    data = pd.read_csv(r"(yourpath)\\data.csv", sep=";")
    data['PROPORCAO'] = data['VALOREMPENHO'] / data['PIB']
    return data
```

### Interface do Usuário

#### Barra Lateral

- **Configuração Interativa**: O usuário define o número de entradas a serem exibidas.

```python
with st.sidebar:
    st.header("Configurações")
    top_n = st.number_input("Selecione o número de entradas para exibir", min_value=1, max_value=len(data), value=10)
```

#### Abas Interativas

1. **Visão Geral**: Apresenta o resumo estatístico dos dados.

```python
with tab1:
    st.header("Resumo dos Dados")
    st.write(data.describe())
```

2. **Análise Detalhada**: Visualiza as distribuições com histogramas e boxplots.

```python
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.histogram(data, x='VALOREMPENHO', title="Histograma do Valor Empenhado")
        st.plotly_chart(fig1, use_container_width=True)
```

3. **Maiores Valores**: Identifica os maiores valores e os exibe em gráficos.

```python
with tab3:
    col1, col2, col3 = st.columns(3)
    with col1:
        hg_commit = data.nlargest(top_n, 'VALOREMPENHO')
        fig = px.bar(hg_commit, x='MUNICIPIO', y='VALOREMPENHO', title="Maiores Valores Empenhados")
        st.plotly_chart(fig, use_container_width=True)
```

---

## Como Executar o Projeto

1. Instale o Python e as bibliotecas necessárias:
   - `streamlit`
   - `pandas`
   - `plotly`

2. Substitua `(yourpath)\\data.csv` pelo caminho completo do seu arquivo CSV.
3. Execute o comando abaixo no terminal:

```bash
streamlit run app.py
```

4. Acesse o link fornecido pelo terminal no navegador.

---

## Estrutura do Arquivo CSV

O arquivo de dados deve conter as seguintes colunas:

- `MUNICIPIO`: Nome do município.
- `VALOREMPENHO`: Valor empenhado.
- `PIB`: Produto Interno Bruto do município.

---

## Exemplos de Uso

- **Identificar municípios com maior proporção entre despesas e PIB.**
- **Visualizar distribuições dos valores empenhados e PIB.**
- **Gerar insights rápidos sobre dados financeiros municipais.**

---

## Tecnologias Utilizadas

- **Streamlit**: Desenvolvimento da interface web interativa.
- **Pandas**: Manipulação e análise de dados.
- **Plotly**: Visualização gráfica interativa.

---

## Autor

Thiago Menezes Alves

---

**Versão do Projeto**: 1.0


# Análise de Cancelamento de Clientes (Churn Analysis)

Este projeto tem como objetivo analisar os fatores que levam clientes a cancelarem um serviço, utilizando **Python para análise de dados** e **visualização gráfica**.

A partir de uma base de dados contendo informações sobre clientes, foi realizada uma análise exploratória para identificar padrões que influenciam no cancelamento.

---

##  Objetivo do Projeto

Identificar **possíveis causas de cancelamento de clientes (churn)** e gerar insights que possam ajudar empresas a reduzir a perda de clientes.

---

##  Tecnologias Utilizadas

* **Python**
* **Pandas** – Manipulação e análise de dados
* **Plotly Express** – Visualização interativa de dados

---

##  Estrutura do Projeto

```
churn-analysis/
│
├── cancelamentos.csv
├── main.py
└── README.md
```

---

##  Base de Dados

A base utilizada contém informações como:

* tipo de contrato
* quantidade de ligações para o call center
* dias de atraso no pagamento
* status de cancelamento do cliente

---

##  Etapas da Análise

### 1️ Importação dos dados

A base de dados foi carregada utilizando a biblioteca **pandas**.

### 2️ Limpeza da base

Foram removidas:

* colunas irrelevantes (`CustomerID`)
* registros com valores nulos

### 3️ Análise exploratória (EDA)

Foi analisada a taxa geral de cancelamento:

```
df['cancelou'].value_counts(normalize=True)
```

Também foram gerados gráficos para analisar como cada variável impacta no cancelamento.

### 4️ Visualização dos dados

Para cada variável da base foi gerado um **histograma comparando clientes que cancelaram e os que não cancelaram**.

```
for column in df.columns:
    fig = px.histogram(df, x=column, color='cancelou')
```

---

##  Principais Insights

A análise mostrou alguns padrões relevantes:

* Clientes com **contrato mensal** possuem maior taxa de cancelamento.
* Clientes que **ligam mais de 4 vezes para o call center** tendem a cancelar o serviço.
* Clientes com **atraso superior a 20 dias** possuem maior probabilidade de cancelar.

---

##  Possíveis Ações para Reduzir Cancelamentos

Com base nos dados, algumas estratégias podem ser adotadas:

* Oferecer **descontos para planos anuais ou trimestrais**
* Melhorar o atendimento do suporte para **resolver problemas em até 3 ligações**
* Criar uma política financeira para **resolver atrasos antes de 20 dias**

---

## Como Executar o Projeto

1️ Instale as dependências:

```
pip install pandas plotly
```

2️ Execute o script:

```
python analysis.py
```

3️  Os gráficos serão exibidos automaticamente.

---

##  Possíveis Melhorias Futuras

* Criar um **dashboard interativo com Streamlit**
* Aplicar **modelos de Machine Learning para prever churn**
* Integrar com **banco de dados**
* Criar um **pipeline automatizado de análise**

---


Projeto desenvolvido como estudo de **análise de dados com Python**, focado em identificação de padrões de comportamento de clientes e suporte à tomada de decisão baseada em dados.

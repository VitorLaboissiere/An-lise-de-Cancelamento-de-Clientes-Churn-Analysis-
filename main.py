import pandas as pd
import plotly.express as px
# Passo 1: Importar base de dados
df = pd.read_csv('cancelamentos.csv')

# Passo 2: Visualizar base de dados
df = df.drop(columns="CustomerID")
# colunas inúteis - informações que não te ajudam, te atrapalham

# Passo 3: Corrigir cagadas da base de dados
print(df.info())

df = df.dropna()
print(df.info())
# Passo 4: Análise dos cancelamentos
print(df['cancelou'].value_counts(normalize=True))
# Passo 5: Análise da causa dos cancelamentos (como as colunas impactam no cancelamento?)

for column in df.columns:
    fig = px.histogram(df, x=column, color='cancelou')
    fig.show()
# clientes do contrato mensal TODOS cancelam
    # ofercer desconto nos planos anuais e trimestrais
# clientes que ligam mais do que 4 vezes para o call center, cancelam
    # criar um processo para resolver o problema do cliente em no máximo 3 ligações
# clientes que atrasaram mais de 20 dias, cancelaram
    # política de resolver atrasos em até 10 dias (equipe financeira)

df = df[df["duracao_contrato"] != "Monthly"]
df = df[df["ligacoes_callcenter"] <= 4]
df = df[df["dias_atraso"] <= 20]

print(df["cancelou"].value_counts(normalize=True))
# formatar para  porcentagem %
print(df["cancelou"].value_counts(normalize=True).map("{:.2%}".format))

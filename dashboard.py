import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título do dashboard
st.title("Dashboard de Trades")

# Carregar dados de trades (exemplo a partir de um CSV)
# Você pode substituir pelo seu próprio método de carregamento
trades = pd.read_csv("trades.csv")  # Assumindo que existe um arquivo trades.csv

# Exibir a tabela de trades
st.subheader("Tabela de Trades")
st.dataframe(trades)

# Calcular resultado diário
trades['date'] = pd.to_datetime(trades['date'])  # Certifique-se que a coluna 'date' é do tipo datetime
resultado_diario = trades.groupby(trades['date'].dt.date)['profit'].sum()
st.subheader("Resultado Diário")
st.line_chart(resultado_diario)

# Gráfico de evolução de capital
capital_evolucao = trades.groupby(trades['date'].dt.date)['capital'].sum().cumsum()
st.subheader("Evolução de Capital")
plt.figure(figsize=(10, 5))
plt.plot(capital_evolucao.index, capital_evolucao.values)
plt.title("Evolução de Capital ao Longo do Tempo")
plt.xlabel("Data")
plt.ylabel("Capital Acumulado")
st.pyplot(plt)
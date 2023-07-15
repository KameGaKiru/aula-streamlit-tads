import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Título do app
st.title('Stock History App')

# Criando o sidebar
st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# Baixando os dados do Yahoo Finanças
data = yf.download(ticker_symbol, start='2020-01-01', end='2023-06-26')

# Exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico do símbolo fornecido pelo usuário
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Fechamento'))
fig1.update_layout(title=f"{ticker_symbol}", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig1)

# Baixando os dados das Lojas Americanas
lojas_americas_data = yf.download("LAME4.SA", start='2020-01-01', end='2023-06-26')

# Exibir os dados das Lojas Americanas
st.subheader('Histórico das Lojas Americanas')
st.dataframe(lojas_americas_data)

# Exibir o gráfico das Lojas Americanas
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=lojas_americas_data.index, y=lojas_americas_data['Close'], name='Fechamento'))
fig2.update_layout(title="Lojas Americanas", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig2)

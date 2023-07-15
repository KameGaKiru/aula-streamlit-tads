import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

# Título do app
st.title('Stock History App')

# Criando o sidebar
st.sidebar.title('Selecione o stock')
ticker_symbol = st.sidebar.text_input('stock', 'AAPL', max_chars=10)

# Baixando os dados do yahoo finanças
data = yf.download(ticker_symbol, start='2020-01-01', end='2023-06-26')

# Exibir os dados
st.subheader('Histórico')
st.dataframe(data)

# Exibir o gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Fechamento'))
fig.update_layout(title=f"{ticker_symbol}", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig)

# Baixando os dados das ações das Lojas Americanas
ticker_symbol_lojas_americas = "LAME4.SA"
data_lojas_americas = yf.download(ticker_symbol_lojas_americas, start='2020-01-01', end='2023-06-26')

# Exibir os dados das Lojas Americanas
st.subheader('Histórico - Lojas Americanas')
st.dataframe(data_lojas_americas)

# Exibir o gráfico das Lojas Americanas
fig_lojas_americas = go.Figure()
fig_lojas_americas.add_trace(go.Scatter(x=data_lojas_americas.index, y=data_lojas_americas['Close'], name='Fechamento'))
fig_lojas_americas.update_layout(title=f"{ticker_symbol_lojas_americas}", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig_lojas_americas)

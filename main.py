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

# Exibir o gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Fechamento'))
fig.update_layout(title=f"{ticker_symbol}", xaxis_title="Data", yaxis_title="Preço")
st.plotly_chart(fig)

if ticker_symbol.upper() == 'PETR4':
    # Baixando os dados da Petrobras
    data_petrobras = yf.download('PETR4.SA', start='2020-01-01', end='2023-06-26')

    # Exibir o gráfico da Petrobras
    fig_petrobras = go.Figure()
    fig_petrobras.add_trace(go.Scatter(x=data_petrobras.index, y=data_petrobras['Close'], name='Fechamento'))
    fig_petrobras.update_layout(title='Petrobras', xaxis_title='Data', yaxis_title='Preço')
    st.plotly_chart(fig_petrobras)

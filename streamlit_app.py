import plotly.express as px
import streamlit as st
import pandas as pd

st.title("📊 Dashboard de Vendas Interativo")
arquivo = st.file_uploader("📂 Envie a planilha de vendas (.xlsx)", type=["xlsx"])

if arquivo:
    df = pd.read_excel(arquivo)
    df['Data'] = pd.to_datetime(df['Data'])

    df['Faturamento'] = df['Quantidade'] * df['Valor Unitário']

    st.subheader("📅 Filtrar por período")
    col1, col2 = st.columns(2)
    data_inicial = col1.date_input("Data inicial", value=df['Data'].min().date())
    data_final = col2.date_input("Data final", value=df['Data'].max().date())

    df_filtrado = df[
        (df['Data'] >= pd.to_datetime(data_inicial)) & 
        (df['Data'] <= pd.to_datetime(data_final))
    ]

    fig = px.bar(df_filtrado, x="Produto", y="Faturamento", color="Produto", title="Faturamento por Produto")
    st.plotly_chart(fig)

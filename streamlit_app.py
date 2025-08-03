import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")
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

    produtos = df_filtrado['Produto'].unique()
    produtos_selecionados = st.multiselect("🛒 Selecione os produtos", options=produtos, default=produtos)
    df_filtrado = df_filtrado[df_filtrado['Produto'].isin(produtos_selecionados)]

    total_faturado = df_filtrado['Faturamento'].sum()
    total_vendas = df_filtrado['Quantidade'].sum()
    ticket_medio = total_faturado / total_vendas if total_vendas > 0 else 0

    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Faturamento Total", f"R$ {total_faturado:,.2f}")
    col2.metric("🛒 Total de Itens Vendidos", int(total_vendas))
    col3.metric("🎯 Ticket Médio", f"R$ {ticket_medio:,.2f}")

    fig_bar = px.bar(
        df_filtrado,
        x="Produto",
        y="Faturamento",
        color="Produto",
        title="💰 Faturamento por Produto"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    df_diario = df_filtrado.groupby("Data").sum(numeric_only=True).reset_index()
    fig_linha = px.line(
        df_diario,
        x="Data",
        y="Faturamento",
        title="📆 Faturamento por Dia"
    )
    st.plotly_chart(fig_linha, use_container_width=True)

    

    st.subheader("📄 Tabela de dados filtrados")
    st.dataframe(df_filtrado)

    csv = df_filtrado.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Baixar dados filtrados como CSV",
        data=csv,
        file_name="dados_filtrados.csv",
        mime="text/csv"
    )




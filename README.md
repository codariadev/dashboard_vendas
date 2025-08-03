# 📊 Dashboard de Vendas Interativo

Este é um projeto desenvolvido com [Streamlit](https://streamlit.io/) e [Plotly](https://plotly.com/python/) para criação de um dashboard interativo de vendas a partir de uma planilha Excel.

## 🚀 Funcionalidades

- Upload de planilhas `.xlsx` com dados de vendas
- Cálculo automático do faturamento (quantidade × valor unitário)
- Filtros por período (data inicial e final)
- Gráfico interativo de faturamento por produto
- Interface leve e responsiva

---

## 🧾 Formato da Planilha Excel

Para que o sistema funcione corretamente, o arquivo Excel enviado **deve conter obrigatoriamente** as seguintes colunas:

| Coluna          | Tipo de dado     | Exemplo                   |
|------------------|------------------|----------------------------|
| `Data`           | Data             | 2025-08-01                |
| `Produto`        | Texto            | Camiseta                  |
| `Quantidade`     | Número inteiro   | 10                        |
| `Valor Unitário` | Número decimal   | 59.90                     |

> ⚠️ Os nomes das colunas devem estar exatamente como acima (com letras maiúsculas e acentos, se houver).

---

## 🛠️ Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/dashboard-vendas.git
cd dashboard-vendas
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> Se não houver um `requirements.txt`, instale manualmente:
```bash
pip install streamlit pandas plotly openpyxl
```

### 3. Execute a aplicação

```bash
streamlit run app.py
```

---

## 📝 Observações

- Arquivos diferentes do formato `.xlsx` não serão aceitos.
- O gráfico é gerado com base nos dados filtrados pelo intervalo de datas escolhido.
- O campo `Faturamento` é calculado automaticamente a partir dos valores de `Quantidade` e `Valor Unitário`.

---

## 📸 Exemplo de visualização interativo

(https://dashboardvendas-nwfekbrxlabmuhe2ntdwrw.streamlit.app/)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Criado por [CodariaDev](https://github.com/codariadev) 🚀




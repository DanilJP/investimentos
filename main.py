import streamlit as st
import pandas as pd
import numpy as np

# Título e descrição
st.title("Aplicativo Streamlit Base")
st.header("Exibição de Dados Sintéticos")
st.write("Este é um exemplo de como criar um aplicativo base no Streamlit com um DataFrame sintético.")

# Gerar dados sintéticos
def generate_synthetic_data(rows=100):
    np.random.seed(42)  # Para reprodutibilidade
    data = {
        "ID": range(1, rows + 1),
        "Nome": [f"Usuário {i}" for i in range(1, rows + 1)],
        "Idade": np.random.randint(18, 60, size=rows),
        "Salário": np.random.uniform(2000, 10000, size=rows).round(2),
        "Data Admissão": pd.date_range("2015-01-01", periods=rows, freq="W").strftime("%Y-%m-%d"),
    }
    return pd.DataFrame(data)

# Criar DataFrame
df = generate_synthetic_data()

# Exibir DataFrame
st.subheader("Tabela de Dados Sintéticos")
st.dataframe(df)

# Download de CSV
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Baixar CSV", data=csv, file_name="dados_sinteticos.csv", mime="text/csv")

# Filtro de exemplo
st.subheader("Filtro de Idade")
idade_min = st.slider("Idade mínima", min_value=18, max_value=60, value=25)
idade_max = st.slider("Idade máxima", min_value=18, max_value=60, value=40)

# Filtrar DataFrame
filtered_df = df[(df["Idade"] >= idade_min) & (df["Idade"] <= idade_max)]
st.write(f"Mostrando resultados para idade entre {idade_min} e {idade_max}")
st.dataframe(filtered_df)

import streamlit as st
import pandas as pd
import datetime
from itertools import zip_longest

if 'dict_conta' not in st.session_state:
    st.session_state.dict_conta = {}

dict_conta = st.session_state.dict_conta

conta = [  # (mesmo conteúdo omitido para brevidade, igual ao seu)
    "1.1.1.01.01", "1.1.1.01.02", "1.1.1.02.01", "1.1.1.03.01",  # ...
]

descricao = [  # (mesmo conteúdo omitido para brevidade, igual ao seu)
    "Caixa", "Fundo Fixo de Caixa", "Bancos Conta Movimento", "Aplicação Financeira de Liquidez Imediata",  # ...
]

descricao_to_conta = dict(zip(descricao, conta))

with st.form("my_form"):
    st.subheader("Novo Lançamento Contábil")

    selecionar_data = st.date_input("Data do lançamento")
    valor = st.number_input("Valor do lançamento", value=0.01, min_value=0.01)
    conta_d = st.selectbox("Conta de Débito", options=descricao, index=None, placeholder="Selecione")
    conta_c = st.selectbox("Conta de Crédito", options=descricao, index=None, placeholder="Selecione")

    col1, col2 = st.columns(2)
    with col1:
        registrar = st.form_submit_button("Registrar Lançamento")
    with col2:
        limpar = st.form_submit_button("Limpar Lançamentos")

    if registrar:
        if conta_d == conta_c:
            st.error("Não é permitido usar a mesma conta para Débito e Crédito.")
        else:
            for conta_nome in [conta_d, conta_c]:
                if conta_nome not in dict_conta:
                    dict_conta[conta_nome] = {
                        'id_conta': descricao_to_conta.get(conta_nome, 'Conta não encontrada'),
                        'tipo': conta_nome,
                        'débito': [],
                        'crédito': []
                    }

            dict_conta[conta_d]['débito'].append((valor, selecionar_data))
            dict_conta[conta_c]['crédito'].append((valor, selecionar_data))
            st.success("Lançamento registrado com sucesso!")

    if limpar:
        st.session_state.dict_conta = {}
        st.info("Lançamentos limpos com sucesso!")

# === Gerar dados da tabela ===
dados_tabela = []

saldos_por_conta = {}
for nome_conta, dados in dict_conta.items():
    total_d = sum(v for v, _ in dados['débito'])
    total_c = sum(v for v, _ in dados['crédito'])
    saldo = total_d - total_c
    saldos_por_conta[nome_conta] = saldo

for nome_conta, dados in dict_conta.items():
    id_conta = dados['id_conta']
    debitos = dados['débito']
    creditos = dados['crédito']
    saldo_conta = saldos_por_conta[nome_conta]

    saldo_debito = saldo_conta if saldo_conta > 0 else ""
    saldo_credito = abs(saldo_conta) if saldo_conta < 0 else ""

    for valor, data in debitos:
        dados_tabela.append({
            'ID Conta': id_conta,
            'Conta': nome_conta,
            'Data': data,
            'Débito': valor,
            'Crédito': "",
            'Saldo Débito': saldo_debito,
            'Saldo Crédito': saldo_credito
        })

    for valor, data in creditos:
        dados_tabela.append({
            'ID Conta': id_conta,
            'Conta': nome_conta,
            'Data': data,
            'Débito': "",
            'Crédito': valor,
            'Saldo Débito': saldo_debito,
            'Saldo Crédito': saldo_credito
        })

df = pd.DataFrame(dados_tabela)

st.subheader("Lançamentos Registrados")
st.dataframe(df)

# Exibição dos saldos
st.subheader("Saldos Finais por Conta")
for nome, saldo in saldos_por_conta.items():
    cod = descricao_to_conta.get(nome, "N/A")
    tipo = "Devedor" if saldo > 0 else "Credor" if saldo < 0 else "Zerado"
    st.write(f"**{nome} ({cod})** (Saldo {tipo}): R$ {abs(saldo):.2f}")

# Razonetes
st.subheader("Visualização em Razonetes")
for nome_conta, dados in dict_conta.items():
    id_conta = dados['id_conta']
    debitos = dados['débito']
    creditos = dados['crédito']
    total_d = sum(v for v, _ in debitos)
    total_c = sum(v for v, _ in creditos)
    saldo = total_d - total_c
    tipo_saldo = "Devedor" if saldo > 0 else "Credor" if saldo < 0 else "Zerado"

    debitos_html = "<br>".join(f"{v:.2f}" for v, _ in debitos)
    creditos_html = "<br>".join(f"{v:.2f}" for v, _ in creditos)

    html_razonete = f"""
    <div class="container" style="border:1px solid #ccc; padding:10px; margin-bottom:20px;">
        <div style="text-align:center; font-weight:bold;">{nome_conta}</div>
        <div class="row" style="display:flex; text-align:center; margin-top:10px;">
            <div style="flex:1; border:1px solid #000;">D</div>
            <div style="flex:1; border:1px solid #000;">C</div>
        </div>
        <div class="row" style="display:flex; text-align:center;">
            <div style="flex:1; border:1px solid #000;">{debitos_html}</div>
            <div style="flex:1; border:1px solid #000;">{creditos_html}</div>
        </div>
        <div style="text-align:right; margin-top:5px;">
            <b>Saldo ({tipo_saldo}):</b> R$ {abs(saldo):.2f}
        </div>
    </div>
    """
    st.markdown(html_razonete, unsafe_allow_html=True)

import streamlit as st
import pandas as pd
import datetime
from itertools import zip_longest

st.set_page_config(page_title="Lançamentos Contábeis", layout="centered")


if 'dict_conta' not in st.session_state:
    st.session_state.dict_conta = {}

dict_conta = st.session_state.dict_conta

conta = ['1.1.1.01.01', '2.1.2.01.01']
descricao = ['caixa', 'fornecedor']

descricao_to_conta = dict(zip(descricao, conta))


# while True:
#     data = input("Digite uma data com sómente numeros no formato dd/mm/aaaa: ")

#     if not data.isdigit():
#         print("Erro: Digite somente números.")
#         continue

#     if len(data) != 8:
#         print("Digite uma data com 8 digitos")
#         continue
#     else:
#         data_formatada = data[:2]+"/"+data[2:4]+"/"+data[4:]

#     try:
#         valor = float(input("Digite o valor para a conta: "))
#     except ValueError:
#         print("Por favor, insira um valor numérico válido.")
#         continue

#     while True:
#         conta_d = input("Em qual conta você vai fazer o lançamento a débito? ").strip().lower()
#         conta_c = input("Em qual conta você vai fazer o lançamento a crédito? ").strip().lower()

#         if conta_d == conta_c:
#             print("Não pode fazer esse mesmo lançamento na mesma conta")
#             continue
#         else:
#             break

#     for conta_nome in [conta_d, conta_c]:
#         if conta_nome not in dict_conta:
#             dict_conta[conta_nome] = {
#                 'id_conta': descricao_to_conta.get(conta_nome, 'Conta não encontrada'),
#                 'tipo': conta_nome,
#                 'débito': [],
#                 'crédito': [],
#                 'saldo_debito': [],
#                 'saldo_credito': []
#             }

#     dict_conta[conta_d]['débito'].append(valor)
#     dict_conta[conta_d]['crédito'].append(0)

#     dict_conta[conta_c]['crédito'].append(valor)
#     dict_conta[conta_c]['débito'].append(0)

#     sair = input("Deseja fazer outro lançamento? (s/n): ").lower()
#     if sair != 's':
#         break


# for descricao, dados in dict_conta.items():
#     valor_d = sum(dados['débito'])
#     valor_c = sum(dados['crédito'])
#     saldo_final = valor_d - valor_c

#     if saldo_final > 0:
#         dados['saldo_debito'].append(saldo_final)
#         saldo_d = f"{saldo_final:.2f}"
#         saldo_c = None
#     elif saldo_final < 0:
#         dados['saldo_credito'].append(abs(saldo_final))
#         saldo_d = None
#         saldo_c = f"{abs(saldo_final):.2f}"
#     else:
#         saldo_d = saldo_c = 0.00

#     print(f"\nData: {data_formatada}")
#     print(f"Descrição: {dados['tipo']}")
#     print(f"Conta: {dados['id_conta']}")
#     print("débito       | crédito")
#     for d, c in zip_longest(dados['débito'], dados['crédito'], fillvalue=0):
#         d_val = f"{d:.2f}" if d else None
#         c_val = f"{c:.2f}" if c else None
#         print(f"{d_val or '':<12} | {c_val or '':<12}")
#     print("-" * 27)
#     print(f"{saldo_d or '':<12} | {saldo_c or '':<12}")

# dados_tabela = []

# for descricao, dados in dict_conta.items():
#     for d, c, saldo_d, saldo_c in zip_longest(dados['débito'], dados['crédito'], dados['saldo_debito'], dados['saldo_credito'], fillvalue=""):
#         dados_tabela.append({
#             'ID Conta': dados['id_conta'],
#             'Conta': descricao,
#             'Data': data_formatada,
#             'Débito': d,
#             'Crédito': c,
#             'Saldo Débito': saldo_d,
#             'Saldo Crédito': saldo_c
#         })

# df = pd.DataFrame(dados_tabela)
# st.dataframe(df)




import streamlit as st
import pandas as pd
from itertools import zip_longest


# Inicialização do dicionário persistente
if 'dict_conta' not in st.session_state:
    st.session_state.dict_conta = {}

dict_conta = st.session_state.dict_conta

conta = ['1.1.1.01.01', '2.1.2.01.01']
descricao = ['caixa', 'fornecedor']
descricao_to_conta = dict(zip(descricao, conta))

# Formulário para novo lançamento
with st.form("my_form"):
    st.subheader("Novo Lançamento Contábil")

    selecionar_data = st.date_input("Data do lançamento")

    valor = st.number_input("Valor do lançamento", value=0.01, min_value=0.01)

    conta_d = st.selectbox("Conta de Débito", options=descricao, index=None, placeholder="Selecione")
    conta_c = st.selectbox("Conta de Crédito", options=descricao, index=None, placeholder="Selecione")

    submitted = st.form_submit_button("Registrar Lançamento")

    if submitted:
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

# Construir tabela para exibição
dados_tabela = []

for nome_conta, dados in dict_conta.items():
    debitos = dados['débito']
    creditos = dados['crédito']

    # Alinha débitos e créditos com datas
    for (d_valor, d_data), (c_valor, c_data) in zip_longest(debitos, creditos, fillvalue=(0.0, "")):
        dados_tabela.append({
            'ID Conta': dados['id_conta'],
            'Conta': nome_conta,
            'Data': d_data or c_data,
            'Débito': d_valor if d_valor else "",
            'Crédito': c_valor if c_valor else ""
        })

# Cálculo de saldo final por conta
saldos = []
for nome_conta, dados in dict_conta.items():
    total_d = sum(v for v, _ in dados['débito'])
    total_c = sum(v for v, _ in dados['crédito'])
    saldo = total_d - total_c
    saldos.append((nome_conta, saldo))

df = pd.DataFrame(dados_tabela)
st.subheader("Lançamentos Registrados")
st.dataframe(df)

st.subheader("Saldos Finais por Conta")
for nome, saldo in saldos:
    tipo = "Devedor" if saldo > 0 else "Credor" if saldo < 0 else "Zerado"
    st.write(f"**{nome}** (Saldo {tipo}): R$ {abs(saldo):.2f}")


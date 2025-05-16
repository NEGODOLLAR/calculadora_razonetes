import streamlit as st
import pandas as pd
import datetime
from itertools import zip_longest

if 'dict_conta' not in st.session_state:
    st.session_state.dict_conta = {}

dict_conta = st.session_state.dict_conta

conta = [
    "1.1.1.01.01", "1.1.1.01.02", "1.1.1.02.01", "1.1.1.03.01", 
    "1.1.2.01.01", "1.1.2.01.02", "1.1.2.02.01", "1.1.2.02.02", 
    "1.1.2.02.03", "1.1.2.02.04", "1.1.2.02.05", "1.1.2.03.01", 
    "1.1.3.01.01", "1.1.3.01.02", "1.1.3.02.01", "1.1.3.02.02", 
    "1.1.3.02.03", "1.1.3.02.04", "1.1.3.02.05", "1.1.3.03.01", 
    "1.1.3.03.02", "1.1.4.01.01", "1.1.4.01.02", "1.1.6.01.99", 
    "1.2.1.01.01", "1.2.1.01.02", "1.2.1.01.03", "1.2.1.01.04", 
    "1.2.1.01.05", "1.2.2.01.01", "1.2.3.01.10", "1.2.3.01.11", 
    "1.2.3.01.20", "1.2.3.01.21", "1.2.3.01.30", "1.2.3.01.31", 
    "1.2.3.01.40", "1.2.3.01.41", "1.2.3.01.50", "1.2.3.01.51", 
    "1.2.3.01.60", "1.2.3.01.61", "1.2.3.02.20", "1.2.3.02.30", 
    "1.2.3.02.40", "1.2.3.02.50", "1.2.3.02.51", "1.2.3.01.10", 
    "1.2.3.01.20", "1.2.3.01.21", "1.2.4.01.10", "1.2.4.01.20", 
    "1.2.4.01.30", "1.2.4.02.10", "1.2.4.02.20", "1.2.4.02.30", 
    "2.1.1.01.01", "2.1.1.01.02", "2.1.1.01.03", "2.1.1.01.04", 
    "2.1.1.01.05", "2.1.1.01.06", "2.1.1.01.07", "2.1.2.01.01", 
    "2.1.2.01.02", "2.1.2.02.01", "2.1.2.02.02", "2.1.2.02.03", 
    "2.1.3.01.01", "2.1.3.01.02", "2.1.4.01.01", "2.1.4.01.02", 
    "2.1.4.03.01", "2.1.5.01.01", "2.1.5.01.02", "2.2.1.01.01", 
    "2.2.1.01.02", "2.2.1.01.03", "2.2.1.02.01", "2.2.1.02.02", 
    "2.2.1.02.03", "2.2.2.01.01", "2.2.2.01.01", "2.2.2.01.02", 
    "2.2.2.01.03", "2.3.1.01.01", "2.8.1.02.01", "2.8.2.01.01", 
    "2.8.3.01.01", "2.8.8.01.01", "2.8.8.02.01", "3.1.1.01.01", 
    "3.1.1.01.02", "3.1.1.01.03", "3.1.2.01.01", "3.1.2.01.02", 
    "3.1.2.01.03", "3.1.2.01.04", "3.1.2.01.05", "3.1.2.02.01", 
    "3.1.2.02.02", "3.1.2.02.03", "3.2.1.01.01", "3.2.1.01.02", 
    "3.2.1.01.03", "3.3.1.01.01", "3.3.1.01.02", "3.3.1.01.03", 
    "3.3.1.01.04", "3.3.1.01.05", "3.3.1.01.06", "3.3.1.01.07", 
    "3.3.1.01.08", "3.3.1.01.09", "3.3.1.01.10", "3.3.1.02.01", 
    "3.3.1.02.02", "3.3.1.02.03", "3.3.2.01.01", "3.3.2.01.02", 
    "3.3.2.01.03", "3.3.2.01.04", "3.3.2.01.05", "3.3.2.01.06", 
    "3.3.2.01.07", "3.3.2.01.08", "3.3.2.01.09", "3.3.2.01.10", 
    "3.3.2.01.11", "3.3.2.02.01", "3.3.2.02.02", "3.3.2.02.03", 
    "3.3.2.02.04", "3.3.2.02.05", "3.3.2.02.06", "3.3.2.02.07", 
    "3.3.2.02.08", "3.3.2.02.09", "3.3.2.02.10", "3.3.2.02.11", 
    "3.3.2.02.12", "3.3.2.02.13", "3.3.2.02.14", "3.3.2.03.01", 
    "3.3.9.01.01", "3.3.9.01.02", "3.3.9.02.01", "3.3.9.02.02", 
    "3.3.9.03.01", "3.4.1.01.01", "3.4.1.01.02", "3.4.1.01.03", 
    "3.4.1.01.04", "3.4.1.01.05", "3.4.1.02.01", "3.4.1.02.02", 
    "3.4.1.02.03", "3.4.1.02.04"
]

descricao = [
    "Caixa (Ativo)", "Fundo Fixo de Caixa (Ativo)", "Bancos Conta Movimento (Ativo)", 
    "Aplicação Financeira de Liquidez Imediata (Ativo)", "Contas a Receber (Ativo)", 
    "PECLD (Ativo)", "Adiantamento Quinzenal (Ativo)", "Empréstimos a colaboradores (Ativo)", 
    "Antecipação de Salários (Ativo)", "Antecipação de Férias (Ativo)", 
    "Antecipação de 13º Salário (Ativo)", "Adiantamentos a Fornecedores (Ativo)", 
    "Mercadorias para Revenda (Ativo)", 
    "(-) Perda por Ajuste ao Valor Realizável Líquido - Estoque Mercadorias (Ativo)", 
    "Insumos (materiais diretos) (Ativo)", "Outros Materiais (Ativo)", 
    "Produtos em Elaboração (Ativo)", "Produtos Acabados (Ativo)", 
    "(-) Perda por Ajuste ao Valor Realizável Líquido - Estoque Produtos (Ativo)", 
    "Materiais para Consumo (Ativo)", "Materiais para Reposição (Ativo)", 
    "Aluguéis e Arrendamentos Pagos Antecipadamente (Ativo)", 
    "Prêmios de Seguros a Apropriar (Ativo)", "Outras Despesas Antecipadas (Ativo)", 
    "Clientes - Longo Prazo (Ativo)", "PCLD Longo Prazo (Ativo)", 
    "Juros a Apropriar (Ativo)", "Empréstimos de LP (Ativo)", "Juros a Apropriar (Ativo)", 
    "Participações Societárias (Ativo)", "Terrenos (Ativo)", "Impairment Terrenos (Ativo)", 
    "Edifícios e Construções (Ativo)", "Impairment Edifícios e Construções (Ativo)", 
    "Benfeitorias em Imóveis de Terceiros (Ativo)", 
    "Impairment Benfeitorias em Imóveis de Terceiros (Ativo)", 
    "Máquinas, Equipamentos e Instalações Industriais (Ativo)", 
    "Impairment Máquinas, Equipamentos e Instalações Industriais (Ativo)", 
    "Móveis, Utensílios e Instalações Comerciais (Ativo)", 
    "Impairment Móveis, Utensílios e Instalações Comerciais (Ativo)", 
    "Veículos (Ativo)", "Impairment Veículos (Ativo)", 
    "Depreciação Acumulada - Edifícios e Construções (Ativo)", 
    "Depreciação Acumulada - Benfeitorias em Imóveis de Terceiros (Ativo)", 
    "Depreciação Acumulada - Máquinas, Equipamentos e Instalações Industriais (Ativo)", 
    "Depreciação Acumulada - Móveis, Utensílios e Instalações Comerciais (Ativo)", 
    "Depreciação Acumulada - Veículos (Ativo)", "Terrenos para Investimento - Custo (Ativo)", 
    "Edifícios para Investimento - Custo (Ativo)", 
    "Edifícios para Investimento - Depreciação (Ativo)", "Softwares (Ativo)", 
    "Marcas (Ativo)", "Patentes e Segredos Industriais (Ativo)", 
    "Amortização Acumulada - Softwares (Ativo)", "Amortização Acumulada - Marcas (Ativo)", 
    "Amortização Acumulada - Patentes e Segredos Industriais (Ativo)", 
    "Salários e Remunerações a Pagar (Passivo)", "Participações no Resultado a Pagar (Passivo)", 
    "FGTS a Recolher (Passivo)", "Férias (Passivo)", "13º Salário (Passivo)", 
    "FGTS - Férias (Passivo)", "FGTS – 13º Salário (Passivo)", 
    "Fornecedores Nacionais (Passivo)", "Fornecedores Exterior (Passivo)", 
    "Aluguéis e arrendamentos a Pagar (Passivo)", "Adiantamento de Clientes (Passivo)", 
    "Outras Contas a Pagar (Passivo)", "Duplicatas Descontadas (Passivo)", 
    "Empréstimos e Financiamentos (Passivo)", "Simples Nacional (Passivo)", 
    "Tributos Municipais (Passivo)", "Parcelamento Simples Nacional CP (Passivo)", 
    "Lucros a Pagar (Passivo)", "Mútuo com Partes Relacionadas (Passivo)", 
    "Fornecedores Nacionais (Passivo)", "Fornecedores Exterior (Passivo)", 
    "Juros a Apropriar (Passivo)", "Empréstimos e Financiamentos LP (Passivo)", 
    "Duplicatas Descontadas LP (Passivo)", "Juros a Apropriar (Passivo)", 
    "Parcelamento Simples Nacional LP (Passivo)", "Empréstimos de Sócios (Passivo)", 
    "Mútuos com Partes Relacionadas (Passivo)", "Juros a Apropriar (Passivo)", 
    "Capital Social Subscrito (Passivo)", "Capital Social a Integralizar (Passivo)", 
    "Adiantamento para Futuro Aumento de Capital (Passivo)", "Lucros a Distribuir (Passivo)", 
    "Lucros Acumulados (Passivo)", "Prejuízos Acumulados (Passivo)", 
    "Serviços Prestados (Resultado)", "Mercadorias Vendidas (Resultado)", 
    "Produtos Vendidos (Resultado)", "SIMPLES NACIONAL (Resultado)", "ICMS (Resultado)", 
    "ISS (Resultado)", "PIS/Pasep (Resultado)", "Cofins (Resultado)", 
    "DESCONTOS E ABATIMENTOS (Resultado)", "DEVOLUÇÕES (Resultado)", 
    "JUROS DE AVP (Resultado)", "Custos dos Produtos Vendidos (Resultado)", 
    "Custos das Mercadorias Vendidas (Resultado)", "Custos dos Serviços Prestados (Resultado)", 
    "Salários (Resultado)", "Gratificações (Resultado)", "Férias (Resultado)", 
    "13 Salário (Resultado)", "FGTS (Resultado)", "Vale Refeição/Refeitório (Resultado)", 
    "Vale Transporte (Resultado)", "Assistência Médica (Resultado)", 
    "Seguro de Vida (Resultado)", "Treinamento (Resultado)", 
    "Comissões sobre Vendas (Resultado)", "Propaganda e publicidade (Resultado)", 
    "Brindes e material promocional (Resultado)", "Salários (Resultado)", 
    "Gratificações (Resultado)", "Férias (Resultado)", "13º Salário (Resultado)", 
    "FGTS (Resultado)", "Vale Refeição/Refeitório (Resultado)", 
    "Vale Transporte (Resultado)", "Assistência Médica (Resultado)", 
    "Seguro de Vida (Resultado)", "Treinamento (Resultado)", "Pro Labore (Resultado)", 
    "Aluguéis e Arrendamentos (Resultado)", "Condomínios e Estacionamentos (Resultado)", 
    "Despesas com Veículos (Resultado)", "Depreciação (Resultado)", 
    "Amortização (Resultado)", "Serviços Profissionais Contratados (Resultado)", 
    "Energia (Resultado)", "Água e Esgoto (Resultado)", "Telefone e Internet (Resultado)", 
    "Correios e Malotes (Resultado)", "Seguros (Resultado)", "Multas (Resultado)", 
    "Bens de Pequeno Valor (Resultado)", "Material de Escritório (Resultado)", 
    "Taxas e Tributos Municipais (Resultado)", 
    "Receita na Venda de Investimento, Imobilizado ou Intangível (Resultado)", 
    "Custo do Investimento, Imobilizado ou Intangível Baixado (Resultado)", 
    "PECLD (Resultado)", "Perda de recuperabilidade (Impairment) (Resultado)", 
    "Receita de Participação Societária (Resultado)", "Juros Passivos (Resultado)", 
    "Despesas Bancárias (Resultado)", "IOF (Resultado)", "Descontos Concedidos (Resultado)", 
    "Variação Cambial Passivo (Resultado)", "Rendimentos de Aplicação Financeira (Resultado)", 
    "Juros Ativos (Resultado)", "Descontos Obtidos (Resultado)", 
    "Variação Cambial Ativo (Resultado)"
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
            'Débito': f"{valor:.2f}",
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
            'Crédito': f"{valor:.2f}",
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

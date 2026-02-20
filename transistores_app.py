import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de TBJ", page_icon="⚡")

st.title("⚡ Calculadora de Transistor Bipolar de Junção (TBJ)")
st.markdown("---")

# --- Interface Lateral (Inputs) ---
st.sidebar.header("Parâmetros de Entrada")
vbb = st.sidebar.number_input("VBB (Tensão de Base) [V]", value=15.0)
vcc = st.sidebar.number_input("VCC (Tensão de Coletor) [V]", value=15.0)
beta = st.sidebar.number_input("β (Ganho/Beta)", value=100)
rb_kohm = st.sidebar.number_input("RB (Resistência de Base) [kΩ]", value=470.0)
rc_kohm = st.sidebar.number_input("RC (Resistência de Coletor) [kΩ]", value=3.6)
vbe = st.sidebar.slider("VBE (Queda de tensão) [V]", 0.5, 0.9, 0.7)

# Conversão de kΩ para Ω
rb = rb_kohm * 1000
rc = rc_kohm * 1000

# --- Lógica de Cálculo ---
ib = (vbb - vbe) / rb
ic = beta * ib
vce = vcc - (ic * rc)
pd = vce * ic

# --- Exibição do Front-end ---
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Corrente da Base (IB)", value=f"{ib*1e6:.2f} µA")
    st.metric(label="Corrente do Coletor (IC)", value=f"{ic*1e3:.2f} mA")

with col2:
    st.metric(label="Tensão VCE", value=f"{vce:.2f} V")
    st.metric(label="Potência Dissipada", value=f"{pd*1e3:.2f} mW")

# Verificação de Estado do Transistor
st.markdown("### Análise de Operação")
if vce < 0.2:
    st.error("⚠️ Transistor em SATURAÇÃO (VCE muito baixo)")
elif vce >= vcc * 0.95:
    st.warning("⚠️ Transistor em CORTE (Praticamente sem corrente)")
else:
    st.success("✅ Transistor em REGIÃO ATIVA")

st.info(f"Reta de Carga: VCE máximo = {vcc}V | IC Sat (máx) = {(vcc/rc)*1e3:.2f}mA")
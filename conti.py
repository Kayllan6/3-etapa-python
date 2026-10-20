import streamlit as st


st.set_page_config(
    page_title="Supermercado Econômico",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 Supermercado Econômico")
st.subheader("Calculadora de Troco")

st.write("Digite o valor da compra e o valor pago pelo cliente.")

col1, col2 = st.columns(2)

with col1:
    compra = st.number_input(
        "Valor da compra (R$)",
        value=0.0,
        step=1.0,
        min_value=0.0
    )

with col2:
    pagamento = st.number_input(
        "Valor pago (R$)",
        value=0.0,
        step=1.0,
        min_value=0.0
    )

resultado = None

if st.button("Calcular troco", type="primary"):

    if pagamento < compra:
        st.error("Valor insuficiente! O pagamento é menor que a compra.")

    else:
        resultado = pagamento - compra

if resultado is not None:
    st.success(f"**Troco:** R$ {resultado:.2f}")
```


import streamlit as st
from extractor import extraer_items_desde_pdf

st.title("Extractor de Ítems del CV (SIGEVA-CONICET)")
st.subheader("Universidad Católica de Cuyo - Secretaría de Investigación")

uploaded_file = st.file_uploader("Subí tu CV en formato PDF", type="pdf")

if uploaded_file:
    st.success("Archivo cargado correctamente.")
    with st.spinner("Procesando el archivo..."):
        items_detectados = extraer_items_desde_pdf(uploaded_file)
        st.subheader("Ítems detectados:")
        for item in items_detectados:
            st.write("-", item)
    st.download_button("Descargar ítems en Excel", "Funcionalidad aún no implementada")

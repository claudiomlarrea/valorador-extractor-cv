import streamlit as st
from extractor import extraer_items_desde_pdf

st.title("📄 Extractor de CV (SIGEVA-CONICET)")

archivo_pdf = st.file_uploader("Subí tu CV en PDF generado por SIGEVA-CONICET", type=["pdf"])
if archivo_pdf is not None:
    with open("cv_temp.pdf", "wb") as f:
        f.write(archivo_pdf.read())
    st.success("Archivo cargado correctamente. Analizando...")
    items_detectados = extraer_items_desde_pdf("cv_temp.pdf")
    st.dataframe(items_detectados)
    items_detectados.to_csv("items_extraidos.csv", index=False)
    with open("items_extraidos.csv", "rb") as f:
        st.download_button("📥 Descargar ítems detectados (CSV)", f, file_name="items_extraidos.csv")

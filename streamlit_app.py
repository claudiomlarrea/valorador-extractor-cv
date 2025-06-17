import streamlit as st
import pandas as pd
from extractor import extraer_items_desde_pdf

st.title("🧠 Extractor de Ítems desde CV SIGEVA")

uploaded_file = st.file_uploader("Subí el archivo PDF del CV SIGEVA-CONICET", type="pdf")

if uploaded_file is not None:
    st.success("Archivo cargado correctamente.")

    items_detectados = extraer_items_desde_pdf(uploaded_file)

    if items_detectados:
        st.header("📌 Ítems detectados:")
        for item in items_detectados:
            st.markdown(f"- **{item}**: {items_detectados[item]} puntos")

        df = pd.DataFrame(list(items_detectados.items()), columns=["Ítem", "Puntaje"])

        st.download_button(
            label="📥 Descargar ítems en Excel",
            data=df.to_excel(index=False, engine="openpyxl"),
            file_name="items_detectados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("No se detectaron ítems relevantes en el documento.")

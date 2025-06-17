import streamlit as st
import pandas as pd
from extractor import extraer_items_desde_pdf

st.set_page_config(page_title="📄 Valorador Extractor CV", layout="wide")

st.title("📄 Extractor de Ítems desde CV PDF")

uploaded_file = st.file_uploader("Subí el archivo PDF generado por SIGEVA o similar", type=["pdf"])

if uploaded_file:
    st.success("✅ Archivo cargado correctamente.")
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    items_detectados = extraer_items_desde_pdf("temp.pdf")

    st.markdown("### 🧾 Ítems detectados:")
    for item, puntaje in items_detectados.items():
        st.markdown(f"- **{item}**: {puntaje} puntos")

    df = pd.DataFrame(items_detectados.items(), columns=["Ítem detectado", "Puntaje asignado"])

    # Descargar en Excel
    st.download_button(
        label="📥 Descargar ítems en Excel",
        data=df.to_excel(index=False, engine="openpyxl"),
        file_name="items_detectados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

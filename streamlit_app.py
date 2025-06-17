
import streamlit as st
import pandas as pd
from extractor import extraer_items_desde_pdf
from io import BytesIO

st.set_page_config(page_title="Extractor de Ítems del CV", layout="centered")
st.title("📄 Extractor de Ítems del CV SIGEVA-CONICET")

uploaded_file = st.file_uploader("Cargá tu archivo PDF del CV generado por SIGEVA-CONICET", type=["pdf"])

if uploaded_file is not None:
    texto_extraido = uploaded_file.read()
    items_detectados = extraer_items_desde_pdf(texto_extraido)

    if items_detectados:
        st.success("Archivo cargado correctamente.")
        st.subheader("Ítems detectados:")
        for item, puntaje in items_detectados.items():
            st.markdown(f"- **{item}**: {puntaje} puntos")

        df = pd.DataFrame(list(items_detectados.items()), columns=["Ítem detectado", "Puntaje asignado"])
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
            writer.save()
            processed_data = output.getvalue()

        st.download_button(
            label="📥 Descargar ítems en Excel",
            data=processed_data,
            file_name="items_detectados.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.warning("No se detectaron ítems reconocibles en el CV.")

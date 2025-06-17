
# Artefacto 1: Extractor de Ítems desde CV

Este artefacto permite subir un archivo PDF o Word del CV generado desde SIGEVA-CONICET y extraer automáticamente los ítems relevantes para su evaluación posterior según la Resolución 897.

## Instrucciones
1. Ejecutar la app con `streamlit run streamlit_app.py`.
2. Subir un archivo .pdf o .docx con el CV generado por SIGEVA-CONICET.
3. Visualizar y exportar los ítems detectados para usarlos en el artefacto evaluador.

## Archivos incluidos
- `streamlit_app.py`: Aplicación principal de Streamlit.
- `extractor.py`: Función de extracción de ítems desde el CV.
- `requirements.txt`: Dependencias necesarias.

## Requisitos
- Python 3.8 o superior
- Streamlit
- PyMuPDF (fitz)
- python-docx

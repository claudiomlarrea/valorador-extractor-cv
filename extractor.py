
import fitz  # PyMuPDF

def extraer_items_desde_pdf(pdf_bytes):
    texto_extraido = ""
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for pagina in doc:
            texto_extraido += pagina.get_text()

    texto = texto_extraido.lower()
    items = {
        "Doctorado": 250 if "doctor" in texto else 0,
        "Maestría": 150 if "maestr" in texto else 0,
        "Especialización": 75 if "especializ" in texto else 0,
        "Cursos de postgrado": 75 if "curso de postgrado" in texto or "posgrado" in texto else 0,
        "Profesor Titular": 200 if "profesor titular" in texto else 0,
        "Ayudante": 40 if "ayudante" in texto else 0,
        "Libro": 120 if "isbn" in texto or "editorial" in texto else 0,
        "Premio": 60 if "premio" in texto or "distinción" in texto else 0,
        "Investigador": 150 if "investigador" in texto else 0,
        "Becario o adscripto": 30 if "becario" in texto or "adscripto" in texto else 0,
        "Rector": 100 if "rector" in texto else 0
    }
    return {k: v for k, v in items.items() if v > 0}

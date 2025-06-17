import fitz  # PyMuPDF
import pandas as pd
import re

def extraer_items_desde_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    texto = ""
    for page in doc:
        texto += page.get_text()
    patrones = {
        "Doctorado": r"[Dd]octorado",
        "Maestría": r"[Mm]aestr[íi]a",
        "Especialización": r"[Ee]specializaci[oó]n",
        "Profesor Titular": r"[Pp]rofesor [Tt]itular",
        "Ayudante": r"[Aa]yudante",
        "Investigador": r"[Ii]nvestigador",
        "Libro": r"[Ll]ibro[s]?",
        "Premio": r"[Pp]remio[s]?",
        "Evaluador de tesis": r"[Jj]urado de [Tt]esis",
        "Artículo": r"[Aa]rt[íi]culo[s]?",
        "Capítulo de libro": r"[Cc]ap[íi]tulo[s]?",
        "Ponencia": r"[Pp]onencia[s]?",
    }
    resultados = []
    for item, patron in patrones.items():
        if re.search(patron, texto):
            resultados.append({"Ítem detectado": item})
    return pd.DataFrame(resultados)

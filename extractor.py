import fitz  # PyMuPDF
import re

def extraer_items_desde_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    texto_extraido = ""
    for pagina in doc:
        texto_extraido += pagina.get_text()

    texto = texto_extraido.lower()

    items = {
        # Formación académica
        "Doctorado": 250 if re.search(r"\bdoctorado\b", texto) else 0,
        "Maestría": 150 if re.search(r"\bmaestr[íi]a\b", texto) else 0,
        "Especialización": 75 if re.search(r"\bespecializaci[óo]n\b", texto) else 0,
        "Cursos de postgrado": 75 if re.search(r"\bcursos? de postgrado\b", texto) else 0,
        "Título de grado": 30 if re.search(r"\bt[íi]tulo de grado\b", texto) else 0,

        # Docencia
        "Profesor Titular": 200 if re.search(r"\bprofesor titular\b", texto) else 0,
        "Profesor Asociado": 160 if re.search(r"\bprofesor asociado\b", texto) else 0,
        "Profesor Adjunto": 120 if re.search(r"\bprofesor adjunto\b", texto) else 0,
        "JTP": 80 if re.search(r"\bjefe de trabajos pr[áa]cticos\b", texto) else 0,
        "Ayudante": 40 if re.search(r"\bayudante de primera categor[íi]a\b", texto) else 0,
        "Tribunal de concursos docentes": 60 if re.search(r"\btribunal de concursos\b", texto) else 0,
        "Docente de posgrado acreditado": 100 if re.search(r"\bdocente.*posgrado.*acreditado\b", texto) else 0,
        "Docente de posgrado no acreditado": 50 if re.search(r"\bdocente.*posgrado.*no acreditado\b", texto) else 0,
        "Evaluador de tesis": 60 if re.search(r"\b(tribunal de tesis|evaluador de tesis)\b", texto) else 0,

        # Producción
        "Libro": 120 if re.search(r"\blibro\b", texto) else 0,
        "Capítulo de libro": 60 if re.search(r"\bcap[íi]tulo de libro\b", texto) else 0,
        "Publicación con referato": 180 if re.search(r"\bpublicaci[óo]n.*referato\b", texto) else 0,
        "Publicación sin referato": 50 if re.search(r"\bpublicaci[óo]n.*sin referato\b", texto) else 0,

        # Otros
        "Premio": 60 if re.search(r"\bpremio|distinci[óo]n\b", texto) else 0,
        "Becario o adscripto": 30 if re.search(r"\bbecario|adscripto\b", texto) else 0,
        "Rector": 100 if re.search(r"\brector\b", texto) and not re.search(r"\bvicerrector|rectorado\b", texto) else 0
    }

    return {k: v for k, v in items.items() if v > 0}

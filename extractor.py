
import fitz  # PyMuPDF

def extraer_items_desde_pdf(pdf_file):
    texto_extraido = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for pagina in doc:
            texto_extraido += pagina.get_text()

    # Palabras clave de ejemplo — se pueden mejorar con expresiones regulares más sofisticadas
    patrones = {
        "Títulos de Grado": "Licenciado|Ingeniero|Abogado|Contador|Médico",
        "Maestrías": "Magíster|Maestría",
        "Doctorados": "Doctor en|PhD",
        "Especializaciones": "Especialista en",
        "Cursos de Postgrado": "Curso.*Postgrado|Diplomatura",
        "Profesor Titular": "Profesor Titular",
        "Profesor Asociado": "Profesor Asociado",
        "Profesor Adjunto": "Profesor Adjunto",
        "Jefe de Trabajos Prácticos": "Jefe de Trabajos Prácticos",
        "Ayudante de primera categoría": "Ayudante de primera",
        "Libros": "ISBN|Editorial|Libro",
        "Capítulo de libro": "Capítulo.*libro",
        "Publicación con referato": "revista científica|journal",
        "Publicación sin referato": "publicación sin referato",
        "Premios, Becas y Distinciones": "Premio|Beca|Distinción",
        "Dirección de tesis": "Director.*tesis|Dirigí.*tesis",
    }

    encontrados = []
    for item, patron in patrones.items():
        if patron.lower() in texto_extraido.lower():
            encontrados.append(item)

    return list(set(encontrados))

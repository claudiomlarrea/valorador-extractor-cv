import fitz  # PyMuPDF

def extraer_items_desde_pdf(pdf_file):
    texto_extraido = ""

    # Leer el texto de cada página del PDF
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            texto_extraido += page.get_text()

    texto_extraido = texto_extraido.lower()

    items_detectados = {
        # Formación Académica
        "Doctorado": 250 if "doctorado" in texto_extraido else 0,
        "Maestría": 150 if "maestría" in texto_extraido else 0,
        "Especializaciones": 75 if "especialización" in texto_extraido else 0,
        "Cursos de postgrado": 75 if "curso de postgrado" in texto_extraido or "posgrado" in texto_extraido else 0,

        # Docencia
        "Profesor Titular": 200 if "profesor titular" in texto_extraido else 0,
        "Profesor Asociado": 160 if "profesor asociado" in texto_extraido else 0,
        "Profesor Adjunto": 120 if "profesor adjunto" in texto_extraido else 0,
        "Jefe de Trabajos Prácticos": 80 if "jefe de trabajos prácticos" in texto_extraido else 0,
        "Ayudante de primera categoría": 40 if "ayudante de primera" in texto_extraido else 0,
        "Tribunal de concursos docentes": 60 if "tribunal de concurso" in texto_extraido else 0,
        "Docencia en Postgrados acreditados": 100 if "postgrado acreditado" in texto_extraido else 0,
        "Docencia en Postgrados no acreditados": 50 if "postgrado no acreditado" in texto_extraido else 0,
        "Tribunal de tesis de Postgrado": 60 if "jurado de tesis" in texto_extraido else 0,

        # Investigación
        "Director de Programa de Investigación": 200 if "director de programa de investigación" in texto_extraido else 0,
        "Co-director de Programa o Director de Proyecto": 150 if "codirector de programa" in texto_extraido or "director de proyecto" in texto_extraido else 0,
        "Co-director de Proyecto": 100 if "codirector de proyecto" in texto_extraido else 0,
        "Integrante de proyecto de investigación": 60 if "integrante de proyecto" in texto_extraido else 0,
        "Becario o adscripto": 30 if "becario" in texto_extraido or "adscripto" in texto_extraido else 0,

        # Producción Académica
        "Libro": 120 if "isbn" in texto_extraido or "libro" in texto_extraido else 0,
        "Capítulo de libro": 60 if "capítulo" in texto_extraido else 0,
        "Publicación con referato": 180 if "referato" in texto_extraido else 0,
        "Publicación sin referato": 50 if "sin referato" in texto_extraido else 0,

        # Actividad Científica
        "Premio": 60 if "premio" in texto_extraido or "distinción" in texto_extraido else 0,
        "Conferencista": 50 if "conferencista" in texto_extraido else 0,
        "Expositor o panelista": 40 if "expositor" in texto_extraido or "panelista" in texto_extraido else 0,
        "Organizador de evento": 30 if "organizador" in texto_extraido else 0,
        "Asistente a eventos": 20 if "asistente" in texto_extraido else 0,
        "Desarrollo con evaluación externa": 200 if "evaluación externa" in texto_extraido else 0,
        "Desarrollo sin evaluación": 50 if "desarrollo sin evaluación" in texto_extraido else 0,
        "Miembro de sociedad científica": 100 if "miembro" in texto_extraido and "científica" in texto_extraido else 0,
        "Evaluador de investigaciones": 100 if "evaluador" in texto_extraido else 0,

        # Formación de Recursos Humanos
        "Dirección de tesis de postgrado": 150 if "director de tesis" in texto_extraido else 0,
        "Co-dirección de tesis de postgrado": 100 if "codirector de tesis" in texto_extraido else 0,
        "Dirección de investigadores": 150 if "director de investigadores" in texto_extraido else 0,
        "Co-dirección de investigadores": 100 if "codirector de investigadores" in texto_extraido else 0,
        "Dirección de becarios": 60 if "director de becario" in texto_extraido else 0,
        "Dirección de auxiliares de docencia": 30 if "director de auxiliares" in texto_extraido else 0,
        "Dirección de tesis de grado": 30 if "director de tesis de grado" in texto_extraido else 0,
        "Co-dirección de tesis de grado": 20 if "codirector de tesis de grado" in texto_extraido else 0,

        # Gestión Universitaria
        "Rector": 100 if "rector" in texto_extraido else 0,
        "Vicerrector": 80 if "vicerrector" in texto_extraido else 0,
        "Decano": 80 if "decano" in texto_extraido else 0,
        "Vicedecano": 60 if "vicedecano" in texto_extraido else 0,
        "Secretario de Universidad": 60 if "secretario de universidad" in texto_extraido else 0,
        "Secretario de Facultad": 40 if "secretario de facultad" in texto_extraido else 0,
        "Director de instituto": 35 if "director de instituto" in texto_extraido else 0,
        "Co-director de instituto": 20 if "codirector de instituto" in texto_extraido else 0,
        "Consejero superior": 15 if "consejo superior" in texto_extraido else 0,
        "Consejero de facultad": 10 if "consejo directivo" in texto_extraido else 0,
        "Responsable de programa institucional": 35 if "responsable de programa" in texto_extraido else 0,
        "Participante de programa institucional": 10 if "participante de programa" in texto_extraido else 0,
        "Comisiones asesoras": 10 if "comisión asesora" in texto_extraido else 0,
        "Otros antecedentes": 10 if "otros antecedentes" in texto_extraido else 0,
    }

    return {k: v for k, v in items_detectados.items() if v > 0}

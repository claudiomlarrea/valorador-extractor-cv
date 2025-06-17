def extraer_items_cv(path_pdf):
    doc = fitz.open(path_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()

    texto = texto.lower()

    # Diccionario de ítems y sus puntajes máximos
    items_detectados = {
        "Formación Académica": {
            "título de grado": ("licenciatura", 30),
            "especialización": ("especialista", 75),
            "maestría": ("magíster", 150),
            "doctorado": ("doctor", 250),
            "cursos de postgrado": ("curso.*postgrado|curso.*posgrado", 75)
        },
        "Docencia Universitaria": {
            "profesor titular": ("profesor titular", 200),
            "profesor asociado": ("profesor asociado", 160),
            "profesor adjunto": ("profesor adjunto", 120),
            "jtp": ("jefe de trabajos prácticos", 80),
            "ayudante primera": ("ayudante de primera", 40),
            "tribunal concursos": ("tribunal.*concurso", 60),
            "docencia postgrado acreditado": ("docente.*postgrado.*acreditado", 100),
            "docencia postgrado no acreditado": ("docente.*postgrado", 50),
            "tribunal tesis": ("tribunal.*tesis", 60)
        },
        "Investigación Científica y Tecnológica": {
            "director programa": ("director.*programa.*investigaci", 200),
            "co-director programa o director proyecto": ("co.?director.*programa|director.*proyecto", 150),
            "co-director proyecto": ("co.?director.*proyecto", 100),
            "integrante proyecto": ("integrante.*proyecto", 60),
            "becario o adscripto": ("becario|adscripto", 30)
        },
        "Producción Académica": {
            "libros": ("libro", 120),
            "capítulos de libro": ("capítulo.*libro", 60),
            "patentes": ("patente|registro.*propiedad", 60),
            "publicación con referato": ("publicación.*referato", 180),
            "publicación sin referato": ("publicación.*sin referato", 50)
        },
        "Actividad Científica": {
            "premios": ("premio|distinci[oó]n", 60),
            "conferencista": ("conferencia.*invitaci[oó]n", 50),
            "panelista": ("panelista|expositor", 40),
            "organizador": ("organizador|coordinador", 30),
            "asistente": ("asistente", 20),
            "desarrollo ctec evaluado": ("desarrollo.*evaluaci[oó]n.*externa", 200),
            "desarrollo ctec sin eval": ("desarrollo.*sin evaluaci[oó]n", 50),
            "miembro sociedades científicas": ("miembro.*sociedad.*cient", 100),
            "miembro comisiones evaluadoras": ("comisi[oó]n.*evaluadora", 100)
        },
        "Formación de Recursos Humanos": {
            "dirección tesis postgrado": ("director.*tesis.*maestr[ií]a|doctorado", 150),
            "co-dirección tesis postgrado": ("co.?director.*tesis.*maestr[ií]a|doctorado", 100),
            "dirección investigadores": ("director.*investigador", 150),
            "co-dirección investigadores": ("co.?director.*investigador", 100),
            "dirección becarios": ("director.*becario|pasante", 60),
            "dirección auxiliares docencia": ("director.*auxiliar.*docencia", 30),
            "dirección tesis grado": ("director.*tesis.*grado", 30),
            "co-dirección tesis grado": ("co.?director.*tesis.*grado", 20)
        },
        "Gestión Universitaria": {
            "rector": ("rector", 100),
            "vicerrector": ("vicerrector", 80),
            "decano": ("decano", 80),
            "vicedecano": ("vicedecano", 60),
            "secretario universidad": ("secretario.*universidad", 60),
            "secretario facultad": ("secretario.*facultad", 40),
            "director centro": ("director.*centro|instituto|escuela", 35),
            "co-director centro": ("co.?director.*centro|instituto|escuela", 20),
            "consejero superior": ("consejo superior", 15),
            "consejero facultad": ("consejo directivo", 10),
            "responsable programa": ("responsable.*programa", 35),
            "participante programa": ("participante.*programa", 10),
            "miembro comisiones asesoras": ("comisi[oó]n asesora", 10),
            "otros antecedentes": ("otros antecedentes", 10)
        }
    }

    resultados = {}
    for area, subitems in items_detectados.items():
        resultados[area] = {}
        for nombre, (patron, puntaje) in subitems.items():
            encontrado = bool(re.search(patron, texto))
            resultados[area][nombre] = puntaje if encontrado else 0

    return resultados

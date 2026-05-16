import streamlit as st

st.set_page_config(
    page_title="Ayuda Uni",
    page_icon="🎓",
    layout="wide"
)

# --- Sidebar ---
with st.sidebar:
    st.title("🎓 Ayuda Uni")
    st.markdown("---")
    pagina = st.radio("Navegación", ["Inicio", "Contacto", "Recursos"])
    st.markdown("---")
    st.caption("Hecho para estudiantes")

# --- Página Inicio ---
if pagina == "Inicio":
    st.title("Bienvenido a Ayuda Uni")
    st.subheader("Resolvemos tus dudas universitarias en un solo lugar")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("""
        ### ¿Qué puedes hacer aquí?
        - Consultar información de trámites
        - Enviar tus preguntas directamente
        - Acceder a recursos útiles para la uni
        """)
        
        with st.expander("Ver cómo funciona"):
            st.write("1. Ve a la sección Contacto")
            st.write("2. Llena el formulario con tu duda")
            st.write("3. Te responderemos lo antes posible")
    
    with col2:
        st.info("💡 Tip: Usa el menú de la izquierda para moverte entre secciones")

# --- Página Contacto ---
elif pagina == "Contacto":
    st.title("Contáctanos")
    st.write("Déjanos tu duda y te respondemos pronto")
    
    with st.form("formulario_contacto", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            nombre = st.text_input("Nombre")
            carrera = st.selectbox("Carrera", ["Ingeniería", "Derecho", "Medicina", "Otra"])
        
        with col2:
            correo = st.text_input("Correo")
            asunto = st.selectbox("Asunto", ["Trámites", "Horarios", "Becas", "Otro"])
        
        mensaje = st.text_area("Escribe tu mensaje", height=150)
        
        enviado = st.form_submit_button("Enviar mensaje", type="primary")
        
        if enviado:
            if nombre and correo and mensaje:
                st.success(f"¡Gracias {nombre}! Recibimos tu mensaje sobre {asunto}.")
                st.balloons()
            else:
                st.error("Por favor completa todos los campos")

# --- Página Recursos ---
elif pagina == "Recursos":
    st.title("Recursos Útiles")
    
    tab1, tab2, tab3 = st.tabs(["Académico", "Trámites", "Bienestar"])
    
    with tab1:
        st.markdown("### Material académico")
        st.write("- Calendario académico")
        st.write("- Guías de estudio")
        st.write("- Biblioteca virtual")
    
    with tab2:
        st.markdown("### Trámites frecuentes")
        st.write("- Inscripción de materias")
        st.write("- Solicitud de constancias")
        st.write("- Revalidación de materias")
    
    with tab3:
        st.markdown("### Apoyo estudiantil")
        st.write("- Servicio psicológico")
        st.write("- Bolsa de trabajo")
        st.write("- Actividades extracurriculares")

# --- Footer ---
st.markdown("---")
st.caption("© 2026 Ayuda Uni | Hecho con Streamlit")

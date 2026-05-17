import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- Función para enviar correo ---
def enviar_correo(nombre, correo, asunto, mensaje):
    try:
        msg = MIMEText(
            f"Nuevo mensaje desde Ayuda Uni\n"
            f"Nombre: {nombre}\n"
            f"Correo: {correo}\n"
            f"Asunto: {asunto}\n\n"
            f"Mensaje:\n{mensaje}"
        )
        msg["Subject"] = f"[Ayuda Uni] {asunto} - {nombre}"
        msg["From"] = st.secrets["EMAIL_USER"]
        msg["To"] = st.secrets["EMAIL_USER"]

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(st.secrets["EMAIL_USER"], st.secrets["EMAIL_PASS"])
            server.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Error al enviar: {e}")
        return False

# --- Configuración de la página ---
st.set_page_config(page_title="Ayuda Uni", page_icon="🎓", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("🎓 Ayuda Uni")
    pagina = st.radio("Navegación", ["Inicio", "Contacto", "Recursos"])

# --- Página Contacto ---
if pagina == "Contacto":
    st.title("Contáctanos")
    
    with st.form("formulario_contacto", clear_on_submit=True):
        nombre = st.text_input("Nombre")
        correo = st.text_input("Correo")
        asunto = st.selectbox("Asunto", ["Trámites", "Horarios", "Becas", "Otro"])
        mensaje = st.text_area("Escribe tu mensaje", height=150)
        
        enviado = st.form_submit_button("Enviar mensaje", type="primary")
        
        if enviado:
            if nombre and correo and mensaje:
                with st.spinner("Enviando mensaje..."):
                    if enviar_correo(nombre, correo, asunto, mensaje):
                        st.success(f"¡Gracias {nombre}! Recibimos tu mensaje sobre {asunto}.")
                        st.balloons()
            else:
                st.error("Por favor completa todos los campos")

# --- Página Inicio ---
elif pagina == "Inicio":
    st.title("Bienvenido a Ayuda Uni")
    st.write("Resolvemos tus dudas universitarias en un solo lugar")

# --- Página Recursos ---
elif pagina == "Recursos":
    st.title("Recursos Útiles")
    st.write("- Calendario académico")
    st.write("- Guías de estudio")
    st.write("- Biblioteca virtual")

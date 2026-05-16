import streamlit as st
import smtplib
from email.mime.text import MIMEText

# --- Configuración de la página ---
st.set_page_config(
    page_title="Ayuda Uni",
    page_icon="🎓",
    layout="wide"
)

# --- Función para enviar correo ---
def enviar_correo(nombre, correo, asunto, mensaje):
    try:
        msg = MIMEText(
            f"Nuevo mensaje desde Ayuda Uni\n"
            f"Nombre: {nombre}\n"
            f"Correo: {correo}\n"
            f"Carrera: {carrera}\n"
            f"Asunto: {asunto}\n\n"
            f"Mensaje:\n{mensaje}"
        )
        msg["Subject"] = f"[Ayuda Uni] {asunto} - {nombre}"
        msg["From"] = st.secrets["EMAIL_USER"]
        msg["To"] = st.secrets["EMAIL_USER"]

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(st.secrets["EMAIL_USER"], st.secrets["EMAIL_PASS"])
            server.send

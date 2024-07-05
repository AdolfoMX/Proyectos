import streamlit as st
from streamlit_option_menu import option_menu

import pages_app.authenticator_user as stauth
from pages_app.interfaz_specialist.specialist_view import specialist_view_main
from pages_app.interfaz_patient.patient_view import patient_view_main

import time

import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="SLSM app",
    page_icon=".\\images\\latido-del-corazon.png",
    layout="centered",
    initial_sidebar_state="auto"
)

# Autenticación de usuarios

authenticator = stauth.Authenticate([""], [""], [""], "SLSM app", "auth", cookie_expiry_days=2)

#time.sleep(0.2)

# Inicio de sesión
name, authentication_status, username, rol_login = authenticator.login("Inicio de sesión", "main")

# Verificación
if st.session_state['authentication_status']:  
    time.sleep(0.08)
    
    if "rol_logout" not in st.session_state:
        st.session_state["rol_logout"] = authenticator
    
    if rol_login == 1:
        # Interfaz del especialista
        specialist_view_main()
    
    if rol_login == 2:
        # Interfaz de paciente
        patient_view_main()
    
elif st.session_state['authentication_status'] is False:
    st.error('Usuario/contraseña es incorrecto', icon="⛔")
    
    # Registro de usuario
    authenticator.register_user()
    
elif st.session_state['authentication_status'] is None:
    st.warning('Por favor ingrese su usuario y contraseña', icon="⚠️")
    
    # Registro de usuario
    authenticator.register_user()
import streamlit as st
from streamlit_option_menu import option_menu

from pages_app.interfaz_specialist.patients import patients_main
from pages_app.interfaz_specialist.visualizations import visualizations_main
from pages_app.interfaz_specialist.progress_record import progress_record_main
from pages_app.interfaz_specialist.home_specialist import home_specialist_main

def specialist_view_main():
    with st.sidebar:
        # Inicio de código
        st.markdown(
            """
            <style>
                [data-testid=stSidebar] [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-top: -24%;
                    margin-bottom: 2%;
                    margin-left: auto;
                    margin-right: auto%;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.image(".\\images\\icon_doctor.png", width=180, use_column_width=False)
        
        selectd = option_menu(
            menu_title="Menú principal",
            options=["Inicio", "Información de pacientes", "Registro de avances", "Visualizaciones"],
            icons=["house", "people", "percent", "bar-chart"]
        )           
        
        # Salir sesión
        st.session_state["rol_logout"].logout('Salir de sesión', 'main')
    
    # Secciones
    if selectd == "Inicio":        
        home_specialist_main()

    if selectd == "Información de pacientes":
        patients_main()

    if selectd == "Registro de avances":
        progress_record_main()

    if selectd == "Visualizaciones":
        visualizations_main()
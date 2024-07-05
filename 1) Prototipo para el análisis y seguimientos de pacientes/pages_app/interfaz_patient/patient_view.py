import streamlit as st
from streamlit_option_menu import option_menu

from pages_app.interfaz_patient.home_patient import home_patient
from pages_app.interfaz_patient.form_slsm import form_main
from pages_app.interfaz_patient.information_patient import information_patient_main
from pages_app.interfaz_patient.visualizations_patient import visualizations_patient_main
from pages_app.interfaz_patient.progress_record_patient import progress_record_patient_main

def patient_view_main():
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
        
        st.image(".\\images\\icon_patient.png", width=180, use_column_width=False)
        
        selectd = option_menu(
            menu_title="Menú principal",
            options=["Inicio", "Acerca de mi", "Cuestionario SLSM", "Avances", "Resultados"],
            icons=["house", "file-earmark-person", "file-medical", "percent", "bar-chart"]
        )           
        
        # Salir sesión
        st.session_state["rol_logout"].logout('Salir de sesión', 'main')
    
    # Secciones
    if selectd == "Inicio":
        home_patient()        
        #st.write(f"Haz seleccionado {selectd}") 

    if selectd == "Acerca de mi":
        information_patient_main()
        
    if selectd == "Cuestionario SLSM":
        form_main()

    if selectd == "Avances":
        progress_record_patient_main()

    if selectd == "Resultados":
        visualizations_patient_main()
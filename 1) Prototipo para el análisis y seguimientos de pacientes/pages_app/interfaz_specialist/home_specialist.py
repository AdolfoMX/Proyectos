import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

def home_specialist_main():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
            """, unsafe_allow_html=True
        )
        
    st.title(":blue[Inicio]")
    st.subheader("", divider="rainbow")
    
    text_colum1, image_column2 = st.columns(2)

    with text_colum1:
        st.write("")
        st.write(f"**Querido(a), Dr(a) :blue[{st.session_state.name}],**")
        st.write(
        """
        Eres la pieza vital de este rompecabezas, la chispa que ilumina el camino hacia un estilo de vida equilibrado. Con tu conocimiento y pasión, inspiras el cambio y la esperanza en aquellos que buscan una vida mejor.

        Cada consulta, cada palabra, y cada gesto tuyo tiene el poder de transformar vidas. Recordemos siempre que la medicina está en tu voz, en tu apoyo y en tu empatía. Sigamos avanzando juntos, motivando día a día, construyendo un mundo donde la salud es un regalo que todos merecen.

        Bienvenido a un viaje de propósito, motivación y cambio! Juntos, haremos la diferencia en la salud de nuestra comunidad.
        """
        )
    
    with image_column2:
        with open("images/doctor_home_specialist.json", "r",errors='ignore') as f:
            data = json.load(f)
        st.markdown("<br><br>",unsafe_allow_html=True)
        st_lottie(data, width=300)


    st.write("**¡Gracias por ser parte del Equipo de Salud Latina Sin Medicina!**")
import streamlit as st
import mysql.connector

def general_data_view(id_user):
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    cursor = cnx.cursor()
    sql = f"SELECT nombre, apellidos, correo FROM usuarios WHERE id_usuario = '{id_user}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    sql2 = f"SELECT fecha_nacimiento, numero_telefono, genero FROM historiales_medicos WHERE id_usuario = '{id_user}'"
    cursor.execute(sql2)
    result2 = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    if not result2:
        result2 = [("", "", "")]
        
    col1_genel, col2_genel = st.columns(2)
    
    with col1_genel:
        st.text_input("Nombre", value=result[0][0], disabled=True)
        st.text_input("Correo electrónico", value=result[0][2], disabled=True)
        st.text_input("Fecha de nacimiento", value=result2[0][0], disabled=True)
        
    with col2_genel:
        st.text_input("Apellidos", value=result[0][1], disabled=True)
        st.text_input("Número de teléfono", value=result2[0][1], disabled=True)
        st.text_input("Sexo", value=result2[0][2], disabled=True)


def medical_history_view(id_user):
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    cursor = cnx.cursor()
    sql = f"SELECT * FROM historiales_medicos WHERE id_usuario = '{id_user}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    
    cursor.close()
    cnx.close()
    
    if result:
        # colocar aqui visualizacion del formulario
        st.subheader("Sección Salud Física")
        col1_sec2, col2_sec2 = st.columns(2)

        with col1_sec2:
            st.text_input("¿Haces alguna actividad física?", value=result[0][7], disabled=True)
            st.text_input("¿Tienes sobrepeso?", value=result[0][9], disabled=True)
            st.text_input("Cuántos años con sobrepeso lleva", value=result[0][11], disabled=True)
            st.text_area("¿Qué complicaciones ha tenido (sobrepeso)?", value=result[0][13], disabled=True)
            st.text_input("Cuántos días a la semana hace ejercicio moderado", value=result[0][15], disabled=True)
            st.text_area("Cuando no hace ejercicio, ¿qué se lo impide?", value=result[0][17], disabled=True)
            
        with col2_sec2:
            st.text_input("¿Cuántos días a la semana realizas actividad física?", value=result[0][8], disabled=True)
            st.text_input("¿Cuántos kilos de sobrepeso tiene?", value=result[0][10], disabled=True)
            st.text_input("¿Ha tenido alguna complicación por el sobrepeso?", value=result[0][12], disabled=True)
            st.text_input("Cuántos minutos hace ejercicio moderado", value=result[0][14], disabled=True)
            st.text_area("¿Qué le motiva hacer ejercicio?", value=result[0][16], disabled=True)
            st.text_area("¿El ejercicio le causa problemas de salud?",value=result[0][18], disabled=True)
            
        st.text_area("¿Sabe cuándo su cuerpo está tenso o estresado?", value=result[0][19], disabled=True)

        st.divider()

        # Sección 3 de preguntas
        st.subheader("Sección Enfermedades crónicas")
        col1_sec3, col2_sec3 = st.columns(2)

        with col1_sec3:
            st.text_input("¿Tiene hipertensión?", value=result[0][20], disabled=True)
            st.text_input("¿Ha tenido alguna complicación por la hipertensión?", value=result[0][22], disabled=True)
            st.text_input("¿Tiene diabetes?", value=result[0][24], disabled=True)
            st.text_input("¿Ha tenido alguna complicación por la diabetes?", value=result[0][26], disabled=True)
            st.text_input("¿Tiene alguna enfermedad cardíaca?", value=result[0][28], disabled=True)
            st.text_input("¿Ha tenido alguna complicación por la enfermedad cardíaca?", value=result[0][30], disabled=True)
            st.text_input("¿Tiene alguna enfermedad cerebral?", value=result[0][32], disabled=True)
            st.text_input("¿Ha tenido alguna complicación por la enfermedad cerebral?", value=result[0][34], disabled=True)

        with col2_sec3:
            st.text_input("¿Cuántos años lleva padeciendo de hipertensión?", value=result[0][21], disabled=True)
            st.text_area("¿Qué complicaciones ha tenido por la hipertensión?", value=result[0][23], disabled=True)
            st.text_input("¿Cuántos años lleva padeciendo de diabetes?", value=result[0][25], disabled=True)
            st.text_area("¿Qué complicaciones ha tenido por la diabetes?", value=result[0][27], disabled=True)
            st.text_input("¿Cuántos años lleva padeciendo la enfermedad cardíaca?", value=result[0][29], disabled=True)
            st.text_area("¿Qué complicaciones ha tenido por la enfermedad cardíaca?", value=result[0][31], disabled=True)
            st.text_input("¿Cuántos años lleva padeciendo la enfermedad cerebral?", value=result[0][33], disabled=True)
            st.text_area("¿Qué complicaciones ha tenido por la enfermedad cerebral?", value=result[0][35], disabled=True)

        st.text_area("¿Qué otras enfermedades crónicas ha tenido?", value=result[0][36], disabled=True)
            
        st.divider()

        # Sección 4 de preguntas
        st.subheader("Sección Salud mental")
        col1_sec4, col2_sec4 = st.columns(2)

        with col1_sec4:
            st.text_input("¿Siente que no tiene control en cosas importantes de su vida?", value=result[0][37], disabled=True)
            st.text_input("¿Siente que su vida no va como quisiera?", value=result[0][39], disabled=True)
            st.text_area("¿Qué tan frecuente siente que su vida no tiene próposito o sentido?",value=result[0][41], disabled=True)
            st.text_input("¿Sus pensamientos o emociones afectan su salud física?", value=result[0][43], disabled=True)
            st.text_input("¿Se ha sentido abatido, deprimido o sin esperanza?", value=result[0][45], disabled=True)
            st.text_input("¿Siente que es un fracaso para si mismo o su familia?", value=result[0][47], disabled=True)
            st.text_input("¿Fácilmente se irrita o molesta?", value=result[0][49], disabled=True)
            st.text_input("¿Cuándo sufre estrés extremo siente que puede aprender de eso?", value=result[0][51], disabled=True)
            st.text_input("¿Cumple sus propias metas?", value=result[0][53], disabled=True)
            st.text_input("¿Hay personas que le apoyan en caso necesario?", value=result[0][55], disabled=True)
            st.text_input("¿Está satisfecho con su Sistema de Creencias?", value=result[0][57], disabled=True)

        with col2_sec4:
            st.text_input("¿Se siente incapaz de manejar sus problemas personales?", value=result[0][38], disabled=True)
            st.text_input("¿Siente que no puede librarse de lo que le molesta?", value=result[0][40], disabled=True)
            st.text_input("¿En su vida ha pensado seriamente suicidarse?", value=result[0][42], disabled=True)
            st.text_input("¿En las ultimas 3 semanas ha sentido poca alegría o placer de las cosas?", value=result[0][44], disabled=True)
            st.text_input("¿Ha perdido el apetito o come demasiado a causa de su estado emocional?", value=result[0][46], disabled=True)
            st.text_input("¿Tiene problemas para concentrarse?", value=result[0][48], disabled=True)
            st.text_area("Si tu respuesta anterior es sí, ¿Qué realizas para controlarlo?",value=result[0][50], disabled=True)
            st.text_input("¿Le es fácil saber lo que es prioritario?", value=result[0][52], disabled=True)
            st.text_input("¿Vive una vida con propósito o significado?", value=result[0][54], disabled=True)
            st.text_input("¿Tiene su propia fortaleza interna?", value=result[0][56], disabled=True)
            st.text_area("¿Cómo califica su vida social?",value=result[0][58], disabled=True)

        st.divider()

        # Sección 5 de preguntas
        st.subheader("Sección Conciliación del sueño")
        col1_sec5, col2_sec5 = st.columns(2)

        with col1_sec5:
            st.text_input("¿Tiene algún problema de salud que le impide dormir?", value=result[0][59], disabled=True)
            st.text_input("¿Se despierta en la noche y no puede volver a dormir?", value=result[0][61], disabled=True)
            st.text_input("¿Su trabajo le obliga a estar despierto de noche?", value=result[0][63], disabled=True)
            st.text_input("¿Cuantás horas al día duerme habitualmente?", value=result[0][65], disabled=True)
            
        with col2_sec5:
            st.text_area("Si su respuesta fue afirmativa, ¿qué problema de salud tiene?", value=result[0][60], disabled=True)
            st.text_input("¿Sus problemas le quitan el sueño o le hacen dormir mucho?", value=result[0][62], disabled=True)
            st.text_input("¿Necesita hacer siesta?", value=result[0][64], disabled=True)
            
        st.divider()

        # Sección 6 de preguntas
        st.subheader("Sección Alimentación")
        col1_sec6, col2_sec6 = st.columns(2)

        with col1_sec6:
            st.text_input("¿Cuántas veces ingiere comida “chatarra” a la semana?", value=result[0][65], disabled=True)
            st.text_input("¿Ha intentado alguna dieta o plan de nutrición?", value=result[0][67], disabled=True)
            st.text_input("¿Cena abundante?", value=result[0][69], disabled=True)
            
        with col2_sec6:
            st.text_input("¿Cuál es su tipo de alimentación?", value=result[0][66], disabled=True)
            st.text_input("¿Respeta sus “horas de comida” a lo largo del día?", value=result[0][68], disabled=True)
            st.text_input("¿Sentirse estresado le motiva a tomar alimentos?", value=result[0][70], disabled=True)

        st.divider()

        # Sección 7 de preguntas
        st.subheader("Sección Adicciones y/o consumos")
        col1_sec7, col2_sec7 = st.columns(2)

        with col1_sec7:
            st.text_input("A lo largo de su vida ¿ha fumado más de 100 cigarrillos (5 paquetes)?", value=result[0][71], disabled=True)
            st.text_area("En el ultimo año, ¿con qué frecuencia ha consumido bebidas alcohólicas?",value=result[0][73], disabled=True)

        with col2_sec7:
            st.text_input("¿Ha usado fármacos para bajar de peso?", value=result[0][72], disabled=True)
            st.text_input("¿Se ha sentido culpable por su forma de beber o le critican por ello?", value=result[0][74], disabled=True)

        st.divider()

        # Sección extra
        st.subheader("Sección extra")
        col1_ext, col2_ext = st.columns(2)

        with col1_ext:
            st.text_input("¿Su salud actual le limita hacer su vida normal?", value=result[0][75], disabled=True)
            st.text_area("¿Cuánta confianza tiene de recuperar su buena salud?", value=result[0][77], disabled=True)
            st.text_area("¿Cuáles serían las 5 causas por las que podría fallar de la pregunta anterior?", value=result[0][79], disabled=True)

        with col2_ext:
            st.text_area("De la pregunta anterior describe el porque", value=result[0][76], disabled=True)
            st.text_area("¿Qué fortalezas personales o familiares usará en su propósito de salud?", value=result[0][78], disabled=True)
            st.text_input("Seleccione sus 3 propósitos más importantes", value=result[0][80], disabled=True)
    else:
        st.warning("Complete el cuestionario SLSM para visualizar la informacion", icon="⚠️")
    

def information_patient_main():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
                
                div[data-testid="stExpander"] div[role="button"] p {
                    font-size: 1.1rem;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.title(":blue[Perfil]")
        
        with st.expander("**Datos generales**"):
            general_data_view(st.session_state['id_user'])
         
        with st.expander("**Historial médico**"):
            medical_history_view(st.session_state['id_user'])

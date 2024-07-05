import streamlit as st
from streamlit_option_menu import option_menu

import mysql.connector
import datetime as dt
import re

def check_users_db(full_name):
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    cursor = cnx.cursor()
    
    sql = f"SELECT id_usuario, CONCAT(nombre, ' ', apellidos) AS nombre_completo FROM usuarios WHERE id_rol = 2 AND CONCAT(nombre, ' ', apellidos) LIKE '%{full_name}%'"
    cursor.execute(sql)

    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    
    return result


def sentence_sql():
    sql = """
        INSERT INTO hojas_evolucion_medico (
            id_usuario,
            fecha_registro,
            peso,
            IMC,
            grasa_viseral,
            porcentaje_musculo,
            abdomen,
            ejercicio,
            horas_sueno,
            talla,
            grasa_corporal,
            edad_metabolica,
            calorias,
            glucosa,
            comida_chatarra,
            calidad_sueno,
            notas
        ) 
        VALUES (%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,	%s,
                %s,	%s,	%s,	%s,	%s,	%s,	%s	                   
        )
    """
    return sql


def form(id_user):
    with st.form("Hoja de evolución", clear_on_submit=True):
        current_date = dt.date.today()
        #current_date = dt.datetime.strptime('07/10/2023', '%d/%m/%Y')
        #current_date = current_date.date()
        #st.write(current_date)
        date_now = st.text_input(":blue[Fecha de registro]", value=current_date.strftime("%d/%m/%y"), disabled=True)

        col1_sec1, col2_sec1 = st.columns(2)

        with col1_sec1:
            weight = st.number_input('Peso (kg)', min_value=0.0, max_value=200.0, format="%0.2f")
            IMC = st.number_input('Índice de masa corporal (IMC)', min_value=0.0, max_value=40.0, format="%0.2f")
            visceral_fat = st.number_input('Grasa visceral (%)', min_value=0.0, max_value=60.0, format="%0.2f")
            muscle = st.number_input('Porcentaje de musculo (%)', min_value=0.0, max_value=45.0, format="%0.2f")
            abdomen = st.number_input('Perimetro abdominal (cm)', min_value=0.0, max_value=120.0, format="%0.2f")
            exercise = st.number_input('Minutos al día de ejercicio', min_value=1, max_value=720)
            hours_sleep = st.number_input('Horas de sueño', min_value=1, max_value=12)

        with col2_sec1:
            size = st.number_input('Talla (cm)', min_value=0, max_value=100)
            body_fat = st.number_input('Porcentaje de grasa corporal (%)', min_value=0.0, max_value=40.0, format="%0.2f")
            metabolic_age = st.number_input('Edad metabólica', min_value=1, max_value=100)
            calories = st.number_input('Consumo de calorias (kcal)', min_value=1000, max_value=3000)
            glucose = st.number_input('Glucosa en sangre (mg/dl)', min_value=1, max_value=3000)
            junk_food = st.selectbox('Apetito de comida chatarra', ("Mucha","Poca", "Casi nada", "Nada"), index=0, placeholder="Seleciona una opcion")
            sleep_quality = st.selectbox('Calidad de sueño', ("Bastante buena","Buena", "Mala", "Bastante mala"), index=0, placeholder="Seleciona una opcion")
        notes = st.text_area('Notas de la sesión', max_chars=200)

        submitted = st.form_submit_button("Enviar")
        if submitted:
            try:
                cnx = mysql.connector.connect(
                    user='root', 
                    password='root',
                    host='127.0.0.1',
                    database='slsm_db'
                )

                cursor = cnx.cursor()
                sql_last_date = f"SELECT * FROM hojas_evolucion_medico AS a INNER JOIN(SELECT id_usuario, MAX(fecha_registro) AS fecha_max FROM hojas_evolucion_medico GROUP BY id_usuario) AS b ON a.id_usuario = b.id_usuario AND a.fecha_registro = b.fecha_max WHERE a.id_usuario = {id_user}"
                
                cursor.execute(sql_last_date)
                result_date = cursor.fetchall()
                
                if not result_date:
                    sql = sentence_sql()
                    val = (
                        id_user,
                        current_date,
                        weight,
                        IMC,
                        visceral_fat,
                        muscle,
                        abdomen,
                        exercise,
                        hours_sleep,
                        size,
                        body_fat,
                        metabolic_age,
                        calories,
                        glucose,
                        junk_food,
                        sleep_quality,
                        notes
                    )

                    cursor.execute(sql, val)
                    cnx.commit()
                    
                    st.success('La información ha sido registrada!', icon="✅")
                    cursor.close()
                    cnx.close()
                else:
                    if result_date[0][2] == current_date:
                        cursor.close()
                        cnx.close()
                        st.info("Sólo puede hacer un registro por día", icon="📋")
                    else:
                        sql = sentence_sql()
                        val = (
                            id_user,
                            current_date,
                            weight,
                            IMC,
                            visceral_fat,
                            muscle,
                            abdomen,
                            exercise,
                            hours_sleep,
                            size,
                            body_fat,
                            metabolic_age,
                            calories,
                            glucose,
                            junk_food,
                            sleep_quality,
                            notes
                        )

                        cursor.execute(sql, val)
                        cnx.commit()
                        
                        st.success('La información ha sido registrada!', icon="✅")
                        cursor.close()
                        cnx.close()
            except:
                st.warning("Por favor asegurese de llenar todos los campos", icon="⚠️")


def evolution_sheets(id_user):
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    #current_date.strftime("%d/%m/%y")
    date = st.date_input("Selecciona una fecha de búsqueda", min_value=dt.date(2023,1,1), format="DD/MM/YYYY")
    
    cursor = cnx.cursor()
    sql = f"SELECT * FROM hojas_evolucion_medico WHERE id_usuario = {id_user} AND fecha_registro = '{date}'"
    cursor.execute(sql)
    result = cursor.fetchall()

    if not result:
        st.warning("No se encontraron registros de esa fecha", icon="⚠️")
    else:
        for i in range(len(result)):
            st.subheader(f":date: {i+1}. Fecha: :blue[{result[i][2]}]", divider='red')
            
            with st.expander("**Ver hoja**..."):
                col1_sec1, col2_sec1 = st.columns(2)

                with col1_sec1:
                    st.text_input('Peso (kg)', value=result[i][3], disabled=True, key=f"{i+1}.1")
                    st.text_input('Índice de masa corporal (IMC)', value=result[i][4], disabled=True, key=f"{i+1}.2")
                    st.text_input('Grasa visceral (%)', value=result[i][5], disabled=True, key=f"{i+1}.3")
                    st.text_input('Porcentaje de musculo (%)', value=result[i][6], disabled=True, key=f"{i+1}.4")
                    st.text_input('Perimetro abdominal (cm)', value=result[i][7], disabled=True, key=f"{i+1}.5")
                    st.text_input('Minutos al día de ejercicio', value=result[i][8], disabled=True, key=f"{i+1}.6")
                    st.text_input('Horas de sueño', value=result[i][9], disabled=True, key=f"{i}.7")

                with col2_sec1:
                    st.text_input('Talla (cm)', value=result[i][10], disabled=True, key=f"{i+1}.8")
                    st.text_input('Porcentaje de grasa corporal (%)', value=result[i][11], disabled=True, key=f"{i+1}.9")
                    st.text_input('Edad metabólica', value=result[i][12], disabled=True, key=f"{i+1}.10")
                    st.text_input('Consumo de calorias (kcal)', value=result[i][13], disabled=True, key=f"{i+1}.11")
                    st.text_input('Glucosa en sangre (mg/dl)', value=result[i][14], disabled=True, key=f"{i+1}.12")
                    st.text_input('Apetito de comida chatarra', value=result[i][15], disabled=True, key=f"{i+1}.13")
                    st.text_input('Calidad de sueño', value=result[i][16], disabled=True, key=f"{i+1}.14")
                    
                st.text_area('Notas de la sesión', value=result[i][17], disabled=True, key=f"{i+1}.15")
            
    cursor.close()
    cnx.close()


def patient_notes(id_user):
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='127.0.0.1',
        database='slsm_db'
    )
    
    #current_date.strftime("%d/%m/%y")
    date = st.date_input("Selecciona una fecha de búsqueda", min_value=dt.date(2023,1,1), format="DD/MM/YYYY")
    
    cursor = cnx.cursor()
    sql = f"SELECT * FROM avances_usuarios WHERE id_usuario = {id_user} AND fecha_registro = '{date}'"
    
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if not result:
        st.warning("No se encontraron registros de esa fecha", icon="⚠️")
    else:
        for i in range(len(result)):
            st.subheader(f":date: {i+1}. Fecha: :blue[{result[i][2]}]", divider='red')
            
            with st.expander("**Ver hoja**..."):
            
                st.subheader("Sección 1. Salud física")
                col1_sec1, col2_sec1 = st.columns(2)

                with col1_sec1:
                    st.text_input('Indique del 1 al 10 cómo se siente físicamente tras la última sesión:', value=result[i][3], disabled=True, key=f"{i+1}.1")

                with col2_sec1:
                    st.text_input('¿Cómo se sintió físicamente?', value=result[i][4], disabled=True, key=f"{i+1}.2")

                st.text_area('¿Notó mejoras?', value=result[i][5], disabled=True, key=f"{i+1}.3")   

                st.divider()
                
                st.subheader("Sección 2. Enfermedades crónicas")
                col1_sec2, col2_sec2 = st.columns(2)
                        
                with col1_sec2:
                    st.text_input('Indique del 1 al 10 cuánto considera que ha progresado en su salud', value=result[i][6], disabled=True, key=f"{i+1}.4")
                
                with col2_sec2:
                    st.text_input('¿Cómo se sintió respecto a su salud?', value=result[i][7], disabled=True, key=f"{i+1}.5")
                
                st.text_area('¿Notó mejoras?', value=result[i][8], disabled=True, key=f"{i+1}.6")
                
                st.divider()

                st.subheader("Sección 3. Salud mental")
                col1_sec3, col2_sec3 = st.columns(2)
                
                with col1_sec3:
                    st.text_input('Indique del 1 al 10 cuánto considera que ha progresado en su salud mental', value=result[i][9], disabled=True, key=f"{i+1}.7")
                
                with col2_sec3:
                    st.text_input('¿Cómo se sintió respecto a su salud mental?', value=result[i][10], disabled=True, key=f"{i+1}.8")
                
                st.text_area('¿Notó mejoras?', value=result[i][11], disabled=True, key=f"{i+1}.9")
                
                st.divider()

                st.subheader("Sección 4. Conciliación del sueño")
                col1_sec4, col2_sec4 = st.columns(2)
                    
                with col1_sec4:
                    st.text_input('Indique del 1 al 10 cuánto considera que ha progresado en su conciliación del sueño', value=result[i][12], disabled=True, key=f"{i+1}.10")
                
                with col2_sec4:
                    st.text_input('¿Cómo se sintió respecto a su sueño?', value=result[i][13], disabled=True, key=f"{i+1}.12")
                
                st.text_area('¿Notó mejoras?', value=result[i][14], disabled=True, key=f"{i+1}.13")
                
                st.divider()

                st.subheader("Sección 5. Alimentación")
                col1_sec5, col2_sec5 = st.columns(2)
                
                with col1_sec5:
                    st.text_input('Indique del 1 al 10 cuánto considera que ha progresado en su alimentación', value=result[i][15], disabled=True, key=f"{i+1}.14")
                
                with col2_sec5:
                    st.text_input('¿Cómo se sintió respecto a su alimentación?', value=result[i][16], disabled=True, key=f"{i+1}.15")
                
                st.text_area('¿Notó mejoras?', value=result[i][17], disabled=True, key=f"{i+1}.16")
                
                st.divider()

                st.subheader("Sección 6. Adicciones y/o consumos")
                col1_sec6, col2_sec6 = st.columns(2)
                
                with col1_sec6:
                    st.text_input('Indique del 1 al 10 cuánto considera que ha progresado en las adicciones y/o consumo (tabaco y/o alcohol)', value=result[i][18], disabled=True, key=f"{i+1}.17")
                
                with col2_sec6:
                    st.text_input('¿Cómo se sintió respecto al consumo y/o adicciones?', value=result[i][19], disabled=True, key=f"{i+1}.18")
                
                st.text_area('¿Notó mejoras?', value=result[i][20], disabled=True, key=f"{i+1}.19")
                
                st.divider()

                st.subheader("Sección 7. Avances generales")
                st.text_area('En general, ¿Cómo se sintió tras esta última sesión?', value=result[i][21], disabled=True, key=f"{i+1}.20")

                st.divider()
            
    cursor.close()
    cnx.close()


def progress_record_main():
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
        
        if 'list_users' not in st.session_state:
            st.session_state['list_users'] = [""]
        
        st.title(":blue[Registro y consulta de avances]")
        
        col1, col2 = st.columns(2)        
        with col1:
            search_pacient = st.text_input("Buscador", value="")
            submitted = st.button("Enviar")

        if submitted:
            search_pacient = " ".join(search_pacient.upper().split())
            
            if search_pacient != "":
                results_db = check_users_db(" ".join(search_pacient.upper().split()))
                
                if not results_db:
                    st.session_state['list_users'] = [""]
                    st.warning("El paciente no está registrado", icon="⚠️")
                else:
                    st.session_state['list_users'] = ["ID " + str(data[0]) + ". "+ data[1] for data in results_db]
        
        with col2:
            selectd_user = st.selectbox("Paciente(s)", st.session_state['list_users'])
            st.info(f"[Selección]: {selectd_user}", icon="📋")
            
        st.subheader("", divider="red")
        
        if selectd_user != "":
            id_user = re.search(r"\d+", selectd_user)
            id_user = int(id_user.group())
            
            selectd = option_menu(
                menu_title=None,
                options=["Formulario", "Hojas de progreso", "Notas del paciente"],
                orientation="horizontal"
            )
            
            if selectd == "Formulario":
                form(id_user)
            
            if selectd == "Hojas de progreso":
                evolution_sheets(id_user)
                
            if selectd == "Notas del paciente":
                patient_notes(id_user)

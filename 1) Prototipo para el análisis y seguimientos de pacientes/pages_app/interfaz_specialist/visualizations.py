import streamlit as st

import mysql.connector
import re

import pandas as pd
import plotly.express as px

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


def general_data_view(id_user):
    
    cnx = mysql.connector.connect(
        user='root', 
        password='root',
        host='127.0.0.1',
        database='slsm_db'
    )

    cursor = cnx.cursor()
    sql = f"SELECT * FROM hojas_evolucion_medico WHERE id_usuario = {id_user}"
    cursor.execute(sql)
    result = cursor.fetchall()

    sql2 = f"SELECT * FROM avances_usuarios WHERE id_usuario = {id_user}"
    cursor.execute(sql2)
    result2 = cursor.fetchall()

    sql3 = f"SELECT * FROM hojas_evolucion_medico AS a INNER JOIN(SELECT id_usuario, MAX(fecha_registro) AS fecha_max FROM hojas_evolucion_medico GROUP BY id_usuario) AS b ON a.id_usuario = b.id_usuario AND a.fecha_registro = b.fecha_max WHERE a.id_usuario = {id_user};"

    cursor.execute(sql3)
    result3 = cursor.fetchall()

    cursor.close()
    cnx.close()
    
    peso, porc_grasa, porc_musc = st.columns(3)
    horas_sueno, min_ejercicio = st.columns(2)
    medidas, progreso_general = st.columns(2)
    
    if result:
        if result3:
            peso.metric(
                label="Peso (kg)",
                value= result3[0][3],
            )

            porc_grasa.metric(
                label= "Porcentaje de masa muscular %",
                value= result3[0][6],
            )

            porc_musc.metric(
                label= "Porcentaje de grasa corporal %",
                value= result3[0][11],
            )

        #Conversion a data frame de tabla 1
        df_result = pd.DataFrame(result)
        columns_list = [str(i) for i in range(0,18)]
        df_result.columns = columns_list
        
        df_result.rename(columns= { '0': 'id_hojas',
                                    '1': 'id_usuario',
                                    '2': 'fecha_registro',
                                    '3': 'peso',
                                    '4': 'IMC',
                                    '5': 'grasa_viseral',
                                    '6': 'porcentaje_musculo',
                                    '7': 'abdomen',
                                    '8': 'ejercicio',
                                    '9': 'horas_sueno',
                                    '10': 'talla',
                                    '11': 'grasa_corporal',
                                    '12': 'edad_metabolica',
                                    '13': 'calorias',
                                    '14': 'glucosa',
                                    '15': 'comida_chatarra',
                                    '16': 'calidad_sueno',
                                    '17': 'notas'
                                }, inplace=True)

        df_result['fecha_registro'] = pd.to_datetime(df_result['fecha_registro'], format="%d/%m/%Y")
        
        #Gráfico de horas de sueño
        horas_sueno.write("##### Horas de sueño")
        with horas_sueno:
            chart_sueno = px.line(df_result, x='fecha_registro', y='horas_sueno', width=300, height=300, markers=True, color_discrete_sequence=['#FF4B4B']) 
            st.plotly_chart(chart_sueno)
            
        #Gráfico de mins al día de ejercicio
        min_ejercicio.write("##### Minutos al día de ejercicio")
        with min_ejercicio:
            chart_ejercicio = px.line(df_result, x='fecha_registro', y='ejercicio', width=300, height=300, markers=True, template="seaborn", color_discrete_sequence=['#FF4B4B'])
            st.plotly_chart(chart_ejercicio)
        
        #Gráfico de Índice de masa corporal
        medidas.write('##### Índice de masa corporal')
        with medidas:
            fig_medidas = px.bar(df_result, x='fecha_registro', y='IMC', color_discrete_sequence=['#0068C9'], width=300, height=300)
            st.plotly_chart(fig_medidas)
    else:
        st.warning("No hay datos de progreso encontrados", icon="⚠️")
        
    if result2:
        #Conversion a data frame de tabla 2
        df_result2 = pd.DataFrame(result2)
        columns_list2 = [str(i) for i in range(0,22)]
        df_result2.columns = columns_list2
        
        df_result2.rename(columns= {'0': 'id_avance',
                                    '1': 'id_usuario',
                                    '2': 'fecha_registro',
                                    '3': 'pregunta1_sec1',
                                    '4': 'notas1_sec1',
                                    '5': 'notas2_sec1',
                                    '6': 'pregunta1_sec2',
                                    '7': 'notas1_sec2',
                                    '8': 'notas2_sec2',
                                    '9': 'pregunta1_sec3',
                                    '10': 'notas1_sec3',
                                    '11': 'notas2_sec3',
                                    '12': 'pregunta1_sec4',
                                    '13': 'notas1_sec4',
                                    '14': 'notas2_sec4',
                                    '15': 'pregunta1_sec5',
                                    '16': 'notas1_sec5',
                                    '17': 'notas2_sec5',
                                    '18': 'pregunta1_sec6',
                                    '19': 'notas1_sec6',
                                    '20': 'notas2_sec6',
                                    '21': 'pregunta1_sec7',

                                }, inplace=True)

        #Extrae el progreso general del paciente (como se ha sentido del 1 al 10)
        new_table2 = (df_result2[["pregunta1_sec1", "pregunta1_sec2", "pregunta1_sec3", "pregunta1_sec4", "pregunta1_sec5", "pregunta1_sec6"]])
        progress_patient = new_table2.transpose()

        progress_patient.rename(index= {'pregunta1_sec1': 'Salud física',
                                'pregunta1_sec2': 'Enfermedades',
                                'pregunta1_sec3': 'Salud mental',
                                'pregunta1_sec4': 'Conciliación del sueño',
                                'pregunta1_sec5': 'Alimentación',
                                'pregunta1_sec6': 'Adicciones y/o consumos',
                                }, inplace=True)

        progreso_general.write('##### Sentir general del paciente')
        with progreso_general:
            fig_progreso_general = px.bar(progress_patient,
                                        x=0,
                                        y=progress_patient.index,
                                        orientation="h",
                                        color_discrete_sequence=["#0068C9"] *len(progress_patient),
                                        width=400, height=300,
                                        )
            st.plotly_chart(fig_progreso_general)
    else:
        st.warning("No hay notas del paciente encontrados", icon="⚠️")
    

def progress_visual_patient(id_user):
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
    
    if not result:
        st.warning("El usuario no se encuentra registrado", icon="⚠️")
    else:            
        general_data_view(id_user)
                
    cursor.close()
    cnx.close()


def visualizations_main():
    with st.container():
        st.markdown(
            """
            <style>
                .css-1y4p8pa {
                    margin-top: -6rem;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.title(":blue[Gráficas de progreso]")

        if 'list_search_users_sv' not in st.session_state:
            st.session_state['list_search_users_sv'] = [""]
        
        col1, col2 = st.columns(2)        
        with col1:
            search_pacient = st.text_input("Buscador", value="")
            submitted = st.button("Enviar")

        if submitted:
            search_pacient = " ".join(search_pacient.upper().split())
            
            if search_pacient != "":
                results_db = check_users_db(" ".join(search_pacient.upper().split()))
                
                if not results_db:
                    st.session_state['list_search_users_sv'] = [""]
                    st.warning("El paciente no está registrado", icon="⚠️")
                else:
                    st.session_state['list_search_users_sv'] = ["ID " + str(data[0]) + ". "+ data[1] for data in results_db]
        
        with col2:
            selectd_user = st.selectbox("Paciente(s)", st.session_state['list_search_users_sv'])
            st.info(f"[Selección]: {selectd_user}", icon="📋")
            
        st.subheader("", divider="red")
        
        if selectd_user != "":
            id_user = re.search(r"\d+", selectd_user)
            id_user = int(id_user.group())
            progress_visual_patient(id_user)
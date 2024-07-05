import jwt
import bcrypt
import mysql.connector
from datetime import datetime, timedelta

import streamlit as st
import extra_streamlit_components as stx
import streamlit.components.v1 as components
import time

class Hasher:
    def __init__(self, passwords):
        """Create a new instance of "Hasher".
        Parameters
        ----------
        passwords: list
            The list of plain text passwords to be hashed.
        Returns
        -------
        list
            The list of hashed passwords.
        """
        self.passwords = passwords

    def hash(self, password):
        """
        Parameters
        ----------
        password: str
            The plain text password to be hashed.
        Returns
        -------
        str
            The hashed password.
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    def generate(self):
        """
        Returns
        -------
        list
            The list of hashed passwords.
        """
        hashedpw = []

        for password in self.passwords:
            hashedpw.append(self.hash(password))
        return hashedpw

class Authenticate:
    def __init__(self, names, usernames, passwords, cookie_name, key, cookie_expiry_days=30):
        """Create a new instance of "Authenticate".
        Parameters
        ----------
        names: list
            The list of names of users.
        usernames: list
            The list of usernames in the same order as names.
        passwords: list
            The list of hashed passwords in the same order as names.
        cookie_name: str
            The name of the JWT cookie stored on the client's browser for passwordless reauthentication.
        key: str
            The key to be used for hashing the signature of the JWT cookie.
        cookie_expiry_days: int
            The number of days before the cookie expires on the client's browser.
        Returns
        -------
        str
            Name of authenticated user.
        boolean
            The status of authentication, None: no credentials entered, False: incorrect credentials, True: correct credentials.
        str
            Username of authenticated user.
        """
        self.names = names
        self.usernames = usernames
        self.passwords = passwords
        self.cookie_name = cookie_name
        self.key = key
        self.cookie_expiry_days = cookie_expiry_days
        self.cookie_manager = stx.CookieManager()

        if 'name' not in st.session_state:
            st.session_state['name'] = None
        if 'authentication_status' not in st.session_state:
            st.session_state['authentication_status'] = None
        if 'username' not in st.session_state:
            st.session_state['username'] = None
        if 'logout' not in st.session_state:
            st.session_state['logout'] = None
        if 'rol_login' not in st.session_state:
            st.session_state['rol_login'] = None
        if 'id_user' not in st.session_state:
            st.session_state['id_user'] = None
            

    def token_encode(self):
        """
        Returns
        -------
        str
            The JWT cookie for passwordless reauthentication.
        """
        return jwt.encode({'name':st.session_state['name'],
        'username':st.session_state['username'],
        'exp_date':self.exp_date,
        'rol_login':st.session_state['rol_login'],
        'id_user':st.session_state['id_user']}, self.key, algorithm='HS256')

    def token_decode(self):
        """
        Returns
        -------
        str
            The decoded JWT cookie for passwordless reauthentication.
        """
        try:
            return jwt.decode(self.token, self.key, algorithms=['HS256'])
        except:
            return False

    def exp_date(self):
        """
        Returns
        -------
        str
            The JWT cookie's expiry timestamp in Unix epoch.
        """
        return (datetime.utcnow() + timedelta(days=self.cookie_expiry_days)).timestamp()

    def check_pw(self):
        """
        Returns
        -------
        boolean
            The validation state for the input password by comparing it to the hashed password on disk.
        """
        return bcrypt.checkpw(self.password.encode(), self.passwords[self.index].encode())
    
    def check_user_db(self, email):
        cnx = mysql.connector.connect(
            user='root', 
            password='root',
            host='127.0.0.1',
            database='slsm_db'
        )
        
        cursor = cnx.cursor()
        sql = f"SELECT * FROM usuarios WHERE correo LIKE '%{email}%'"
        cursor.execute(sql)

        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        
        if not result:
            return False
        else:
            for data in result:
                if email == data[3]:
                    return True
            return False
        
    def add_user_db(self, name, last_name, email, rol, password):
        cnx = mysql.connector.connect(
            user='root', 
            password='root',
            host='127.0.0.1',
            database='slsm_db'
        )
        cursor = cnx.cursor()
        
        if rol == "Especialista":
            rol_id = 1
        
        if rol == "Paciente":
            rol_id = 2
            
        password_hash = Hasher([password]).generate()
        sql = "INSERT INTO usuarios (nombre, apellidos, correo, id_rol, contrasena, contrasena_hash) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (" ".join(name.upper().split()), " ".join(last_name.upper().split()), email, rol_id, password, password_hash[0])

        cursor.execute(sql, val)
        cnx.commit()
        
        cursor.close()
        cnx.close()
        
    def check_email_db(self, email):
        cnx = mysql.connector.connect(
            user='root', 
            password='root',
            host='127.0.0.1',
            database='slsm_db'
        )
        
        cursor = cnx.cursor()
        sql = f"SELECT * FROM usuarios WHERE correo LIKE '{email}'"
        cursor.execute(sql)

        result = cursor.fetchall()
        cursor.close()
        cnx.close()
        
        if not result:
            return False
        else:
            for data in result:
                if email == data[3]:
                    st.session_state['id_user'] = data[0]
                    self.names[0] = data[1]
                    self.usernames[0] = data[3]
                    self.passwords[0] = data[6]
                    st.session_state['rol_login'] = data[4]
                    return True
            return False
        
    def register_user(self):
        st.markdown(
            """
            <style>
                div[data-testid="stExpander"] div[role="button"] p {
                    font-size: 1.1rem;
                }
            </style>
            """, 
            unsafe_allow_html=True
        )
        
        # Agregar búsqueda y validación de usuario a como también para la contraseña que coincidan
        with st.expander("**Registrarse**"):
            with st.form("Register", clear_on_submit=True):
                col1_form, col2_form = st.columns(2)
                
                with col1_form:
                    name = st.text_input("Nombre")
                    email = st.text_input("Correo")
                
                with col2_form:
                    last_name = st.text_input("Apellidos")
                    rol = st.radio("Se está registrando como:", index=0, options=["Especialista", "Paciente"], horizontal=True)
                    
                password = st.text_input('Contraseña', type='password')
                repeat_password = st.text_input('Repetir contraseña', type='password')
                data_form = [name, last_name, email, password, repeat_password]
                
                if st.form_submit_button("Registrar"):
                    
                    # verifica que los campos esten llenos
                    if "" in data_form:
                        st.error("Por favor asegurese de llenar todos los campos", icon="⛔")
                    else:
                        
                        # verifica si las contraseñas son iguales
                        if password == repeat_password:
                            if not self.check_user_db(email):
                                
                                # registro de datos a la base de datos
                                self.add_user_db(name, last_name, email, rol, password)
                                with st.empty():
                                    st.success("Felicidades, el registro ha sido exítoso!", icon="✅")
                                    st.toast("Felicidades, el registro ha sido exítoso!", icon="✅")
                                    time.sleep(1)
                                
                            else:
                                with st.empty():
                                    st.error("Esta cuenta ya existe con el mismo correo", icon="⛔")
                                    st.toast("Esta cuenta ya existe con el mismo correo", icon="⛔")
                                    time.sleep(1)
                        else:
                            with st.empty():
                                st.error("Por favor asegurese de que la contraseña coincida", icon="⛔")
                                st.toast("Por favor asegurese de que la contraseña coincida", icon="⛔")
                                time.sleep(1)


    def form_login_main(self, form_name, location='main'):
        
        st.markdown(
            """
            <style>
                [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-top: -11%;
                    margin-bottom: -3%;
                    margin-left: auto;
                    margin-right: auto%;
                    width: 100%;
                }
                
                h1 {
                    text-align: center;
                    margin-top: -2%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        
        st.image(".\\images\\atencion-medica.png", width=120, use_column_width=False)
        st.title(":blue[Salud Latina Sin Medicina]")
        
        if location == 'main':
            login_form = st.form('Login')
        elif location == 'sidebar':
            login_form = st.sidebar.form('Login')
            
        login_form.subheader(form_name)
        self.username = login_form.text_input('Usuario (correo)')
        st.session_state['username'] = self.username
        self.password = login_form.text_input('Contraseña', type='password')
                
        if login_form.form_submit_button('Iniciar sesión'):
            self.index = None
            if self.check_email_db(self.username):
                for i in range(0, len(self.usernames)):
                    if self.usernames[i] == self.username:
                        self.index = i
            
            if self.index is not None:
                try:
                    if self.check_pw():
                        st.session_state['name'] = self.names[self.index]
                        self.exp_date = self.exp_date()
                        self.token = self.token_encode()
                        self.cookie_manager.set(self.cookie_name, self.token,
                        expires_at=datetime.now() + timedelta(days=self.cookie_expiry_days))
                        st.session_state['authentication_status'] = True
                    else:
                        st.session_state['authentication_status'] = False
                except Exception as e:
                    print(e)
            else:
                st.session_state['authentication_status'] = False
        
    def login(self, form_name, location='main'):
        """Create a new instance of "authenticate".
        Parameters
        ----------
        form_name: str
            The rendered name of the login form.
        location: str
            The location of the login form i.e. main or sidebar.
        Returns
        -------
        str
            Name of authenticated user.
        boolean
            The status of authentication, None: no credentials entered, False: incorrect credentials, True: correct credentials.
        str
            Username of authenticated user.
        """
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")

        if not st.session_state['authentication_status']:
            self.token = self.cookie_manager.get(self.cookie_name)
    
            if self.token is not None:
                self.token = self.token_decode()
                
                if self.token is not False:
                    if not st.session_state['logout']:
                        if self.token['exp_date'] > datetime.utcnow().timestamp():
                            if 'name' and 'username' in self.token:
                                st.session_state['name'] = self.token['name']
                                st.session_state['username'] = self.token['username']
                                st.session_state['authentication_status'] = True
                                st.session_state['rol_login'] = self.token['rol_login']
                                st.session_state['id_user'] = self.token['id_user']
            
            if st.session_state['authentication_status'] != True:
                self.form_login_main(form_name, location)

        return st.session_state['name'], st.session_state['authentication_status'], st.session_state['username'], st.session_state['rol_login']

    def logout(self, button_name, location='main'):
        """Creates a logout button.
        Parameters
        ----------
        button_name: str
            The rendered name of the logout button.
        location: str
            The location of the logout button i.e. main or sidebar.
        """
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")

        if location == 'main':
            if st.button(button_name):
                self.cookie_manager.delete(self.cookie_name)
                st.session_state['logout'] = True
                st.session_state['name'] = None
                st.session_state['username'] = None
                st.session_state['authentication_status'] = None
        elif location == 'sidebar':
            if st.sidebar.button(button_name):
                self.cookie_manager.delete(self.cookie_name)
                st.session_state['logout'] = True
                st.session_state['name'] = None
                st.session_state['username'] = None
                st.session_state['authentication_status'] = None

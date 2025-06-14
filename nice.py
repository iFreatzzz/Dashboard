import streamlit as st

st.set_page_config(page_title="Dashboard", layout="centered")

# Session state to track login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.rerun()  # Rerun to show dashboard
        else:
            st.error("Invalid username or password.")

def dashboard():
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; margin-top: 50px;">
            <img src="https://scontent-mnl1-2.xx.fbcdn.net/v/t1.6435-1/119482113_768530573720190_4576115466845870596_n.jpg?stp=dst-jpg_s200x200_tt6&_nc_cat=105&ccb=1-7&_nc_sid=e99d92&_nc_eui2=AeHw-02ZL6AFG3_x_tK_dTHTpXgHil78LRCleAeKXvwtEMAZ2BxI4n5L8OFF99vhx8XAHXVYm6GRQTBYz754F_0W&_nc_ohc=7Z9qenQkiE8Q7kNvwFProc4&_nc_oc=AdledxtPlYmUG_SZA8ikSP6n0vYEd2oerxhYYOYLu6IrHNxdtmkJsmxSufOsHr4_i9k&_nc_zt=24&_nc_ht=scontent-mnl1-2.xx&_nc_gid=7umq16yAdrGuFvEQYgBuaQ&oh=00_AfOqfjQd7mZiY0lPmEFZarbruG0-nt-1IahV1WvTchZbxA&oe=68748B86" style="border-radius: 50%; width: 120px; height: 120px; object-fit: cover;"/>
            <h2 style="margin-top: 20px;">Freatzzz</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.success("Welcome to your dashboard!")

if not st.session_state.logged_in:
    st.title("Basic Streamlit Web App")
    st.write("Welcome to your first Streamlit app!")
    login()
else:
    dashboard()

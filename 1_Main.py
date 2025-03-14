# Webpage mit python und streamlit
from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="KE Webspace", page_icon=":sun:", layout="wide")
st.markdown("""
    <style>
    .font {
        font-size:18px !important;
    }
    </style>
""", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# lottie_coding = load_lottieurl("https://lottie.host/2d8650da-67dd-4f88-b3da-27da9474e710/KVib0lIpf3.json") # background white
lottie_coding = load_lottieurl("https://lottie.host/33e14c93-4f6e-446d-8417-ed82b79e82fe/ykkTfkPb9S.json")   # bg black


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

img_kc_form = Image.open("images/kc_Feder_logo.jpg")

#st.title("Main Page")
st.sidebar.success("Seitenwahl")

# ---- Header section -----
with st.container():
    #st.subheader("Meine neue Webseite")
    left_column, right_column = st.columns(2)

    with left_column:
        st.write("#")
        st.title("Killinger Engineering")

    with right_column:
        st_lottie(lottie_coding, height=240, key="coding")

# --- what I am doing ---
with st.container():
    left_column, image_column = st.columns(2)                         # st.columns([2,1])
    with left_column:
        st.subheader("Unser Know-how:")
        st.markdown(        #'<p class="big-font">Hello World !!</p>', unsafe_allow_html=True
            """<p class="font">                                           
             &nbsp; - Datenbanken lokal und Cloud<br>
             &nbsp; - Mikro - Controller Applikationen <br>
             &nbsp; - Programmentwicklung Python u.a.<br>
             &nbsp; - Handy App Entwicklung <br>
             &nbsp; - Cloud Computing <br>  
             &nbsp; - 3D Druck Teile Konstruktion <br>   
             &nbsp; - Dokumentationen <br>   
             &nbsp; - Erstellung von Expertisen <br>    
            
        Wenn es interessant klingt,
        dann gehen Sie auf das
        Kontakt - Formular.   
            """, unsafe_allow_html=True)

    with image_column:
        st.write("##")
        st.image(img_kc_form)



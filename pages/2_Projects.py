from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

img_kc_form = Image.open("images/kc_Feder_logo.jpg")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/33e14c93-4f6e-446d-8417-ed82b79e82fe/ykkTfkPb9S.json")   # bg transparent

# ---- Header section -----
with st.container():
    #st.subheader("Meine neue Webseite")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("#")
        st.subheader("Killinger Engineering")
    with right_column:
        st_lottie(lottie_coding, height=120, key="coding")

st.title("Projekte")

with st.container():
    st.write("---")
    # st.write("Projektliste")
    st.write("#")
    image_column, text_column, link_column = st.columns(3)

    with image_column:
        st.write("#")
        st.image(img_kc_form)

    with text_column:
        st.subheader("Unsere aktuellen Projekte sind:")
        st.write(
            """
            &nbsp;- Sonnenfolger XL  <br>
            &nbsp;- DataBase Entwicklung (SQL & None-SQL)  <br>
            &nbsp;&nbsp;&nbsp; mit Python und Pyside6  <br>
            &nbsp;- 3D Konstruktionen für 3D Drucker - Teile u.a.  <br>
            &nbsp;- MicroController Anwendungen mit ESP32  <br>
            &nbsp;&nbsp;&nbsp; (WLAN und Bluetooth)  <br>
            &nbsp;- Handy Programmierung mit MIT Inventor <br>
            &nbsp;- Atemtaktgeber als Schlafhilfe <br>
            &nbsp;- Präzisionswischer   <br>
            &nbsp;- Farbwalzenreiniger  <br>
            &nbsp;- u.a. <br>
            """, unsafe_allow_html=True
        )

    with link_column:
        st.subheader("Links zu weiteren Infos:")
        st.write("[weitere Infos zum Sonnenfolger](https://youtu.be/RiG4PpyLAFk?si=PAg3KInr8MSIBIw0)")
        st.write("")
        st.write("[weitere Infos zur Konstruktion](https://www.killinger-consulting.de/film/Konstruktion&SCAD.mp4)")
        st.write("[Beispiel zur Wetterdaten - Erfassung mit µC und Cloud DB](https://weatherapp-6hfqptnhx4fvghbvqn2hne.streamlit.app)")
        st.write("")
        st.write("[weitere Infos zur APP - Entwicklung](https://www.killinger-consulting.de/film/APP-Entwicklung_MIT-Inventor.mp4)")
        st.write("")
        st.write("")
        st.write("[weitere Infos zum Wischer](https://www.killinger-consulting.de/film/bodenwischer.mp4)")
        st.write("[weitere Infos zum Reiniger](https://www.killinger-consulting.de/film/farbwalzenreiniger.mp4)")

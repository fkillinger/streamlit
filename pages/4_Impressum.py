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

lottie_coding = load_lottieurl("https://lottie.host/6935cd6a-56c4-4940-ad23-8ad9dd84ab0b/p6aKR2nqhu.json")   # Brief

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

st.title("Impressum")

with st.container():
    st.write("---")
    # st.write("Angaben gemäß § 5 TMG")
    st.write("##")
    text_column, image_column = st.columns(2)

    with text_column:
        st.subheader("Unsere Anschrift:")
        st.write("##")
        st.write(
            """
            Killinger Engineering <br>   
            Fritz Killinger <br>   
            Weitzkaut 24 <br>   
            63864 Glattbach <br>            
            Tel 06021 423653 <br>   
            info@killinger-consulting.de  <br>   
            """, unsafe_allow_html=True
        )

    with image_column:
        st.image(img_kc_form)
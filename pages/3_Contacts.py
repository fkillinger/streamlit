from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

lottie_coding_letter = load_lottieurl("https://lottie.host/6935cd6a-56c4-4940-ad23-8ad9dd84ab0b/p6aKR2nqhu.json")   # Brief

lottie_coding_main = load_lottieurl("https://lottie.host/33e14c93-4f6e-446d-8417-ed82b79e82fe/ykkTfkPb9S.json")   # animation

# ---- Header section -----
with st.container():
    #st.subheader("Meine neue Webseite")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.subheader("Killinger Engineering")
    with right_column:
        st_lottie(lottie_coding_main, height=120, key="coding1")

st.title("Kontakt")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

with st.container():
    st.write("---")
    st.write("Treten Sie in Kontakt mit uns")
    st.write("#")

    # contact_form von https://formsubmit.co
    contact_form = """

    <form action="https://formsubmit.co/fritz.killinger@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         Name <br> 
         <input type="text" name="name" placeholder "your name" required>
         Email - Adresse <br> 
         <input type="email" name="email" placeholder "your email" required>
         Nachricht  <br> 
         <textarea name="message" placeholder "your message here" required></textarea>
         <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_coding_letter, height=250, key="coding2")
        st.empty()



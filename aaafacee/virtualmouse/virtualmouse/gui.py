from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from face_recognition import face
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()
l = load_lottieurl("https://lottie.host/b9db6a62-5698-46fa-af6a-70b7e479567a/RIvUWpNjoM.json")
image_face = Image.open("C:\\Users\\AKSHAT\\OneDrive\\Desktop\\aaafacee\\virtualmouse\\virtualmouse\\images\\face.jpg")
image_vm =   Image.open("C:\\Users\\AKSHAT\\OneDrive\\Desktop\\aaafacee\\virtualmouse\\virtualmouse\\images\\vmouse.jpg")

st.set_page_config( page_title="msbte project", page_icon=":tada:",layout="wide")
#header
with st.container():
    st.subheader("hi there")
    st.write("our project")
#what i do
with st.container():
    st.write("___")
    lc, rc = st.columns(2)
    with lc:
        st.header("our project details")
        st.write("BLAH BLAH")
    with rc:
        st_lottie(l,height=300, key="virtual world")
#proects
with st.container():
    st.write("---")
    st.write("my project")
    st.write("##")
    image_col , text_col = st.columns((1,2))
    with image_col:
        st.image(image_face)
    with text_col:
        st.subheader("ABOUT OUR FACE RECOGNITION SYSTEM!")
        st.write("")
with st.container():
    image_col, text_col = st.columns((1, 2))
    with image_col:
        st.image(image_vm)
    with text_col:
        st.subheader("ABOUT OUR VIRTUAL MOUSE SYSTEM!")
        st.write("")
    if st.button("click here"):
        face()






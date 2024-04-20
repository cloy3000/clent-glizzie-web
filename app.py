
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Glizzie", page_icon="🤩", layout="wide") 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


lottie = load_lottieurl("https://lottie.host/51040f4f-2db2-4334-9f58-70071401beea/r94H4ZKrta.json")




with st.container():
    st.subheader("Hi, I am Clent") 
    st.title("A loving husband")
    st.write("I love you so much babycakes huhuhuhuhuu")

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("4 things why you should love me")
        st.write("##")
        st.write(
            """
            1. kissan tika perme 
            2. palangga nako imong mga iring 
            3. palangga tika kaayouuu
            4. ako nalng kase uwuuu 
            """
        )




with right_column:
    st_lottie(lottie, height="500", key="loving")
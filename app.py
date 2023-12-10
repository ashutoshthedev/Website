import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Developer", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

#---- LOAD ASSETS ----
lottie_coding=load_lottieurl("https://lottie.host/01a616fa-bd75-4d8c-84df-34f8357a0b9a/jyjjRowuKQ.json")
img_contact_form=Image.open("images/PavitraPrabhakar.jpg")
img_lottie_animation=Image.open("images/Punk.jpeg")

#---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Ashutosh :wave:")
    st.title("A Web Developer from Bharat")
    st.write("I am passionate about finding ways to use Python and Web Development to be more efficient and effective")
    st.write("[Learn More >](https://ashutoshthedev.github.io)")

#---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
                """
                    As a fervent website developer, my journey began with a profound fascination for coding, which I wholeheartedly embraced through the versatile language of Python. Through dedicated learning and exploration, I have honed my expertise in essential web technologies such as HTML, CSS, and JavaScript, forming the foundation for crafting websites that not only function efficiently but also boast a seamless user experience.""")
        st.write("[Github >](https://github.com/ashutoshthedev)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

#---- PROJECTS ----
with st.container():
    st.write("----")
    st.header("My Projects")
    st.write("##")
    image_column, text_column= st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Integrate Lottie Animations inside your Streamlit App")
        st.write(
            """
                Learn how to use Lottie Files in Streamlit!
                Animations make our web app more engaging and fun, and Lottie Files are the easiset way to do it
                In this tutorial, I'll show you exactly how to do it
                """
        )
        st.markdown("[Watch video...](https://youtu.be/VqgUkExPvLY?si=mwhW_cZxmhuRmQCH)")

with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("How To Add A Contact Form to Your Streamlit App")
        st.write(
            """
                Want to add a contact form to your Streamlit website?
                In this video, I am going to show you how to implement a contact form in your streamlit app using"""
        )
        st.markdown("[Watch video...](https://youtu.be/VqgUkExPvLY?si=tadfIm6UjJU0ouqD)")

#---- Contact ----
with st.container():
    st.write("---")
    st.header("Get in Touch with US!")
    st.write("##")

    contact_form="""
    <form action="https://formsubmit.co/anmolkt05@gmail.com" method="POST">
     <input type="hidden" name="_captch" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column, right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
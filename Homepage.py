import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image




st.set_page_config(page_title="Resume Website Instructions", layout="wide")


def load_lottieurl(url):
   r = requests.get(url)
   if r.status_code != 200:
       return None
   return r.json()




# Use local CSS
def local_css(file_name):
   with open(file_name) as f:
       st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)




local_css("style/style.css")


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_mu1asgg9.json")
img_1 = Image.open("images/img_1.jpg")
img_2 = Image.open("images/img_2.jpg")






# ---- HEADER SECTION ----
with st.container():
   st.title("Hi, I am Christian Ihekweazu")
   st.subheader("I'm a student majoring in Computer Science at Clemson University")



# ---- WHAT IS THIS ABOUT ----
with st.container():
   #st.write("---")
   left_column, right_column = st.columns(2)
   with left_column:
       st.header("What Exactly Is This For?")
       st.write("##")
       st.write(
           """
           This website serves as instructions for my resume website template that I have uploaded to my GitHub account.
           """
       )
   with right_column:
       st.image(img_1)
   st.write("---")



with st.container():
   st.write("---")
   st.header("Instructions")
   st.write("##")
   text_column, image_column = st.columns((1, 2)) 
   with text_column:
       st.subheader("Step 1")
       st.markdown('<div style="text-align: justify;"> <font size = "4"> Placeholder step </font> </div>', unsafe_allow_html=True)
   with image_column:
       st.image(img_1)
with st.container():
   image_column, text_column  = st.columns((2, 1)) #st.columns((2, 1))
   with text_column:
       st.subheader("Step 2")
       st.markdown('<div style="text-align: justify;"> <font size = "4"> Placeholder step </font> </div>', unsafe_allow_html=True)
   with image_column:
       st.image(img_2)
    



with st.container():
   st.markdown('<h1 style="text-align: center;">Contact Me</h1>', unsafe_allow_html=True)
   st.write("---")
   st.write("##")


   st.markdown('<div style="text-align: justify;"> <font size = "4"> - [My Email](christianihekweazu@gmail.com) </font> </div>', unsafe_allow_html=True)
   st.markdown('<div style="text-align: justify;"> <font size = "4"> - [My Linkedin](www.linkedin.com/in/christianihekweazu) </font> </div>', unsafe_allow_html=True)
   st.markdown('<div style="text-align: justify;"> <font size = "4"> - [My GitHub](https://github.com/CIhekweazu03) </font> </div>', unsafe_allow_html=True)
   st.write("---")  


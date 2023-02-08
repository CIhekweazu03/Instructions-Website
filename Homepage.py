import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image




st.set_page_config(page_title="Instructions for Resume Website", layout="wide")


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
welcome_img = Image.open("images/welcome.jpg")
img_1 = Image.open("images/img_1.jpg")
img_2 = Image.open("images/img_2.jpg")
img_3 = Image.open("images/img_3.jpg")
img_4 = Image.open("images/img_4.jpg")
img_5 = Image.open("images/img_5.jpg")
img_6 = Image.open("images/img_6.jpg")






# ---- HEADER SECTION ----
with st.container():
    st.title("Hi, I am Christian Ihekweazu")
    st.subheader("I'm a student majoring in Computer Science at Clemson University")



# ---- WHAT IS THIS ABOUT ----
with st.container():
    #st.write("---")
    left_column, right_column = st.columns(2)
    with right_column:
        st.header("What Exactly Is This For?")
        st.write("##")
        st.write(
            """
            This website serves as instructions for my resume website template that I have uploaded to my GitHub account.
            """
         )
    with left_column:
        st.image(welcome_img)
    st.write("---")



with st.container():
    st.write("---")
    st.header("Instructions")
    st.write("##")
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 1")
        st.write(
            """
            Download the most recent version of Python:
            \n- [This link will take you to the Python download page for your respective operating system](https://www.python.org/downloads/)
            """
        )
    with image_column:
        st.image(img_1)
    st.write("---")



with st.container():
    image_column, text_column  = st.columns((1, 1)) #st.columns((2, 1))
    with text_column:
        st.subheader("Step 2")
        st.write(
            """
            Open the Terminal or Command Line Interface on your computer and run the following commands:
            \n\tpip install requests
            \n\tpip install Streamlit
            \n\tpip install pillow
            \nThese commands will allow us to have allow us to have all of the respective packages needed to properly run the website locally.
            """
        )
    with image_column:
         st.image(img_2)
    st.write("---")
     

with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 3")
        st.write(
            """
            Download a code editor that works with Python
            \n- I personally use [Visual Studio Code](https://code.visualstudio.com/download), but there are a lot of other great free ones out there.
            """
        )
    with image_column:
        st.image(img_3)
    st.write("---")

with st.container():
    image_column, text_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 4")
        st.write(
            """
            [Download my template project folder from this link](https://GitHub.com/CIhekweazu03/Template-Website-Resume)
            \n- Click on the option to download zip.
            """
        )
    with image_column:
        st.image(img_4)
    st.write("---")

with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 5")
        st.write(
            """
            Use the respective open file option on your editor and go to the Homepage.py file.
            """
        )
    with image_column:
        st.image(img_5)
    st.write("---")

with st.container():
    image_column, text_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 6")
        st.write(
            """
            Edit name, personal information, education etc, to your respective information.
            \n- All the text on the page can be modified to better fit you and your experiences; just pay very close attention to everywhere that has PLACEHOLDER, because that definitely needs to be changed
            """
        )
    with image_column:
        st.image(img_6)
    st.write("---")


with st.container():
    st.markdown('<h1 style="text-align: center;">Contact Me</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("##")


   
    st.markdown('<a href="mailto:christianihekweazu@gmail.com">My Email</a>', unsafe_allow_html=True)
    st.write("[My Linkedin](http://www.linkedin.com/in/christianihekweazu)")
    st.markdown("[My GitHub](https://github.com/CIhekweazu03)")
    st.write("---")  


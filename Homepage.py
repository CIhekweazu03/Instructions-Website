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



welcome_img = Image.open("images/welcome.jpg")
img_1 = Image.open("images/img_1.jpg")
img_2 = Image.open("images/img_2.jpg")
img_3 = Image.open("images/img_3.jpg")
img_4 = Image.open("images/img_4.jpg")
img_5 = Image.open("images/img_5.jpg")
img_6 = Image.open("images/img_6.jpg")
img_7 = Image.open("images/img_7.jpg")
img_8 = Image.open("images/img_8.jpg")
img_9 = Image.open("images/img_9.jpg")
img_10 = Image.open("images/img_10.jpg")
img_11 = Image.open("images/img_11.jpg")
img_12 = Image.open("images/img_12.jpg")
img_13 = Image.open("images/img_13.jpg")
img_14 = Image.open("images/img_14.jpg")
img_15 = Image.open("images/img_15.jpg")
img_16 = Image.open("images/img_16.jpg")
img_17 = Image.open("images/img_17.jpg")






with st.container():
    st.title("Hi, I am Christian Ihekweazu")
    st.subheader("Instructions for Resume Website Template")




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
    image_column, text_column  = st.columns((1, 1))         
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
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 7")
        st.write(
            """
            Modify the “Basic Info,” “Organizations and Extracurriculars,” “Work Experiences”, “Technical Skills,” and “Contact Me” sections with your info.
            \nThis part is a little bit trickier, but in order to change the info you will have to modify the information between the beginning and closing tags.
            \n- For example, if you wanted to rename the Organizations and Extracurriculars you could modify everything after “<h3 style="text-align: center;">” and before “</h3>
            \n- Another example, if you wanted to modify the bullet points, you could freely change everything after “<div style="text-align: justify;"> <font size = "4">” and before “</font> </div>”
            \n- It may take some practice getting down, but if you make too big of a mistake, you can always re-download the respective files from my GitHub.
            """
        )
    with image_column:
        st.image(img_7)
    st.write("---")



with st.container():
    image_column, text_column  = st.columns((1, 1))         
    with text_column:
        st.subheader("Step 8")
        st.write(
            """
            (Optional) Go to the image folder and change the file named img_1.jpg with an image of your choice (could be a self-portrait, another welcome image, etc.); just make sure that the new file is also named img_1.jpg so that you don’t have to modify the Homepage.py file any more than is necessary.
            """
        )
    with image_column:
         st.image(img_8)
    st.write("---")

with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 9")
        st.write(
            """
            Make a GitHub Account and sign into that account.
            \n- [GitHub Sign Up](https://github.com/join)
            """
        )
    with image_column:
        st.image(img_9)
    st.write("---")



with st.container():
    image_column, text_column  = st.columns((1, 1))         
    with text_column:
        st.subheader("Step 10")
        st.write(
            """
            Make a GitHub Repository
            \n- After you make the repository, you wll see a screen like this.
            """
        )
    with image_column:
         st.image(img_10)
    st.write("---")
     
with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 11")
        st.write(
            """
            Click on the uploading an existing file option
            \n- Drag and drop the folder that you’ve been working on into this box
            """
        )
    with image_column:
        st.image(img_11)
    st.write("---")



with st.container():
    image_column, text_column  = st.columns((1, 1))         
    with text_column:
        st.subheader("Step 12")
        st.write(
            """
            Go to [Streamlit.io/cloud](https://Streamlit.io/cloud) and make an account
            \n- There should be a screen like this that will allow you to connect your new Streamlit account to GitHub.
            """
        )
    with image_column:
         st.image(img_12)
    st.write("---")

with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 13")
        st.write(
            """
            Click on the new app button.
            """
        )
    with image_column:
        st.image(img_13)
    st.write("---")



with st.container():
    image_column, text_column  = st.columns((1, 1))         
    with text_column:
        st.subheader("Step 14")
        st.write(
            """
            Click on the Paste Github URL button.
            """
        )
    with image_column:
         st.image(img_14)
    st.write("---")

with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 15")
        st.write(
            """
            Copy and paste the link to the Homepage.py file from your new repository into this text box.
            \n- Now you can click on Deploy!
            """
        )
    with image_column:
        st.image(img_15)
    st.write("---")



with st.container():
    image_column, text_column  = st.columns((1, 1))         
    with text_column:
        st.subheader("Step 16")
        st.write(
            """
            Back on the first page that you see when you log in you can see your app as well as these options when you click on the three dots beside it.
            """
        )
    with image_column:
         st.image(img_16)
    st.write("---")

with st.container():
    text_column, image_column = st.columns((1, 1)) 
    with text_column:
        st.subheader("Step 17")
        st.write(
            """
            (Optional) On this page you can rename the website URL to anything of your choice.
            """
        )
    with image_column:
        st.image(img_17)
    st.write("---")



with st.container():

    st.subheader("Wrap Up")
    st.markdown('<div style="text-align: center;"> <font size = "4"> That is all! If you are interested in learning more about Python, Streamlit, and GitHub, here are some great resources for you: </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"> <font size = "4"> <a href="https://docs.python.org/3/tutorial/">Python</a> </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"> <font size = "4"> <a href="https://docs.github.com/en/get-started/quickstart/hello-world">GitHub</a> </font> </div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;"> <font size = "4"> <a href="https://docs.streamlit.io/">Streamlit</a> </font> </div>', unsafe_allow_html=True)

    st.write("---")

with st.container():
    st.markdown('<h1 style="text-align: center;">Contact Me</h1>', unsafe_allow_html=True)
    st.write("---")
    st.write("##")


   
    st.markdown('<div style="text-align: center;"> <font size = "4"> If you have any questions about any particular step, please feel free to contact me on any of the platforms below, and I’ll try to get back to you as soon as possible. Thank you for checking out this tutorial! </font> </div>', unsafe_allow_html=True)
    st.markdown('<a href="mailto:christianihekweazu@gmail.com">My Email</a>', unsafe_allow_html=True)
    st.write("[My Linkedin](http://www.linkedin.com/in/christianihekweazu)")
    st.markdown("[My GitHub](https://github.com/CIhekweazu03)")
    st.write("---")  


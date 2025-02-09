import streamlit as st

# Set the page configuration with a dark theme
st.set_page_config(
    page_title="Dark Software",
    page_icon="dfc.png",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Dark Theme Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #1e1e1e;
            color: #f1f1f1;
        }
        .stButton>button {
            background-color: #ff0000;
            color: white;
            font-size: 20px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #c10000;
        }
        .stMarkdown {
            color: #b0b0b0;
        }
        .stTitle {
            color: #ff0000;
        }
        
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
pages = ["Home", "About Me"]
selected_page = st.sidebar.radio("Choose a page", pages)

# *Home Page* for Dark Software Download
if selected_page == "Home":
    st.title("Welcome to Dark Software")

    # Description
    st.write("""
    Dark Software is the ultimate tool for your system needs. 
    Download the latest version of Dark Software below!
    """)


    software_link = "https://drive.google.com/file/d/1qvk6a1DJhryevDD3dw2wGO5cXWdtpNJf/view?usp=drive_link"


    if st.button('Download Dark Software'):
        st.markdown(f'<a href="{software_link}" download>Click here to download</a>', unsafe_allow_html=True)

    st.write("Thank you for visiting! Let us know if you have any issues.")


elif selected_page == "About Me":
    st.title("About Me")

    st.write("""
    I am Amir Ali, the creator of Dark Software. 
    Dark Software is a powerful tool designed to make your life easier with efficient system management. 

    Feel free to reach out to me for any questions or support:
    """)

    # Contact Information
    st.subheader("Contact Me:")
    st.write("""
    - *Email*: [Click to Email to me](www.dujin7@gmail.com)
    - *WhatsApp*: [Click to message me on WhatsApp](https://wa.me/+93791838411)
    - *Company*: Dark Force Technologies
    """)

    st.write("Thanks for visiting the About Me page! Feel free to reach out if you need anything.")
hide='''
<style>
#MainMenu{visibility:hidden}
footer{visibility:hidden}
</style>
'''
st.markdown(hide,unsafe_allow_html=True)
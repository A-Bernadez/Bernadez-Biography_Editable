import streamlit as st
from PIL import Image
from datetime import datetime

# App Title
st.title("Editable Biography")

# Create two columns for layout
col1, col2 = st.columns([3, 1])
with col1:
    uploaded_photo = st.file_uploader("", type=["jpg", "jpeg", "png"])
    st.header("About Me")
    name = st.text_input("Full Name", "Angelica Marie B. Bernadez")
    bio = st.text_area("Short Bio About Yourself", 
                       "I am a first year student, taking the course of Bachelor of Science in Computer Engineering."
                        "I am interested on the things related to science and I want to expand my knowledge about it and also about the course I took.")
    contact = st.text_input("Email Address", "angelicabernadez322@gmail.com")
    st.markdown("Educational Attainment")
    Elementary = st.text_input("Elementary", "Honrado Elementary School")
    High_School = st.text_input("High School", "San Francisco National High School")
    College = st.text_input("College", "Surigao del Norte State University")
    
    location = st. text_input ("Permanent Address", "purok-3 Brgy.Honrado, San Francisco, Surigao del Norte")
    
    st.header ("Parental Information")
    father = st.text_input("Father's Full Name", "Noel Plaza Bernadez")
    mother = st.text_input("Motner's Maiden Name", "Wennylyn Aragon Bernal")
    contact_info = st.text_input ("Cellphone Number", "N/A")
    contact_info = st.text_input ("Cellphone Number", "09676484641")
    
with col2:
    if uploaded_photo is not None:
        image = Image.open(uploaded_photo)
        st.image(image, width=250)
    else:
        # Default Image when no photo is uploaded
        st.image("https://scontent.fmnl9-4.fna.fbcdn.net/v/t1.15752-9/464901712_978644247419353_7000827314453278790_n.jpg?stp=dst-jpg_s640x640&_nc_cat=105&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeFHYASTp0tfHLoIQlcUHWCXrwTpZhWB3emvBOlmFYHd6faFFVJ2pY9aEuU1cPIARvyk9b2evnsXL4XUt4A7_CP2&_nc_ohc=SWVz6Gu82EMQ7kNvgGAEdI5&_nc_zt=23&_nc_ht=scontent.fmnl9-4.fna&oh=03_Q7cD1QHpolL7nssBsIczTO-vE6FQFXdrclrmMbEkl_fzLyzq1Q&oe=676CAB55", width=500)
    ("")
    ("")
    ("")
    ("")
    ("")
    birthday = st.text_input("Birthday", "December 19, 2005")
    today = datetime.today()
    birth_date = datetime.strptime(birthday, "%B %d, %Y")
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    st.write(f"Age: {age}"); gender = st.selectbox("Gender", ["Female", "Male", "Other", "Prefer not to say"])
    contact = st.text_input("Contact Number", "09857880196")
    
    ("")
    st.text ("Year Graduated")
    year = st.text_input ("Elementary", "2017-2018")
    year = st.text_input ("High School","2023-2024")
    year = st.text_input ("College","2027-2028")
    ("")
    ("")
    ("")
    ("")
    ("")
    ("")
    birthday = st.text_input("Father's Birthday", "May 4, 1970")
    birthday = st.text_input("Mother'sBirthday", "May 27, 1981")
    occupation = st.text_input ("Father's Occupation", "Tricycle Driver")
    occupation = st.text_input ("Mother's Occupation", "Housewife")
    
st.header ("Workshop/Seminar Attended")
seminar = st.text_area("", 
                        "DOST: 3 DAYS ARDUINO WORKSHOP")

st.header ("HOBBIES/ SKILLS")

hobbies = st.text_area ("Hobbies/Skills", 
                        "I love to Badminton and I also love to watch korean and thrill movies")    
    
import streamlit as st
from streamlit_option_menu import option_menu

#emojis at = webfx/emoji-cheat-sheet
st.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")


#navbar
selected = option_menu(None, ["Home", "Model", "Dictionary", 'About Us'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")



#load assets
video1 = open("Video_call.mp4", "rb") 

st.write("##")


#header
with st.container():
    st.write("Step into the world of Sign Language, where every sign tells a story and every gesture bridges worlds.:wave:")
    st.title("SignSpeak: Where silent gestures find their powerful voice.")
    st.subheader("Explore our project to witness the transformative impact of bridging communication divides and fostering inclusivity.")
    st.write("Join us as we embark on this enlightening journey together! [learn more >](https://google.com)")

#what I do//// maybe add a video
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What we do")
        st.write("##")
        st.subheader(
    """
    Hello, I'm [Your Name]. Welcome to signSpeak!
    
    - With signSpeak, we've created a platform that understands your signs, translates them into written text, and even converts them into spoken words.
    - Record your signs using a camera or webcam, and our technology will detect and translate them into your preferred language.
    - You can also convert the translated text into spoken words, making it easier for everyone to understand.
    
    Thank you for joining us on this journey. Feel free to reach out if you have any questions or feedback.

    """
        )
        
    with right_column:
        st.video(video1) #displaying the video
        
        
            
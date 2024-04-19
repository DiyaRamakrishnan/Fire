import streamlit as st

def generate_css(primary_color, secondary_background_color):
    css = f"""
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #ffffff;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100vh;
            justify-content: center;
        }}
        .title {{
            font-size: 2rem;
            color: {primary_color};
            margin-bottom: 10px;
        }}
        .info-content {{
            width: 80%;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: {secondary_background_color};
            margin-bottom: 20px;
        }}
    </style>
    """
    return css

def show_info_page(primary_color, secondary_background_color):
    css = generate_css(primary_color, secondary_background_color)
    st.markdown(css, unsafe_allow_html=True)

    st.title('Info Page')
    st.markdown('<div>', unsafe_allow_html=True)
    st.header('About Project')
    st.write("""
    We create a reliable motion tracking device and a code that recognizes user activity. Our website allows users to input collected data in order to detect firefighters' positions. This website also serves as a space for customer support, where people can upload their own information easily!
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    

    st.header('About Riley Mattheis and Sydney Leslie')

    st.subheader('Background')
    st.write("""
    We are both upperclassmen at Nouvel Catholic Central. We have been able to work on this research due to the fund graciously provided the AH Nickless foundation. We enjoy participating in extracurricular activities that involve science. One of our favorite activities that we do together is Science Olympiads. 
    """)
    
    st.subheader('Inspiration')
    st.write("""
    The inspiration came from Riley's father who has been a Firefighter and EMT for over 30 years. Ever since Riley was a little girl she's always worried about where her father goes when he enters a burning building. By creating a tracking device and a website, we can now track where he is. We hope to extend this benefit to many others through our device and acessible website!
    """)
    
    st.subheader('Mission')
    st.write("""
    The purpose of this website is to allow customers to upload their image and detect what motion is happening, as a firefighter is in a building. The second purpose of this website is to provide customer support to others that would like to use this website as well.
    """)
    
    st.subheader('Contact')
    st.write("""
    Feel free to contact us! 
    mattheisriley@gmail.com   
    misscewagner@gmail.com
    sleslie@student.nouvelcatholic.org
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
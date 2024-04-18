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

    st.markdown('<div class="info-content">', unsafe_allow_html=True)
    st.header('About Project')
    st.write("""
    Write about your project
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-content">', unsafe_allow_html=True)
    st.header('About Project')
    st.write("""
    Write about your project
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="info-content">', unsafe_allow_html=True)
    st.header('About FIRST NAME LAST NAME')

    st.subheader('Background')
    st.write("""
    Write about yourself! Your hobbies, who you are, etc.
    """)
    
    st.subheader('Inspiration')
    st.write("""
    Why did you want to do this project?
    """)
    
    st.subheader('Mission')
    st.write("""
    Purpose of this website?
    """)
    
    st.subheader('Contact')
    st.write("""
    Write your contact information!
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
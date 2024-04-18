import os
import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from info_page import show_info_page

class_labels = ['DownStairs', 'UpStairs', 'Walking', 'Standing', 'DropTest']

script_dir = os.path.dirname(os.path.abspath(__file__))
model_file_path = os.path.join(script_dir, 'models', 'model.h5')
model = load_model(model_file_path)

img_length = 50
img_width = 50

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
        .input-side, .output-side {{
            width: 80%;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}
        .input-side {{
            background-color: coral;
        }}
        .output-side {{
            background-color: #fff;
        }}
        .title {{
            font-size: 2rem;
            color: #ffffff;
            margin-bottom: 10px;
        }}
        .button {{
            background-color: coral;
            color: #ffffff;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        .button:hover {{
            background-color: #ff7f50;
        }}
        .prediction {{
            font-size: 1.5rem;
            margin-bottom: 10px;
        }}
        .probability {{
            font-size: 1.5rem;
            margin-bottom: 20px;
        }}
        .output-image {{
            max-width: 400px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }}
    </style>
    """
    return css

def process_image(img):
   img = cv2.resize(img, (img_length, img_width))
   input_data = np.array([img], dtype=np.float32) / 255.0
   predictions = model.predict(input_data)
   predicted_class_index = np.argmax(predictions[0])
   predicted_class = class_labels[predicted_class_index]
   return predicted_class, predictions[0][predicted_class_index]


def main():

   primary_color = st.config.get_option("theme.primaryColor")
   secondary_background_color = st.config.get_option("theme.secondaryBackgroundColor")


   css = generate_css(primary_color, secondary_background_color)
   st.markdown(css, unsafe_allow_html=True)


   page = st.sidebar.selectbox("Go to", ["YOURWEBSITENAME", "Info Page", "Comments", "QR Code"])


   if page == "YOURWEBSITENAME":
       st.title('YOURWEBSITENAME')
       st.write("""
       CAPTION ON FRONT PAGE W/ MODEL
       """)


       
       st.markdown('<div class="input-side">', unsafe_allow_html=True)
       st.markdown('<h2 class="title" style="color: #4786a5;">Upload Image</h2>', unsafe_allow_html=True)  # Mellow blue color
       uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
       st.markdown('</div>', unsafe_allow_html=True)


      
       st.markdown('<div class="output-side">', unsafe_allow_html=True)
       if uploaded_file is not None:
           st.markdown('<h2 class="title" style="color: #4786a5;">Detection Result</h2>', unsafe_allow_html=True)  
           
           if uploaded_file.type.startswith('image'):
               img = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
               img = cv2.imdecode(img, cv2.IMREAD_COLOR)
               if st.button('Detect Image'):  
                   result, probability = process_image(img)
                   
                   st.markdown(f'<p class="prediction">Predicted Class: {result}</p>', unsafe_allow_html=True)
                   st.markdown(f'<p class="probability">Probability: {probability}</p>', unsafe_allow_html=True)
           elif uploaded_file.type.startswith('video'):
               video_path = os.path.join(script_dir, 'temp_video.mp4')  
               with open(video_path, 'wb') as f:
                   f.write(uploaded_file.read())
               frame_number = st.number_input("Frame Number", value=0, step=1)
               selected_frame = process_video(video_path, frame_number)
               st.image(cv2.cvtColor(selected_frame, cv2.COLOR_BGR2RGB), caption='Selected Frame', channels='RGB', width=500, output_format='JPEG')
               st.markdown('<h2 class="title" style="color: #4786a5;">Detection Result</h2>', unsafe_allow_html=True)  # Mellow blue color
    
               result, probability = process_image(selected_frame)
               st.markdown(f'<p class="prediction">Predicted Class: {result}</p>', unsafe_allow_html=True)
               st.markdown(f'<p class="probability">Probability: {probability}</p>', unsafe_allow_html=True)
              
   elif page == "Info Page":
       show_info_page(primary_color, secondary_background_color)  


   elif page == "QR Code":
       st.title("QR Code")
       qr_image_path = "YOURqr.png"
       st.image(qr_image_path, caption="Please use the QR code to send this app to people you know!", width=500)


   elif page == "Comments":
       st.title('Comments')
       st.write("""
       Leave your comments and feedback below:
       """)
       
       user_name = st.text_input("Your Name", max_chars=50)
       comment = st.text_area("Your Comment", max_chars=200)
       if st.button("Submit"):
           if len(comment.strip()) > 0:
               
               with open("comments.txt", "a") as file:
                   file.write(f"{user_name}: {comment}\n")
               st.success("Comment submitted successfully!")
               comment = ""
           else:
               st.warning("Please enter a comment before submitting.")
      
       st.write("### Comments:")
       comments = []
       with open("comments.txt", "r") as file:
           comments = file.readlines()
       if comments:
           for comment_text in comments:
               
               parts = comment_text.split(":", 1)
               if len(parts) == 2:
                   name, comment_msg = parts
                   
                   st.write(f"**{name.strip()}**")
                   st.write(f"{comment_msg.strip()}")
               else:
                   st.write(comment_text.strip())


       
       if st.button("Delete All Comments"):
           
           with open("comments.txt", "w") as file:
               file.truncate(0)
           st.success("All comments deleted successfully!")
           
           st.experimental_rerun()


if __name__ == "__main__":
   main()


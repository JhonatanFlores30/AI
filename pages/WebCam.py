import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd
import cv2
import time

st.title("Página de la Webcam")
data = pd.read_csv("data2.csv")

#Placeholder para reproducir la camara
frame_placeholder = st.empty()

# Inicia la camara
cap = cv2.VideoCapture(0)

# Loop para tomar frames de la camara y desplegarlos
if cap.isOpened():
    for _ in range(100):  # Limite de 100 frames para terminar el loop
        ret, frame = cap.read()
        if not ret:
            st.write("Error: No frame available.")
            break
        
        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_pil = Image.fromarray(frame_rgb)
        
        # Display the frame
        frame_placeholder.image(frame_pil, caption="Analizando emociones")
        
        # Pause briefly to allow other elements to render
        time.sleep(0.1)
else:
    st.write("Error: Unable to open webcam.")

# Release the webcam
cap.release()

# Process and display the bar chart
avg_income_by_profession = data.groupby('Profession')['Income'].mean().reset_index()

# Create bar plot
fig = px.bar(
    avg_income_by_profession,
    x='Profession',
    y='Income',
    title='Porcentaje de emocion encontrada',
    labels={'Income': 'Average Income', 'Profession': 'Profession'},
    color='Income',
    color_continuous_scale='Spectral'
)

# Display plot in Streamlit
st.title("Emociones encontradas")
st.plotly_chart(fig)

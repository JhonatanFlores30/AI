import streamlit as st
from PIL import Image
import plotly.express as px
import pandas as pd


st.set_page_config(layout="wide")
st.title("IMAGEN")
data=pd.read_csv("data2.csv")

@st.cache_data
def cargar_imagen(image_file):
    img=Image.open(image_file)
    return img


archivo_imagen=st.file_uploader("Subir Imagenes",type=["png","jpg","jpeg"])
if archivo_imagen is not None:
    st.image(archivo_imagen,width=250)

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

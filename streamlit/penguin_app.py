import streamlit as st
from streamlit_lottie import st_lottie

import plotly.express as px
import pandas as pd
import altair as alt
import requests

# animated penguin


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_penguin = load_lottieurl(
    "https://lottie.host/1293dba5-8288-465a-955c-355feba68a6d/n4jxaVVHZZ.json"
)

header_col1, header_col2 = st.columns([1, 5])
with header_col1:
    st_lottie(lottie_penguin)

with header_col2:
    st.title("This is a :penguin: app")


# Create sidebar
option = st.sidebar.radio("Choose between Image and Video", ["Image", "Video"])

# File upload
file = st.file_uploader("Upload a file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Basic Visualizations")

    # # Visualize data using Altair
    # st.subheader("Altair Chart")
    # # Example Altair chart using Stephens code
    # chart = alt.Chart(df).mark_circle().encode(
    #     x='bill_length_mm',
    #     y='bill_depth_mm',
    #     color='species',
    #     size='body_mass_g',
    #     tooltip=['species', 'bill_length_mm', 'bill_depth_mm', 'body_mass_g']
    # ).interactive()

    # st.altair_chart(chart, use_container_width=True)
    fig = px.scatter(
        df,
        x="bill_length_mm",
        y="bill_depth_mm",
        color="island"
    )
    st.plotly_chart(fig)

# Display image or video based on state of option
if option == "Image":
    st.subheader("Here is a penguin image")
    st.image("https://cdn.vox-cdn.com/thumbor/xYSUaNbrtoz-HUrW5CIStGurgWk=/0x0:4987x3740/1200x800/filters:focal(0x0:4987x3740)/cdn.vox-cdn.com/uploads/chorus_image/image/45503430/453801468.0.0.jpg")
elif option == "Video":
    st.subheader("Here is a penguin video")
    st.video("https://www.youtube.com/watch?v=wCvWEY2h3o8&ab_channel=BBCEarth")

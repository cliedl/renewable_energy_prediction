import streamlit as st

st.set_page_config(
    page_title="Cat app",
    page_icon=":cat:",
    layout="centered",  # Can be "wide" or "centered"
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
)


st.header("We have exactly what your day was missing")


def refresh_image():
    st.experimental_rerun()


col1, col2 = st.columns(2)
with col1:
    st.subheader("Here is a random cat image")
    st.image("https://cataas.com/cat")

with col2:
    st.subheader("Here is a random cat gif")
    st.markdown('<img src="https://cataas.com/cat/gif"/>',
                unsafe_allow_html=True
                )

st.subheader(
    "For your convenience, we have curated the best cat video known to humanity"
)
st.video("https://www.youtube.com/watch?v=y0sF5xhGreA&ab_channel=ThePetCollective")

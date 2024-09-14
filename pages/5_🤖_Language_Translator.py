

import streamlit as st


def text_to_speech() -> None:
    st.set_page_config(page_title="Text to Speech", page_icon="📹", layout="wide")
    st.markdown("# Text to Speech Demo")
    st.sidebar.header("Text to Speech Demo")
    st.write(
        """This app shows how you can use Streamlit to build cool animations.
    It displays an animated fractal based on the the Julia Set. Use the slider
    to tune different parameters."""
)

text_to_speech()

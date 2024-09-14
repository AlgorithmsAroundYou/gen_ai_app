

import streamlit as st


def text_to_speech() -> None:
    st.set_page_config(page_title="Mail Writing Assistance", page_icon="📹", layout="wide")
    st.markdown("# Mail Writing Assistance Demo")
    st.sidebar.header("Mail Writing Assistance")
    st.write(
        """This app shows how you can use Streamlit to build cool animations.
    It displays an animated fractal based on the the Julia Set. Use the slider
    to tune different parameters.""")

    Path = "Hello"
    st.code(Path, language="python")

text_to_speech()



import streamlit as st


def talk_to_document() -> None:
    st.set_page_config(page_title="Ask Document", page_icon="📹", layout="wide")
    st.markdown("# Ask Document Demo")
    st.sidebar.header("Ask Document Demo")
    st.write(
        """This app shows how you can use Streamlit to build cool animations.
    It displays an animated fractal based on the the Julia Set. Use the slider
    to tune different parameters."""
)

talk_to_document()

# Author: Sai Kumar Kodati
#

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Gen AI App",
        page_icon="🏚",
    )

    st.balloons()

    st.info('This is a purely informational message', icon="ℹ️")

    st.write("# Welcome to GenAI App! 👋")

    st.sidebar.success("Select a demo above.")

    st.snow()

    st.markdown(
        """
        GenAI App is an open-source application built specifically for
        Machine Learning and Data Science demo projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what GenAI App can do!
        ### Want to learn more?
        - 
        ### See more complex demos
        - 
    """
    )


if __name__ == "__main__":
    run()
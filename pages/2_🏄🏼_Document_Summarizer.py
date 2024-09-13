

import streamlit as st

def document_summarizer() -> None:
    st.set_page_config(page_title="Document Summarizer Demo", page_icon="📹")
    st.markdown("# Document Summarizer Demo")
    st.sidebar.header("Document Summarizer Demo")
    st.write(
        """This App Helps you to summarize your large document.""")

    uploaded_files = st.file_uploader(
        "Choose files", accept_multiple_files=True
    )
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

document_summarizer()
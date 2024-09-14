
import streamlit as st
from streamlit_player import st_player
import os
from src.video_info import GetVideo
from src.model import Model
from src.prompt import Prompt
from src.copy_module_edit import ModuleEditor
from dotenv import load_dotenv
from st_copy_to_clipboard import st_copy_to_clipboard


class AIVideoSummarizer:
    def __init__(self):
        self.youtube_url = None
        self.video_id = None
        self.video_title = None
        self.video_transcript = None
        self.video_transcript_time = None
        self.summary = None
        self.time_stamps = None
        self.transcript = None
        self.model_name = None
        self.col1 = None
        self.col2 = None
        self.col3 = None
        self.model_env_checker = []
        load_dotenv()

    def get_youtube_info(self):

        testVideo = "https://www.youtube.com/watch?v=DBW9aBLBFh4"
        self.youtube_url = st.text_input("Enter YouTube Video Link", testVideo)

        if self.youtube_url:
            self.video_id = GetVideo.Id(self.youtube_url)
            if self.video_id is None:
                st.write("**Error**")
                st.image("https://i.imgur.com/KWFtgxB.png", use_column_width=True)
                st.stop()
            self.video_title = GetVideo.title(self.youtube_url)
            st.write(f"**{self.video_title}**")
            st_player(self.youtube_url)

    def generate_summary(self):
        if st.button(":rainbow[**Get Summary**]"):
            self.video_transcript = GetVideo.transcript(self.youtube_url)
            self.summary = Model.google_gemini(transcript=self.video_transcript, prompt=Prompt.prompt1())
            print(self.summary)
            result = GetVideo.transcript_time(self.summary, video_url=self.youtube_url)
            st.markdown("## Summary:")
            st.markdown(result, unsafe_allow_html=True)
            

    def run(self):
        st.set_page_config(page_title="AI Video Summarizer", page_icon="📹", layout="wide")
        st.title("AI Video Summarizer")
        editor = ModuleEditor('st_copy_to_clipboard')
        editor.modify_frontend_files()

        self.get_youtube_info()
        self.generate_summary()

if __name__ == "__main__":
    app = AIVideoSummarizer()
    app.run()

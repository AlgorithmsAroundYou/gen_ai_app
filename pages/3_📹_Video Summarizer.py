# import streamlit as st
# from streamlit_player import st_player
# import pyttsx3
# from youtube_transcript_api import YouTubeTranscriptApi
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.embeddings import HuggingFaceInstructEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_community.document_loaders import TextLoader
# from langchain.chains import RetrievalQA
# from langchain_google_genai import GoogleGenerativeAI
# import pickle
# import time
# import os
# import multiprocessing
# import pyttsx3
# import keyboard

# file_path = "faiss_store_openai.pkl"
# status_text = st.empty()
# llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key="AIzaSyAuYa6MTdkeX2uFTA4Y_fhZW9lTt33PMqA", temperature=0.5)

# def text_to_ai(data, language_code): 
#     f = open("temp.txt", "w")
#     f.write(data)
#     f.close()

#     loader = TextLoader("temp.txt")
#     st.sidebar.text("loading data .......")
#     data = loader.load()

#     text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
#     docs = text_splitter.split_documents(data)
#     print("chunks size------------------------", len(data))
       
#     instructor_embedding = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
#     embedding = instructor_embedding
#     verctorstore_openai = FAISS.from_documents(docs, embedding)
#     st.sidebar.text('embedding vector started .......')
#     time.sleep(2)

#     with open(file_path, "wb") as f:
#         pickle.dump(verctorstore_openai, f)
        
#     st.sidebar.text('embedding vector done .......')

# def get_transcript(youtube_url):
#     video_id = youtube_url.split("v=")[-1]
#     transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

#     try:
#         transcript = transcript_list.find_manually_created_transcript()
#         language_code = transcript.language_code
#     except:
#         try:
#             generated_transcripts = [trans for trans in transcript_list if trans.is_generated]
#             transcript = generated_transcripts[0]
#             language_code = transcript.language_code
#         except:
#             raise Exception("No suitable transcript found.")

#     full_transcript = " ".join([part['text'] for part in transcript.fetch()])
#     return full_transcript, language_code

# def summarize_with_langchain(language_code):
#     print("This is the language code: ", language_code)
#     prompt = f'''Your task: Condense a video transcript into a captivating and informative 250-word summary that highlights key points and engages viewers.

# Guidelines:
#     Focus on essential information: Prioritize the video's core messages, condensing them into point-wise sections.
#     Maintain clarity and conciseness: Craft your summary using accessible language, ensuring it's easily understood by a broad audience.
#     Capture the essence of the video: Go beyond mere listings. Integrate key insights and interesting aspects to create a narrative that draws readers in.
#     Word count: Aim for a maximum of 250 words.

# Input:
#     The provided video transcript will be your content source which is {language_code}.

# Example (for illustration purposes only):
#     Setting the Stage: Briefly introduce the video's topic and context.
#     Key Points:
#         Point A: Describe the first crucial aspect with clarity and depth. (timestamp of that point)
#         Point B: Elaborate on a second significant point. (timestamp of that point)
#         (Continue listing and describing key points) (with timestamp for each point)
#     Conclusions: Summarize the video's main takeaways, leaving readers with a clear understanding and potential interest in learning more.

# Additional Tips:
#     Tailor the tone: Adjust your language to resonate with the video's intended audience and overall style.
#     Weave in storytelling elements: Employ vivid descriptions and engaging transitions to make the summary more memorable.
#     Proofread carefully: Ensure your final summary is free of grammatical errors and typos.

# By following these guidelines, you can effectively transform video transcripts into captivating and informative summaries, drawing in readers and conveying the video's essence effectively."""
# # '''
# #     prompt = f'''Summarize the text in very detail in {language_code}.

# # Add a TITLE to the summary in {language_code}.
# # Include an INTRODUCTION,
# # Most important BULLET POINTS with a corresponding timestamp at the end of each bullet point (in the format mm:ss) indicating the part of the video being summarized,
# # Make sure to include the timestamp for every bullet point.
# # End with a CONCLUSION in {language_code}.'''

#     try:
#         if os.path.exists(file_path):
#             with open(file_path, "rb") as f:
#                 verctorstore = pickle.load(f)
#                 chain = RetrievalQA.from_chain_type(
#                         llm=llm,
#                         chain_type="stuff",
#                         retriever=verctorstore.as_retriever(),
#                         input_key="query",
#                         return_source_documents=True
#                         )
#                 result = chain.invoke(prompt)
#                 return result
#     except Exception as e:
#         status_text.write(str(e))

# def text_to_speech(summary):
#     print("In the function", summary)
#     engine = pyttsx3.init()

#     rate = engine.getProperty('rate')
#     engine.setProperty('rate', 180)

#     volume = engine.getProperty('volume')
#     engine.setProperty('volume', 1.0)

#     engine.setProperty('pitch', 0.8)
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)

#     engine.say("Hello World!")
#     engine.say('My current speaking rate is ' + str(rate))
#     engine.say(summary)

#     engine.runAndWait()
#     engine.stop()

# def format_summary_with_links(summary, video_url):
#     lines = summary.splitlines()
#     formatted_lines = []
    
#     for line in lines:
#         if "(" in line and ")" in line:  # Detect lines with timestamps
#             text, timestamp = line.rsplit("(", 1)
#             # print(text, timestamp)
#             timestamp = timestamp.rstrip(")")
#             # print(timestamp)
#             minutes, seconds = map(int, timestamp.split(":"))
#             time_in_seconds = minutes * 60 + seconds
#             timestamp_url = f"{video_url}&t={time_in_seconds}"
#             # print(timestamp_url)
#             clickable_timestamp = f"[{timestamp}]({timestamp_url})"
#             # print(clickable_timestamp)
#             formatted_line = f"{text}({clickable_timestamp})"
#             # print(formatted_line)
#         else:
#             formatted_line = line
#         formatted_lines.append(formatted_line)
#         # print(formatted_lines)
    
#     return "\n".join(formatted_lines)


# def main():
#     if 'summary' not in st.session_state:
#         st.session_state.summary = 0
#     testVideo = ""
#     status_text.title('HPE Video Summarizer Demo')
#     link = st.sidebar.text_input('Enter video you want to summarize:', testVideo)
#     language_code = 0 
#     st_player(link)

#     if st.sidebar.button('Start Load'):
#         if link:
#             try:       
#                 progress = st.progress(0)
#                 st.sidebar.text('Loading the transcript...')
#                 progress.progress(25)

#                 transcript, language_code = get_transcript(link)
#                 print(transcript)
#                 text_to_ai(transcript, language_code)

#                 st.sidebar.text(f'AI generated summary, click on Summarize button to View')
#                 progress.progress(75)
#                 progress.progress(100)
#             except Exception as e:
#                 st.sidebar.write(str(e))
#         else:
#             st.sidebar.write('Please enter a valid YouTube link.')

#     if st.button('Summarize'):
#         result = summarize_with_langchain(language_code)
#         st.session_state.summary = result["result"]
#         formatted_summary = format_summary_with_links(st.session_state.summary, link)
#         st.markdown(formatted_summary, unsafe_allow_html=True)
        
#     if st.button('Speech'):
#         if st.session_state.summary != 0:
#             # print(st.session_state.summary)
#             # text_to_speech(st.session_state.summary)
#             p = multiprocessing.Process(target=text_to_speech, args=(st.session_state.summary,))
#             p.start()
#             while p.is_alive():
#                 if keyboard.is_pressed('q'):
#                     p.terminate()
#                 else:
#                     continue
#             p.join()
#         else:
#             st.write("Please summarize the video first.")

# if __name__ == "__main__":
#     main()



import streamlit as st
from streamlit_player import st_player
import os
from src.video_info import GetVideo
from src.model import Model
from src.prompt import Prompt
from src.misc import Misc
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
        self.youtube_url = st.text_input("Enter YouTube Video Link")

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
        st.set_page_config(page_title="AI Video Summarizer", page_icon="chart_with_upwards_trend", layout="wide")
        st.title("AI Video Summarizer")
        editor = ModuleEditor('st_copy_to_clipboard')
        editor.modify_frontend_files()
        
        
        self.col1, self.col2 = st.columns(2)

        with self.col1:
            self.get_youtube_info()

        with self.col2:
            self.generate_summary()

        

if __name__ == "__main__":
    app = AIVideoSummarizer()
    app.run()

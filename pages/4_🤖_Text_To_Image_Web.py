
import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk
import streamlit as st

import torch
from torch import autocast
#from diffusers import StableDiffusionPipeline
# !pip install diffusers transformers
from diffusers import DiffusionPipeline

st.title("Stable Bud")
prompt = st.text_input("Enter Prompt for Image Generation")

print("------------------------------------------------------", torch.cuda.is_available())

model_id = "CompVis/ldm-text2im-large-256"
device = "cuda"
# load model and scheduler
ldm = DiffusionPipeline.from_pretrained(model_id)


if st.button(":rainbow[**Get Image**]"):
    with autocast(device):
        images = ldm([prompt], guidance_scale=8.5).images
        # save images
        for idx, image in enumerate(images):
            image.save(f"generatedimage.png")

    st.image(image)
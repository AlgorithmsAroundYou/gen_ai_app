
import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk
from auth_token import AuthToken 

import torch
from torch import autocast
from diffusers import StableDiffusionPipeline


#Create the app
app = tk.Tk()
app.geometry("532x622")
app.title("Stable Bud")
ctk.set_appearance_mode("dark")

prompt = ctk.CTkEntry(master=app,
                               placeholder_text="Enter Prompt",
                               width=490, height=40,
                               border_width=2, corner_radius=10,
                               text_color="black", fg_color="white")
prompt.place(x=250, y=20, anchor=tk.CENTER)

lmain = ctk.CTkLabel(master=app, height=512, width=512)
lmain.place(x=10, y=110)

print("------------------------------------------------------", torch.cuda.is_available())

modelid = "CompVis/stable-diffusion-v1-4"
device = "cuda"
pipe = StableDiffusionPipeline.from_pretrained(modelid, revision="fp16", torch_dtype=torch.float16, use_auth_token=AuthToken)
pipe.to(device)

def generate():
    with autocast(device):
        image = pipe(prompt.get(), guidance_scale=8.5)["sample"][0]
    
    img = ImageTk.PhotoImage(image)
    img.save('generatedimage.png')
    lmain.configure(image=img)

trigger = ctk.CTkButton(master=app, command=generate)
trigger.configure(text = "Generate")
trigger.place(x=206, y=60)

app.mainloop()

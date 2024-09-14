
import tkinter as tk
import customtkinter as ctk 

from PIL import ImageTk
from auth_token import AuthToken 

import torch
from torch import autocast
#from diffusers import StableDiffusionPipeline
# !pip install diffusers transformers
from diffusers import DiffusionPipeline


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

model_id = "CompVis/ldm-text2im-large-256"
device = "cuda"
# load model and scheduler
ldm = DiffusionPipeline.from_pretrained(model_id)

def generate():
    with autocast(device):
        images = ldm([prompt.get()], guidance_scale=8.5).images
        # save images
        for idx, image in enumerate(images):
            image.save(f"squirrel-{idx}.png")

    img = ImageTk.PhotoImage(image)
    #img.save('generatedimage.png')  
    lmain.configure(image=img)

trigger = ctk.CTkButton(master=app, command=generate)
trigger.configure(text = "Generate")
trigger.place(x=206, y=60)

app.mainloop()

from django.db import models
# import gradio as gr
# # from openai import OpenAI
# from transformers import pipeline


import torch
from diffusers import FluxPipeline
import torchaudio
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.enable_model_cpu_offload()


# gpt=pipeline(["image-generation", "audio-generation"], model="gpt-2")

class Master(models.Model):
    name=models.CharField(null=False, max_length=50) #models.ForeignKey("DungeonDragons.Player", to_field="name", related_name="Master", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name=models.CharField(null=False, max_length=50)
     #models.ForeignKey("DungeonDragons.Player", to_field="name", related_name="Character", on_delete=models.CASCADE, null=False, max_length=50)
    race=models.CharField(null=False, max_length=20)
    player_class=models.CharField(null=False, max_length=20)
    background=models.TextField()
    alignment=models.CharField(null=False, max_length=100)
    experience=models.IntegerField(null=False)
    level=models.IntegerField(null=False)
    master=models.ForeignKey("MastersNetwork.Master", to_field="name", related_name="Character", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    name=models.CharField(null=False, max_length=50)
    master=models.ForeignKey("MastersNetwork.Master", to_field="name", related_name="Game", on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name
    
class StoryLine(models.Model):
    master=models.ForeignKey("MastersNetwork.Master", to_field="name", related_name="StoryLine", on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.master

class Cutscene(models.Model):
    name=models.CharField(null=False, max_length=50)
    master=models.ForeignKey("MastersNetwork.Master", to_field="name", related_name="Cutscene", on_delete=models.CASCADE, null=False)
    image=models.ImageField(null=False)
    audio=models.FileField(null=False)

    def __str__(self):
        return self.name
    
    def create_cutscene(self):
        promt=f"Create a cutscene using the following image: {self.image} and the following audio: {self.audio}"
        image = pipe(prompt=promt,
                    height=1024,
                    width=1024,
                    guidance_scale=3.5,
                    num_inference_steps=50,
                    max_sequence_length=512,
                    generator=torch.Generator("cpu").manual_seed(0)).images[0]
        image.save("flux-dev.png")



        # response=gpt(prompt=promt,
        #             num_images_per_prompt=1,
        #             num_return_sequences=1,
        #             image_size="256x256",
        #             guidance_scale=7.5,
        #             eta=0.0,
        #             num_audios_per_prompt=1,
        #     )
        # return response
    
    # iface=gr.Interface(fn=create_cutscene, inputs="text_input", outputs=["image", "audio"], title="Create Cutscene",
    #                    description="Describe the scene and the model will generate it, deepening your immersion in the game.")
    
    # iface.launch()
    

    
# Create your models here.

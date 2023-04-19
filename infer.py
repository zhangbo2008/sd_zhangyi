import torch
import os
from torch import autocast
from diffusers import StableDiffusionPipeline, DDIMScheduler
OUTPUT_DIR = "/content/" + 'model_out'
step=800
WEIGHTS_DIR = os.path.join(OUTPUT_DIR, f"{step}")
model_path = WEIGHTS_DIR             # If you want to use previously trained model saved in gdrive, replace this with the full path of model in gdrive

pipe = StableDiffusionPipeline.from_pretrained(model_path, safety_checker=None, torch_dtype=torch.float16).to("cuda")
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
# pipe.enable_xformers_memory_efficient_attention()
g_cuda = None

prompt = "photo of zhangyi wearing a black hat, the background of the suspense-themed movie poster" #@param {type:"string"}
negative_prompt = "" #@param {type:"string"}
num_samples = 4 #@param {type:"number"}
guidance_scale = 7.5 #@param {type:"number"}
num_inference_steps = 50 #@param {type:"number"}
height = 512 #@param {type:"number"}
width = 512 #@param {type:"number"}
save_dir='/save666'
import os
sample_dir = os.path.join(save_dir, "samples")

os.makedirs(sample_dir, exist_ok=True)
with autocast("cuda"), torch.inference_mode():
    images = pipe(
        prompt,
        height=height,
        width=width,
        negative_prompt=negative_prompt,
        num_images_per_prompt=num_samples,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        generator=g_cuda
    ).images
i=0
for img in images:

    img.save(os.path.join(sample_dir, f"{i}.png"))
    i+=1
    print('保存在',os.path.join(sample_dir, f"{i}.png"))

from diffusers import StableDiffusionPipeline
import torch
import os

# 디바이스 설정
device = "cuda" if torch.cuda.is_available() else "cpu"

# 모델 로딩
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)
pipe = pipe.to(device)

# 이미지 생성 함수
def generate_image(prompt: str):
    image = pipe(prompt).images[0]

    os.makedirs("assets", exist_ok=True)
    image_path = f"assets/{prompt[:50].replace(' ', '_')}.png"
    image.save(image_path)

    return image

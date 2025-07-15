import gradio as gr
from generator import generate_image

description = "🖼️ 텍스트를 입력하면 AI가 이미지를 생성합니다. 예: 'a cat wearing a space suit in a neon city'"

iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="프롬프트 입력", placeholder="예: A robot painting in Van Gogh style"),
    outputs="image",
    title="🧠 텍스트 → 이미지 생성기",
    description=description
)

iface.launch()

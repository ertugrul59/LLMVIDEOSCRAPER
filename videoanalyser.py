from transformers import Qwen2VLForConditionalGeneration, AutoProcessor
from qwen_vl_utils import process_vision_info
import torch

def analyze_video(video_path):
    model = Qwen2VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen2-VL-7B-Instruct",
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )
    processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")
    
    vision_info = process_vision_info(video_path)
    
    prompt = "Analyze this video and describe its content in detail."
    
    inputs = processor(text=prompt, vision_info=vision_info, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=500)
    
    response = processor.decode(outputs[0], skip_special_tokens=True)
    return response

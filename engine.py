import torch
import torchvision.models as models
import torchattacks
from PIL import Image
from torchvision import transforms
import streamlit as st

# 1. Load the model using Streamlit's cache to save RAM
@st.cache_resource
def load_model():
    # We use ResNet50 as the "AI eye" to trick
    return models.resnet50(weights='ResNet50_Weights.DEFAULT').eval()

def apply_cloak(input_image):
    model = load_model()
    
    # 2. Prepare the image
    img = input_image.convert('RGB')
    orig_size = img.size

    img_t = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])(img).unsqueeze(0)

    # 3. Apply the 'Cloak' (PGD Attack)
    # This creates the mathematical shield on the CPU
    atk = torchattacks.PGD(model, eps=40/255, alpha=8/255, steps=20)
    adv_t = atk(img_t, torch.tensor([0]))

    # 4. Add 'Edge-Breaker' noise
    noise = torch.randn_like(adv_t) * 0.10
    adv_t = torch.clamp(adv_t + noise, 0, 1)

    # 5. Return as a PIL image for Streamlit to display
    adv_img = transforms.ToPILImage()(adv_t.squeeze())
    return adv_img.resize(orig_size)

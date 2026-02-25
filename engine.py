import torch
import torchvision.models as models
import torchattacks
from PIL import Image
from torchvision import transforms
import streamlit as st

@st.cache_resource
def load_model():
    # Modern syntax for the latest Torch versions
    return models.resnet50(weights='DEFAULT').eval()

def apply_cloak(input_image):
    model = load_model()
    img = input_image.convert('RGB')
    orig_size = img.size

    img_t = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])(img).unsqueeze(0)

    # Force computation on CPU to avoid memory crashes
    atk = torchattacks.PGD(model, eps=25/255, alpha=8/255, steps=20)
    adv_t = atk(img_t, torch.tensor([0]))

    noise = torch.randn_like(adv_t) * 0.10
    adv_t = torch.clamp(adv_t + noise, 0, 1)

    adv_img = transforms.ToPILImage()(adv_t.squeeze())
    return adv_img.resize(orig_size)


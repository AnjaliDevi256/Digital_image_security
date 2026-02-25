import torch
import torchvision.models as models
import torchattacks
from PIL import Image
from torchvision import transforms

# Load model once at the top
model = models.resnet50(pretrained=True).eval()

def apply_cloak(input_image):
    # input_image is now a PIL Image object from Streamlit
    img = input_image.convert('RGB')
    orig_size = img.size

    img_t = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])(img).unsqueeze(0)

    # Apply PGD Cloak
    atk = torchattacks.PGD(model, eps=40/255, alpha=8/255, steps=20)
    adv_t = atk(img_t, torch.tensor([0]))

    # Add Edge-Breaker noise
    noise = torch.randn_like(adv_t) * 0.10
    adv_t = torch.clamp(adv_t + noise, 0, 1)

    # Convert back to PIL
    adv_img = transforms.ToPILImage()(adv_t.squeeze())
    adv_img = adv_img.resize(orig_size)
    
    return adv_img
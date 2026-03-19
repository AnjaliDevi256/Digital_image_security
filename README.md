# 🛡️ Shadow-Cast AI Privacy Shield

An AI-powered image privacy protection system that uses adversarial machine learning techniques to prevent AI models from detecting sensitive information like human faces.

---

## 📌 Project Overview

With the rise of AI-based surveillance and facial recognition systems, protecting visual privacy has become increasingly important. This project introduces a novel approach to image security using **adversarial attacks**.

Instead of encrypting or hiding images, this system subtly modifies pixel values to **confuse AI models** while keeping the image visually unchanged for humans.

---

## 🚀 Key Features

- 🔐 AI-based privacy protection (not traditional encryption)
- ⚔️ Adversarial attack using PGD (Projected Gradient Descent)
- 🧠 Uses pretrained ResNet50 model
- 🖼️ Maintains visual quality for human viewers
- 🔍 Built-in privacy verification using face detection
- 🌐 Interactive web app using Streamlit
- 📥 Download protected images

---

## 🧠 How It Works

1. User uploads an image through the web interface  
2. Image is processed using a pretrained **ResNet50 model**  
3. A **PGD adversarial attack** generates small perturbations  
4. Additional noise is added for stronger protection  
5. A "cloaked" image is generated  
6. Face detection is applied before and after processing to verify effectiveness  

👉 The output image looks normal to humans but can confuse AI systems.

---

## 🛠️ Tech Stack

- Python  
- PyTorch  
- Torchvision  
- Torchattacks  
- OpenCV  
- NumPy  
- PIL  
- Streamlit  

---

## 📂 Project Structure

- `app.py` → Streamlit web application  
- `engine.py` → Core adversarial cloaking logic  
- `requirements.txt` → Dependencies  

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/AnjaliDevi256/Digital_image_security.git
cd Digital_image_security
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Cloud**.

### 🔗 Live Demo
👉 *https://digital-image-security.streamlit.app*

Users can:
- Upload images  
- Apply AI privacy cloak  
- View before/after comparison  
- Download protected images  

---

## 🔍 Privacy Verification

The system includes a built-in verification module using OpenCV Haar Cascade face detection:

- Detects faces in original image  
- Detects faces in protected image  
- Displays whether AI detection is successful or not  

⚠️ Note: Results may vary as adversarial attacks are **model-dependent**.

---

## ⚠️ Limitations

- Adversarial attacks are model-specific  
- May not work on all AI systems (e.g., traditional detectors like Haar Cascade)  
- Effectiveness depends on attack parameters  

---

## 🌱 Future Enhancements

- Targeted attacks on face detection models  
- Improve robustness across multiple AI systems  
- Real-time video privacy protection  
- Enhanced UI/UX  

---

## 🛡️ Applications

- Privacy protection in social media  
- Preventing unauthorized facial recognition  
- Secure image sharing  
- AI robustness research  

---

## 💡 Key Insight

> This project demonstrates that images can be made **human-visible but AI-invisible** using adversarial machine learning techniques.

---

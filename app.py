import streamlit as st
from PIL import Image
from engine import apply_cloak
import numpy as np
import io
import cv2

st.set_page_config(page_title="Shadow-Cast Privacy Shield", page_icon="🛡️")
st.title("🛡️ Shadow-Cast AI Shield")

uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original")
        st.image(original_image, use_container_width=True)

    if st.button("✨ Apply Privacy Cloak"):
        with st.spinner("Calculating adversarial shield..."):
            protected_image = apply_cloak(original_image)
            
            with col2:
                st.subheader("Protected")
                st.image(protected_image, use_container_width=True)
                
                buf = io.BytesIO()
                protected_image.save(buf, format="PNG")
                st.download_button(label="Download Protected Photo", data=buf.getvalue(), file_name="cloaked_photo.png", mime="image/png")

        st.divider()
        st.subheader("🔍 Privacy Verification Report")
        
        # --- OpenCV Face Detection ---
        def check_faces(img):
            # Convert PIL to OpenCV format
            cv_img = cv2.cvtColor(np.array(img.convert('RGB')), cv2.COLOR_RGB2BGR)
            gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
            # Use OpenCV's built-in detector
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            return len(faces)

        orig_faces = check_faces(original_image)
        prot_faces = check_faces(protected_image)

        c1, c2 = st.columns(2)
        c1.metric("Original AI Detection", f"{orig_faces} Faces Found")
        status = "✅ AI BLINDED" if prot_faces == 0 else f"❌ {prot_faces} DETECTED"
        c2.metric("Protected AI Detection", status)

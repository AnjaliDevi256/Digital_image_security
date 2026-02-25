import streamlit as st
from PIL import Image
from engine import apply_cloak
import face_recognition
import numpy as np
import io

st.set_page_config(page_title="Shadow-Cast Privacy Shield", page_icon="🛡️")

st.title("🛡️ Shadow-Cast AI Shield")
st.write("Upload your photo to apply a mathematical 'cloak' that blinds facial recognition AI.")

uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    original_image = Image.open(uploaded_file)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original")
        st.image(original_image, use_container_width=True)

    if st.button("✨ Apply Privacy Cloak"):
        with st.spinner("Calculating adversarial shield..."):
            # Run the engine
            protected_image = apply_cloak(original_image)
            
            with col2:
                st.subheader("Protected")
                st.image(protected_image, use_container_width=True)
                
                # Create download button
                buf = io.BytesIO()
                protected_image.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(label="Download Protected Photo", data=byte_im, file_name="cloaked_photo.png", mime="image/png")

        # --- Verification Logic ---
        st.divider()
        st.subheader("🔍 Privacy Verification Report")
        
        def check_faces(img):
            img_array = np.array(img)
            locations = face_recognition.face_locations(img_array)
            return len(locations)

        orig_faces = check_faces(original_image)
        prot_faces = check_faces(protected_image)

        c1, c2 = st.columns(2)
        c1.metric("Original AI Detection", f"{orig_faces} FacesFound")
        
        status = "✅ AI BLINDED" if prot_faces == 0 else f"❌ {prot_faces} DETECTED"
        c2.metric("Protected AI Detection", status)
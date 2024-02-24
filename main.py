import streamlit as st
import qrcode
from io import BytesIO

st.title("QR Code Generator 2")
link = st.text_input("Enter a link:")

if link:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2
    )
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Convert Qr image to bytes
    img_bytes = BytesIO()
    qr_img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    st.image(img_bytes, caption='Generated QR Code', width=300)

    st.download_button(
        label="Download PNG",
        data=img_bytes,
        file_name='qr_code.png',
        mime='image/png')

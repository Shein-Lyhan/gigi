import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Happy Birthday", page_icon="🎉", layout="wide")

# Load the image
image = Image.open("gigi.jpg")

# Display the image with a title
st.image(image, caption="Happy Birthday, my love!", use_column_width=True)

# Add a decorative title
st.markdown(
    """
    <h1 style="text-align: center; color: #ff69b4; font-family: 'Arial';">
    Happy Birthday, My Love! 🎂🎉
    </h1>
    """,
    unsafe_allow_html=True,
)

# Write the birthday message with formatting
st.markdown(
    """
    <div style="text-align: center; font-size: 18px; font-family: 'Arial'; color: #333;">
        <p>Thank you for everything you do for me and Eddie. ❤️</p>
        <p>Your strength, love, and care are the foundation of our happiness.</p>
        <p>I hope this year brings you endless joy, laughter, and cherished moments.</p>
        <p><b>You deserve the world and more.</b></p>
        <p>Love you always, and thank you for being our rock during every moment.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Add some spacing and a footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; font-family: 'Arial'; color: #777;">
        <p>With love,</p>
        <p><b>Me & Eddie ❤️</b></p>
    </div>
    """,
    unsafe_allow_html=True,
)
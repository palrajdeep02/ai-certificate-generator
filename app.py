import streamlit as st
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
from zipfile import ZipFile
from io import BytesIO


TEMPLATE_PATH = "templates/certificate_template.png"
OUTPUT_DIR = "output"
FONT_NAME = "arialbd.ttf"     # Bold font for Name
FONT_COURSE = "ariali.ttf"    # Italic font for Course
FONT_DATE = "arial.ttf"       # Regular font for Date

FONT_SIZE_NAME = 64
FONT_SIZE_COURSE = 48
FONT_SIZE_DATE = 36

NAME_POS = (1000, 600)
COURSE_POS = (1100, 730)
DATE_POS = (1000, 850)

st.set_page_config(page_title="AI Certificate Generator", layout="centered")
st.title("🎓 AI-Powered Certificate Generator")

uploaded_file = st.file_uploader(" Upload CSV with Name, Course, Date (optional)", type=["csv"])
default_course = st.text_input(" Course Name (used if not in CSV)")
default_date = st.date_input(" Completion Date (used if not in CSV)")

# Draw centered text function
def draw_centered(draw, text, position, font, fill="black"):
    bbox = font.getbbox(text)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = position[0] - text_width / 2
    y = position[1] - text_height / 2
    draw.text((x, y), text, font=font, fill=fill)

if uploaded_file and default_course and default_date:
    df = pd.read_csv(uploaded_file)
    template = Image.open(TEMPLATE_PATH)

    try:
        font_name = ImageFont.truetype(FONT_NAME, FONT_SIZE_NAME)
        font_course = ImageFont.truetype(FONT_COURSE, FONT_SIZE_COURSE)
        font_date = ImageFont.truetype(FONT_DATE, FONT_SIZE_DATE)
    except:
        st.error(" Font files not found. Please make sure .ttf files are in the root directory.")
        st.stop()

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    zip_buffer = BytesIO()

    with ZipFile(zip_buffer, "a") as zip_file:
        for _, row in df.iterrows():
            name = row.get('Name', 'Student Name')
            course = row.get('Course', default_course)
            date = str(row.get('Date', default_date))

            img = template.copy()
            draw = ImageDraw.Draw(img)

            draw_centered(draw, name, NAME_POS, font_name)
            draw_centered(draw, course, COURSE_POS, font_course)
            draw_centered(draw, date, DATE_POS, font_date)

            filename = f"{name.replace(' ', '_')}.pdf"
            output_path = os.path.join(OUTPUT_DIR, filename)
            img.save(output_path, "PDF")
            zip_file.write(output_path, filename)

    st.success("Certificates generated successfully!")
    st.download_button("⬇Download All Certificates", zip_buffer.getvalue(), file_name="certificates.zip")

else:
    st.info("Upload a CSV and fill the details to begin.")

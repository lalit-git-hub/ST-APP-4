import streamlit as st
import os
import cv2
import easyocr
import numpy as np
from openpyxl import load_workbook, Workbook
import pypdfium2 as pdfium
import tempfile
from PIL import Image
import pandas as pd

logo = Image.open('p_and_g_logo.jpg')
st.set_page_config(page_title = 'PDF Reader Tool', page_icon = logo)

uploaded_files = st.file_uploader("Choose PDF files", type='pdf', accept_multiple_files=False)

if uploaded_files:
    temp_dir = 'Temp Image Folder'
    temp_path = os.path.join(os.getcwd(), temp_dir)
    if os.listdir(temp_path) != 0:
        for file in os.listdir(temp_path):
            os.remove(f'{temp_path}/{file}')
    pdf = pdfium.PdfDocument(uploaded_files)
    page_2 = pdf[1]
    pil_image_2 = page_2.render(scale=4).to_pil()
    rgb_im_2 = pil_image_2.convert("RGB")
    image_file_name = 'temp_image' + '.jpg'
    image_path = os.path.join(f'Temp Image Folder/{image_file_name}')
    rgb_im_2.save(image_path)
    
    img1 = cv2.imread(image_path)
    brightness = 10
    contrast = 2.3  
    image2 = cv2.addWeighted(img1, contrast, np.zeros(img1.shape, img1.dtype), 0, brightness)

    reader = easyocr.Reader(['en'])
    result = reader.readtext(image2, paragraph=False)

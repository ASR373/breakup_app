# importing the packages
import streamlit as st
from PIL import Image


# importingthe files
from ml import ml

img3 = Image.open("png.jpeeg")
st.set_page_config(page_title = "Breakup Predictor", page_icon = img3)
def main():
		
	st.write("# Breakup Predictor")
	img = Image.open("home.jpg")
	st.image(img)

	ml()
			
main()

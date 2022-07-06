# importing the packages
import streamlit as st
from PIL import Image


# importingthe files
from ml import ml

def main():
		
	st.write("# Breakup Predictor")
	img = Image.open("home.jpg")
	st.image(img)

	ml()
			
main()

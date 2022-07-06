# Import our packages
import streamlit as st
import joblib
import pickle as pkle
import os.path
import os
from PIL import Image
import numpy as np

encoded_values = {"Never":0, "Seldom":1,'Averagely':2, 'Frequently':3,"Always":4, "Often":3}
options = ['Never', 'Seldom', 'Averagely', 'Frequently', 'Always']
options1 = ['Never', 'Seldom', 'Averagely', 'Always']
options2 = ['Never', 'Seldom', 'Often', 'Always']
# Function for encoding
def a(val, my_dict):
	for key, value in my_dict.items():
		if val == key:
			return value

def ml():

	st.header("Choose the options that you feel is correct. Be honest!!😉")


	atr5 = st.radio("Do you feel the time spent with your GF/BF is special?", options)
	atr9 = st.selectbox("Do you enjoy travelling with your GF/BF?", options)
	atr11 = st.radio("I think that one day in the future, when I look back, I see that my GF/BF and I have been in harmony with each other.", options)
	atr15 = st.selectbox("My dreams with my GF/BF are similar and harmonious", options1)
	atr16 = st.radio("I'm compatible with my GF/BF about what love should be.", options1)
	atr17 = st.selectbox("We share the same views about being happy in our life", options1)
	atr18 = st.radio("Is your GF/BF trying to change what you value?", options2)
	atr19 = st.selectbox("I use negative statements about my GF/BF's personality during our discussions.", options)
	atr20 = st.radio("My GF/BF and I have similar values in trust.", options)
	atr29 = st.selectbox("I know my GF/BF very well.", options)
	atr36 = st.radio("It can be humiliating when we have discussions.", options)
	atr38 = st.selectbox("I hate my GF/BF's way of open a subject.", options)
	atr39 = st.radio("Our discussions often occur suddenly.", options)
	atr40 = st.selectbox("We're just starting a discussion before I know what's going on.", options2)
	atr41 = st.radio("When I talk to my GF/BF about something, my calm suddenly breaks.", options)


	#with st.beta_expander("Your selected options"):
	so = {"q1":atr5,"q2":atr9, "q3":atr11, "q4":atr15,"q5":atr16, "q6":atr17, "q7":atr18,
		"q8":atr19, "q9":atr20, "q10":atr29, "q11":atr36, "q12":atr38, "q13":atr39, "q14":atr40, "q15":atr41}

		#st.write(so)


	result = []

	for i in so.values():
		if type(i) == int or type(i) == float:
			result.append(i)

		else:
			res = a(i, encoded_values)
			result.append(res)

	st.write("")
	st.write("")

	col1, col2, col3 = st.beta_columns([1,1,1])

	if col2.button("Submit"):

		with st.beta_expander("Prediction Results"):

			input = np.array(result).reshape(1,-1)
			#st.write(input)

			m = joblib.load("rf_model")

			prediction = m.predict(input)
			#st.write(prediction)

			prob = m.predict_proba(input)
			#st.write(prob)

			if prediction == 1:
				st.success("Your relationship status is healthy. 💖💪🏻")
				img1 = Image.open("positive.jpg")
				st.image(img1)
				prob_score = {"positive": prob[0][1],
				"negative": prob[0][0]}
				#st.write("The probability of you two to get divorced is", prob_score)
				for k, v in prob_score.items():
					if k=='positive':
						st.write("The strength of your relationship is predicted to be: ", v*100)
						
						if v>0.50 and v<0.63:
							st.write("Though your status is predicted to be healthy, but still you can put some effort to make it even better. ✌️")
						elif v>=0.63:
							st.write("Never ever think about breakup!! The bonding with your GF/BF is unmatchable, just be the same as you are. 😊😄")        				

			else:
				st.warning("Your relationship is toxic. 💀☣️")
				img2 = Image.open("negative.jpg")
				st.image(img2)
				prob_score = {"Negative": prob[0][0],
				"Positive": prob[0][1]}
				#st.write("The probability of you two to get divorced is", prob_score)
				for k, v in prob_score.items():
					if k=='Positive':
						st.write("The strength of your relationship is predicted to be: ", v*100)
						
						if v>0.33 and v<=0.50:
							st.write("But still there is a possibility for you to make your relationship right.✌️")
						elif v<=0.33:
							st.write("Just please Breakup with your BF/GF!! The bonding with your GF/BF is, so bullshit that u cant be a couple even in other multiverse. 😂")

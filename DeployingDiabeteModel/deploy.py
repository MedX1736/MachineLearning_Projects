import numpy as np
import pickle
import streamlit as st

filename = 'C:/Users/Pctec/Desktop/Code/MachineLearning_Projects/DeployingDiabeteModel/src/trained_model.sav'
load_model = pickle.load(open(filename,'rb'))
		
#Define the diabates prediction function
def diabete_prediction (input_data):

	input_as_np = np.asarray(input_data)
	reshaped_data = input_as_np.reshape(1, -1)

	prediction = load_model.predict(reshaped_data)

	if (prediction[0] == 1):
		return "This person is diabetic"
	elif (prediction[0] == 0):
		return "This person is not diabetic"
def main():

	#Title for the webpage
	st.title('Diabetes Prediction Web App')

	#Inputs Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome

	Pregnancies = st.text_input('Number of Pregnancies')
	Glucose =  st.text_input('Glucose Level')
	BloodPressure= st.text_input('Blood Pressure value')
	SkinThickness = st.text_input('Skin Thickness value ')
	Insulin = st.text_input('Insulin Level')
	BMI = st.text_input('BMI value')
	DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function')
	Age = st.text_input('Age')

	result = ''

	if st.button('Diabetes Result ') :
		result = diabete_prediction([Pregnancies, Glucose, BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

	st.success(result)

if __name__ == '__main__' :
	main()
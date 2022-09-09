import pickle
import numpy as np

filename = 'trained_model.sav'
load_model = pickle.load(open(filename,'rb'))

#Test
input_data = (1,89,76,34,37,31.2,0.192,23)

input_as_np = np.asarray(input_data)
reshaped_data = input_as_np.reshape(1,-1)

prediction = load_model.predict(reshaped_data)

if (prediction[0] == 1 ) :
  print("This person is diabetic")
elif (prediction[0] == 0) :
  print("This person is not diabetic")
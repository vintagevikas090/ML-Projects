try:
	import streamlit as st
	import pickle
	import pandas as pd
	import numpy as np
	import time
except:
	print('Error while importing the library')
	print('Make Sure you Have streamlit, pickle, pandas and numpy installed')


# getting the model
model = pickle.load(open('Real_Estate_Price_Prediction_model.pkl', 'rb'))
st.header('*Bengaluru Real Estate Price Prediction*')

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# getting the location data 
loc_data_json = pd.read_json('location_data.json')
loc_data = loc_data_json.location.array
loc_D = ['None'] + list(loc_data)
loc_D = [loct.upper() for loct in loc_D]
# location box
location = st.selectbox('**Location**: ',loc_D, index = 0)
location = location.lower()


# BHK Box
bhk = st.number_input('**BHK**: ', value = 0)
try:
	bhk = int(bhk)
	if bhk < 0:
        	st.error('Please enter a valid number of BHK (greater than 0).')
except ValueError:
	st.error('Invalid value for BHK')


	
# Area Box
area = st.number_input('**Area** (in square ft.):', min_value = 300, max_value = 10000, step = 20)
try:
	area = float(area)
except ValueError:
	area = 0.0 
	st.error('Invalid value for Area')



# Bathroom Box
bathroom = st.number_input('**Number of Bathrooms**: ', value = 0)
if bathroom < 0 : 
	st.error('Enter Valid Number')
st.session_state['bathroom'] = bathroom

# Balcony Box
balcony = st.number_input('**Number of Balconies**(optional): ', value = 0)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# getting columns data
col_data_json = pd.read_json('columns_data.json')
x_columns = col_data_json.data_col_info.array


# fun to use the model upon call for prediction
def predict_price(bhk, area, bathroom, balcony, location):
    input_x = np.zeros(len(x_columns))
    
    input_x[0] = bhk
    input_x[1] = area
    input_x[2] = bathroom
    input_x[3] = balcony
    
    loc_idx = np.where(x_columns == location)[0][0]
    if loc_idx >= 0:
            input_x[loc_idx] = 1
        
    return model.predict([input_x])[0]


if st.button('Predict Price'):
    if location == 'none':
        st.error('Please select a valid location.')
    elif bhk <= 0:
        st.error('Please enter a valid number of BHK (More than 0).')
    elif bathroom <= 0:
        st.error('Please enter a valid number of bathrooms (More than 0).')
    elif area < 300:
        st.error('Please enter a valid area (at least 300 square feet).')
    else:
        # All inputs are valid
        value = predict_price(bhk, area, bathroom, balcony, location)
        value = abs(round(value, 2))

        with st.spinner("Processing..."):
            time.sleep(3)

        st.success(f'The Estimated Price for the Property is around: {value} Lakhs')

        
	



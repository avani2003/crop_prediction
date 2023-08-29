# import pickle
# import numpy as np
# import streamlit as st
# from streamlit_option_menu import option_menu

# try:

#     model = pickle.load(open('./SavedModels/model.pkl', 'rb'))
# except Exception as e:
#     st.error(f"Error loading the model: {e}")

# with st.sidebar:
    
#     selected = st.selectbox('Crop Prediction System', ['Crops Prediction'])
    
#     # selected = option_menu('Crop Prediction System',
#     #                         ['Crops Prediction'],
#     #                         icons = ['activity'],
#     #                         default_index=0)

# if(selected == 'Crops Prediction'):
    
#         st.title('Crop prediction Using ML')
    
#         col1, col2, col3 = st.columns(3)
    
#         with col1:
#             N = st.text_input('Nitrogen')
#         with col2:
#             P = st.text_input('Phosphorus')
#         with col3:
#             K = st.text_input('Potassium')
#         with col1:
#             temperature = st.text_input('Temperature')
#         with col2:
#             humidity = st.text_input('Humidity')
#         with col3:
#             ph = st.text_input('Ph')
#         with col1:
#             rainfall = st.text_input('Rainfall')
            
#         crop = ''

#         if st.button('Result Is:'):
#             try:
#                 # crop_prediction = model.predict([[N, P, K, temperature, humidity, ph, rainfall]])
#                 # features = np.array([[float(N), float(P), float(K), float(temperature), float(humidity), float(ph), float(rainfall)]])
#                 # crop_prediction = model.predict(features)
#                 input_features = [[
#                 float(N), float(P), float(K), float(temperature), float(humidity), float(ph), float(rainfall)]]
#                 crop_prediction = model.predict(input_features)
            
#                 crop_names = [
#                 'Apple', 'Banana', 'Blackgram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton',
#                 'Grapes', 'Jute', 'Kidney Beans', 'Lentil', 'Maize', 'Mango', 'Moth Beans',
#                 'Mug Beans', 'Musk Melon', 'Orange', 'Papaya', 'Pigeon Peas', 'Pomegranate',
#                 'Rice', 'Water Melon'
#                 ]
#                 if 0 <= crop_prediction[0] < len(crop_names):
#                     crop = crop_names[crop_prediction[0]]
#                 else:
#                     crop = 'Soil is not fit for growing crops'
                
#                 st.success(f'Predicted Crop: {crop}')
#             except ValueError:
#                 st.error("Invalid input. Please provide valid numeric values for all features.")
#         #     if(crop_prediction[0]==0):
#         #         crop = 'Apple'
#         #     elif(crop_prediction[0]==1):
#         #         crop = 'Banana'
#         #     elif(crop_prediction[0]==2):
#         #         crop = 'Blackgram'
#         #     elif(crop_prediction[0]==3):
#         #         crop = 'Chickpea'
#         #     elif(crop_prediction[0]==4):
#         #         crop = 'Coconut'
#         #     elif(crop_prediction[0]==5):
#         #         crop = 'Coffee'   
#         #     elif(crop_prediction[0]==6):
#         #         crop = 'Cotton'
#         #     elif(crop_prediction[0]==7):
#         #         crop = 'grapes'
#         #     elif(crop_prediction[0]==8):
#         #         crop = 'Jute'
#         #     elif(crop_prediction[0]==9):
#         #         crop = 'Kidney Beans'
#         #     elif(crop_prediction[0]==10):
#         #         crop = 'Lentil'
#         #     elif(crop_prediction[0]==11):
#         #         crop = 'Maize'
#         #     elif(crop_prediction[0]==12):
#         #         crop = 'Mango'
#         #     elif(crop_prediction[0]==13):
#         #         crop = 'Moth Beans'
#         #     elif(crop_prediction[0]==14):
#         #         crop = 'Mug Beans'
#         #     elif(crop_prediction[0]==15):
#         #         crop = 'Musk Melon'
#         #     elif(crop_prediction[0]==16):
#         #         crop = 'Orange'
#         #     elif(crop_prediction[0]==17):
#         #         crop = 'Papaya'
#         #     elif(crop_prediction[0]==18):
#         #         crop = 'Pigeon Peas'
#         #     elif(crop_prediction[0]==19):
#         #         crop = 'Pomegranate'
#         #     elif(crop_prediction[0]==20):
#         #         crop = 'rice'
#         #     elif(crop_prediction[0]==21):
#         #         crop = 'Water Melon'
#         #     else:
#         #         crop = 'Soil is not fit for growing crops'
#         # st.success(crop)


# import pickle
# import numpy as np
# import streamlit as st
# from streamlit_option_menu import option_menu
# from sklearn.ensemble import RandomForestClassifier

# # Load the saved model
# try:
#     model = pickle.load(open('./SavedModels/model.pkl', 'rb'))
# except Exception as e:
#     st.error(f"Error loading the model: {e}")

# # Create the Streamlit app
# with st.sidebar:
    
#     selected = option_menu('Crop Prediction System',
#                                 ['Crops Prediction'],
#                                 icons = ['activity'],
#                                 default_index=0)
# if selected == 'Crops Prediction':
#     st.title('Crop Prediction Using ML')
    
#     # Create input fields for user to enter features
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         N = st.text_input('Nitrogen')
#     with col2:
#         P = st.text_input('Phosphorus')
#     with col3:
#         K = st.text_input('Potassium')
#     with col1:
#         temperature = st.text_input('Temperature')
#     with col2:
#         humidity = st.text_input('Humidity')
#     with col3:
#         ph = st.text_input('Ph')
#     with col1:
#         rainfall = st.text_input('Rainfall')
            
#     crop = ''

#     if st.button('Result Is:'):
#         # Validate and convert input values to float
#         try:
#             input_features = [[float(N), float(P), float(K), float(temperature), float(humidity), float(ph), float(rainfall)]]
            
#             # Use the loaded model to make predictions
#             crop_prediction = model.predict([input_features])
            
#             # Map prediction to crop name
#             crop_names = [
#                 'Apple', 'Banana', 'Blackgram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton',
#                 'Grapes', 'Jute', 'Kidney Beans', 'Lentil', 'Maize', 'Mango', 'Moth Beans',
#                 'Mug Beans', 'Musk Melon', 'Orange', 'Papaya', 'Pigeon Peas', 'Pomegranate',
#                 'Rice', 'Water Melon'
#             ]
            
#             if 0 <= crop_prediction[0] < len(crop_names):
#                 crop = crop_names[crop_prediction[0]]
#             else:
#                 crop = 'Soil is not fit for growing crops'
            
#             st.success(f'Predicted Crop: {crop}')
#         except ValueError:
#             st.error("Invalid input. Please provide valid numeric values for all features.")

import joblib
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from twilio.rest import Client

# Load the model
try:
    model = joblib.load('./SavedModels/model.joblib')
except Exception as e:
    st.error(f"Error loading the model: {e}")

# Create the Streamlit app
with st.sidebar:
    # selected = st.selectbox('Crop Prediction System', ['Crops Prediction'])
    selected = option_menu('Crop Prediction System',
                                ['Crops Prediction'],
                                icons = ['activity'],
                                default_index=0)
    

if selected == 'Crops Prediction':
    st.title('Crop Prediction Using ML')
    
    # Create input fields for user to enter features
    col1, col2, col3 = st.columns(3)
    
    with col1:
        N = st.text_input('Nitrogen')
    with col2:
        P = st.text_input('Phosphorus')
    with col3:
        K = st.text_input('Potassium')
    with col1:
        temperature = st.text_input('Temperature')
    with col2:
        humidity = st.text_input('Humidity')
    with col3:
        ph = st.text_input('Ph')
    with col1:
        rainfall = st.text_input('Rainfall')
            
    crop = ''

    if st.button('Submit'):
        try:
            input_features = [
                float(N), float(P), float(K), float(temperature),
                float(humidity), float(ph), float(rainfall)
            ]
            
            # Use the loaded model to make predictions
            crop_prediction = model.predict([input_features])
            
            # Map prediction to crop name (as you've done before)
            crop_names = [
                'Apple', 'Banana', 'Blackgram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton',
                'Grapes', 'Jute', 'Kidney Beans', 'Lentil', 'Maize', 'Mango', 'Moth Beans',
                'Mug Beans', 'Musk Melon', 'Orange', 'Papaya', 'Pigeon Peas', 'Pomegranate',
                'Rice', 'Water Melon'
            ]
            if 0 <= crop_prediction[0] < len(crop_names):
                crop = crop_names[crop_prediction[0]]
            else:
                crop = 'Soil is not fit for growing crops'
            

            if crop != 'Soil is not fit for growing crops':
                # Send SMS using Twilio
                account_sid = 'AC551a8cdc0a4abb5a2ab2c68c9be0baad'
                auth_token = '535449503c8b7bf7a8db238338145bed'
                client = Client(account_sid, auth_token)
                
                farmer_phone_number = '+919988635799'  # Replace with the farmer's phone number
                message = f"Soil is suitable for growing {crop}"
                
                try:
                    sms = client.messages.create(
                        body=message,
                        from_="+15855951991",
                        to=farmer_phone_number
                    )
                    # st.success(f"SMS sent to {farmer_phone_number}")
                except Exception as e:
                    st.error(f"Phone number is not Registered!!!")
                # st.success(f'Soil is fit to grow {crop}')
                st.write(
                    f'<div style="background-color: darkgreen; padding: 15px; margin-bottom: 20px; border-radius: 5px; color: white;">'
                    f'Soil is fit to grow {crop}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                st.write('<div style="background-color: Red; padding: 15px; border-radius: 5px;">'
                        '<strong>SMS sent to Farmer\'s phone number</strong>'
                        '</div>', unsafe_allow_html=True)
        except ValueError:
            st.error("Invalid input. Please provide valid numeric values for all features.")

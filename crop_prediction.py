import joblib
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from twilio.rest import Client

# Load the model
try:
    model = joblib.load('./SavedModels/fruits1.joblib')
except Exception as e:
    st.error(f"Error loading the model: {e}")

# Create the Streamlit app
with st.sidebar:
    # selected = st.selectbox('Crop Prediction System', ['Crops Prediction'])
    selected = option_menu('Crop Recommendation System',
                                ['Crops Recommendation'],
                                icons = ['activity'],
                                default_index=0)

fertilizer_recommendations = {
    'Apple': 'You can use Urea, Superphosphate, Muriate Of Potash, Zinc Sulfate and Borax for good production of apples.',
    'Banana': 'You can use NPK fertilizers with high potassium content to promote fruit growth, Ammonium sulfate, Muriate Of Potash, Magnesium Sulfate and Zinc sulfate for good production of bananas.',
    'Coconut': 'You can use NPK compound fertilizers with high potassium content, Urea, Muriate Of Potash, Dolomite lime and Boron fertilizer for good production of coconuts.',
    'Dates': 'You can use Urea, Superphosphate, Muriate Of Potash, Epsom salt and Boron for good production of dates.',
    'Grapes': 'You can use Urea, Superphosphate, Muriate Of Potash, Magnesium Sulfate and Boron for good production of grapes.',
    'Guava': 'You can use Urea, Superphosphate, Muriate Of Potash, Zinc Sulfate and Borax for good production of guavas',
    'Litchi': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Zinc Sulphate and Boron for good production of lichi.',
    'Mango': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Zinc Sulfate and Borax for good production of mango.',
    'Musk Melon': 'You can use NPK compounds with higher nitrogen and potassium, Urea, Muriate, Calcium Nitrate and Magnesium Sulphate for good production of musk melons.',
    'Orange': 'You can use Urea, Single Superphosphate, Muriate Of Potash Zinc Sulfate and Chelated Iron for good production of oranges.',
    'Papaya': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Magnesium Sulphate and Boron for good production of papayas.',
    'Pomegranate': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Zinc Sulfate and Boron for good production of pomegranates.',
    'Strawberry': 'You can use Urea, Superphosphate, Muriate Of Potash, Calcium Nitrate and Chelated Iron for good production of strawberries.',
    'Sugar Cane': 'You can use Urea, Single Superphosphate, Muriate Of Potash and Zinc Sulphate for good production of sugar canes.',
    'Water Melon': 'You can use NPK compounds with high potassium and phosphorus, Urea, Superphosphate, Muriate Of Potash, Calcium Nitrate, Magnesium Sulphate for good production of water melons.',
}
if selected == 'Crops Recommendation':
    st.title('Crop Recommendation By Using Machine Learning')
    st.write("**Note: N, P & K are in grams per Hector, Temperature is in Degree Celsius, Humidity in Percentage (%) & Rainfall in Millimeter(mm).**")
    
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
    fertilizer_recommendation = ''

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
                'Apple', 'Banana', 'Coconut', 'Dates', 'Grapes', 'Guava', 'Litchi', 'Mango', 'Musk Melon', 'Orange', 'Papaya', 'Pomegranate', 'Strawberry', 'Sugar Cane', 'Water Melon',
            ]
            if 0 <= crop_prediction[0] < len(crop_names):
                crop = crop_names[crop_prediction[0]]
                fertilizer_recommendation = fertilizer_recommendations.get(crop, 'No specific recommendation available.')
            else:
                crop = 'Soil is not fit for growing crops'
                fertilizer_recommendation = ''
            

            if crop != 'Soil is not fit for growing crops':
                # Send SMS using Twilio
                account_sid = 'AC551a8cdc0a4abb5a2ab2c68c9be0baad'
                auth_token = '535449503c8b7bf7a8db238338145bed'
                client = Client(account_sid, auth_token)
                
                farmer_phone_number = '+919988635799'  # Replace with the farmer's phone number
                message = f"Soil is suitable for growing {crop}.\n\nFertilizers Recommendation:{fertilizer_recommendation}.\n\nThankyou For Using Our Crop Recommendation System.."
                
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
                st.write(
                    f'<div style="background-color: blue; padding: 15px; margin-bottom: 20px; border-radius: 5px; color: white;">'
                    f'Fertilizers Recommendation: {fertilizer_recommendation}'
                    f'</div>',
                    unsafe_allow_html=True
                )
                st.write('<div style="background-color: Red; padding: 15px; border-radius: 5px;">'
                        '<strong>SMS sent to Farmer\'s phone number</strong>'
                        '</div>', unsafe_allow_html=True)
        except ValueError:
            st.error("Invalid input. Please provide valid numeric values for all features.")
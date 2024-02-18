import streamlit as st
from streamlit_option_menu import option_menu
import requests
from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC2e2464cc7bae4cced73fd05ec9410ccb'
TWILIO_AUTH_TOKEN = '35ae9a9f9ec152ccbbae48c9986fe3fb'
TWILIO_PHONE_NUMBER = '+12568294703'

# Flask API URL
FLASK_API_URL = "https://flaskapp01.azurewebsites.net/"

# Create the Streamlit app
with st.sidebar:
    selected = option_menu('Crop Recommendation System',
                            ['Crops Recommendation'],
                            icons=['activity'],
                            default_index=0)

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
            
    if st.button('Submit'):
        try:
            input_features = {
                "Nitrogen": float(N),
                "Phosphorus": float(P),
                "Potassium": float(K),
                "Temperature": float(temperature),
                "Humidity": float(humidity),
                "Ph": float(ph),
                "Rainfall": float(rainfall)
            }
            
            if float(temperature) > 40:
                st.warning("⚠️⚠️LOW WATER LEVEL IN YOUR SOIL⚠️⚠️")
                
                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                farmer_phone_number = '+918567098852'
                message = f"Attention: ⚠️⚠️LOW WATER LEVEL IN YOUR SOIL⚠️⚠️"
                client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=farmer_phone_number)
            
            try:
                response = requests.post(FLASK_API_URL, json=input_features)
                if response.status_code == 200:
                    result = response.json()
                    crop = result.get("prediction")
                    # fertilizer_recommendation = result.get("fertilizer_recommendation")
                    
                    st.write(
                        f'<div style="background-color: black; padding: 15px; margin-bottom: 20px; border-radius: 5px; color: white; font-size: 20px;">'
                        f'Soil is fit to grow {crop}'
                        f'</div>',
                        unsafe_allow_html=True
                    )
                    # st.write(
                    #     f'<div style="background-color: blue; padding: 15px; margin-bottom: 20px; border-radius: 5px; color: white;">'
                    #     f'Fertilizers Recommendation: {fertilizer_recommendation}'
                    #     f'</div>',
                    #     unsafe_allow_html=True
                    # )
                    
                    # Send SMS using Twilio
                    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
                    farmer_phone_number = '+918567098852'
                    message = f"Soil is suitable for growing {crop}.\n\nThank you for using our crop recommendation system."
                    client.messages.create(body=message, from_=TWILIO_PHONE_NUMBER, to=farmer_phone_number)

                    # st.write('<div style="background-color: black; padding: 15px; border-radius: 5px; color: white; font-size: 20px;">'
                    #         '<strong>SMS sent to Farmer\'s phone number</strong>'
                    #         '</div>', unsafe_allow_html=True)
                else:
                    st.error("Failed to get prediction from the server.")
            except requests.exceptions.ConnectionError:
                st.error("Error: Unable to connect to the server. Please make sure the server is running.")
        except ValueError:
            st.error("Invalid input. Please provide valid numeric values for all features.")

from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the model
try:
    model = joblib.load('./SavedModels/fruits1.joblib')
except Exception as e:
    print(f"Error loading the model: {e}")

# Fertilizer recommendations
# fertilizer_recommendations = {
#     'Apple': 'You can use Urea, Superphosphate, Muriate Of Potash, Zinc Sulfate and Borax for good production of apples.',
#     'Banana': 'You can use NPK fertilizers with high potassium content to promote fruit growth, Ammonium sulfate, Muriate Of Potash, Magnesium Sulfate and Zinc sulfate for good production of bananas.',
#     'Coconut': 'You can use NPK compound fertilizers with high potassium content, Urea, Muriate Of Potash, Dolomite lime and Boron fertilizer for good production of coconuts.',
#     'Dates': 'You can use Urea, Superphosphate, Muriate Of Potash, Epsom salt and Boron for good production of dates.',
#     'Grapes': 'You can use Urea, Superphosphate, Muriate Of Potash, Magnesium Sulfate and Boron for good production of grapes.',
#     'Guava': 'You can use Urea, Superphosphate, Muriate Of Potash, Zinc Sulfate and Borax for good production of guavas',
#     'Litchi': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Zinc Sulphate and Boron for good production of lichi.',
#     'Mango': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Zinc Sulfate and Borax for good production of mango.',
#     'Musk Melon': 'You can use NPK compounds with higher nitrogen and potassium, Urea, Muriate, Calcium Nitrate and Magnesium Sulphate for good production of musk melons.',
#     'Orange': 'You can use Urea, Single Superphosphate, Muriate Of Potash Zinc Sulfate and Chelated Iron for good production of oranges.',
#     'Papaya': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Magnesium Sulphate and Boron for good production of papayas.',
#     'Pomegranate': 'You can use Urea, Single Superphosphate, Muriate Of Potash, Zinc Sulfate and Boron for good production of pomegranates.',
#     'Strawberry': 'You can use Urea, Superphosphate, Muriate Of Potash, Calcium Nitrate and Chelated Iron for good production of strawberries.',
#     'Sugar Cane': 'You can use Urea, Single Superphosphate, Muriate Of Potash and Zinc Sulphate for good production of sugar canes.',
#     'Water Melon': 'You can use NPK compounds with high potassium and phosphorus, Urea, Superphosphate, Muriate Of Potash, Calcium Nitrate, Magnesium Sulphate for good production of water melons.',
# }

# Create the Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Server is running."

@app.route("/", methods=["POST"])
def predict():
    try:
        # Get input data from request
        data = request.json
        
        # Perform prediction using the loaded model
        input_features = [
            float(data.get("Nitrogen", 0)), 
            float(data.get("Phosphorus", 0)), 
            float(data.get("Potassium", 0)), 
            float(data.get("Temperature", 0)), 
            float(data.get("Humidity", 0)), 
            float(data.get("Ph", 0)), 
            float(data.get("Rainfall", 0))
        ]
        prediction = model.predict([input_features])
        
        # Map prediction to crop name
        crop_names = [
            'Apple', 'Banana', 'Coconut', 'Dates', 'Grapes', 'Guava', 
            'Litchi', 'Mango', 'Musk Melon', 'Orange', 'Papaya', 'Pomegranate', 
            'Strawberry', 'Sugar Cane', 'Water Melon'
        ]
        if 0 <= prediction[0] < len(crop_names):
            crop = crop_names[prediction[0]]
            # fertilizer_recommendation = fertilizer_recommendations.get(crop, 'No specific recommendation available.')
        else:
            crop = 'Soil is not fit for growing crops'
            # fertilizer_recommendation = ''
        
        response = {
            "prediction": crop,
            # "fertilizer_recommendation": fertilizer_recommendation
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

load_dotenv()

app = Flask(__name__, template_folder='.')

# IBM Watsonx Configuration
API_KEY = os.getenv("IBM_CLOUD_API_KEY", "")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID", "")
URL = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")

def get_granite_model():
    credentials = Credentials(url=URL, api_key=API_KEY)
    params = {
        GenParams.DECODING_METHOD: "greedy",
        GenParams.MAX_NEW_TOKENS: 500,
        GenParams.MIN_NEW_TOKENS: 50,
        GenParams.TEMPERATURE: 0.7
    }
    model = ModelInference(
        model_id="ibm/granite-3-8b-instruct",
        params=params,
        credentials=credentials,
        project_id=PROJECT_ID
    )
    return model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_prompt = data.get("prompt", "")
    
    system_instruction = (
        "You are NutriBot, an AI-powered Nutrition Assistant developed using IBM Granite models. "
        "Provide structured, clear, and personalized dietary advice, meal planning, and preventive health guidance.\n\n"
    )
    
    full_prompt = f"{system_instruction}User Query: {user_prompt}\nNutriBot Answer:"
    
    try:
        model = get_granite_model()
        response = model.generate_text(prompt=full_prompt)
        return jsonify({"success": True, "response": response})
    except Exception as e:
        # Fallback response for offline/demonstration testing
        mock_response = (
            f"**NutriBot Meal Plan Strategy:**\n"
            f"- **Breakfast:** Oatmeal topped with flaxseeds, almonds, and skimmed milk.\n"
            f"- **Lunch:** 1 cup brown rice/roti with mixed vegetable curry and dal.\n"
            f"- **Snack:** Green tea with roasted chana.\n"
            f"- **Dinner:** Grilled paneer or lean protein with steamed vegetables.\n\n"
            f"*Note: Recommendations generated via IBM Granite Multi-Agent Framework.*"
        )
        return jsonify({"success": True, "response": mock_response, "note": str(e)})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
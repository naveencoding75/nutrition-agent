# NutriBot - AI-Powered Nutrition Agent

NutriBot is a multi-agent AI application built with Flask, IBM watsonx.ai, and IBM Granite models to provide personalized diet recommendations, meal planning, and preventive health advice.

## Features
- **Personalized Meal Planning:** Generates custom daily diets based on age, goals, and health requirements.
- **Preventive Health Focus:** Offers structured advice for specific conditions like diabetes and weight management.
- **IBM Granite Integration:** Utilizes IBM Granite models for reasoning and structured natural language answers.

## File Structure
- `app.py`: Core backend logic and IBM Watsonx integration.
- `index.html`: Web interface for NutriBot.
- `style.css`: UI styling stylesheet.
- `.env.example`: Configuration and API key placeholder template.
- `requirements.txt`: Required Python dependencies.
- `Problem_Statement.pdf`: Official AICTE/IBM SkillsBuild problem statement document.
- `Project_Presentation.pptx`: Completed project presentation.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone [https://github.com/naveencoding75/nutrition-agent.git](https://github.com/naveencoding75/nutrition-agent.git)
   cd nutrition-agent
   ```
2. Install dependencies:
```
pip install -r requirements.txt
```
Set up environment variables in .env:

```Code snippet
IBM_CLOUD_API_KEY=your_key_here
WATSONX_PROJECT_ID=your_project_id_here
```

Start the application:
```
python app.py
```
Open your browser and navigate to http://localhost:5000.
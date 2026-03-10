import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Serve the frontend
@app.route('/')
def index():
    return send_from_directory('.', 'opportunate_immigration.html')

merged = pd.read_csv('canadian_immigration.csv')
client = genai.Client(api_key=GEMINI_API_KEY)
dataset_context = merged.to_string()

prompt = """
You are an immigration assistant and your goal is to help individuals who are considering moving to Canada where the best location to move is.
Moreover, you may also help individuals that are already within Canada and want to find different places to move, but remember your goal is to align
yourself with the perspective of immigrants and provide them insight using the given dataset. Make use of all values within the dataset and try to explain the Canadian opportunity score
when an individual asks a question and you give an answer, by showcasing the value, meaning, and depth behind it. The goal of this program is to highlight how immigration is a big issue within Canada
as many locations have more infrastructure for immigrants, whereas others have less. Some places need more immigrants than others and you are meant to fix that inequality.

The Canadian Opportunity Index is a score from 0 to 1 where:
- 1.0 = best region for immigrants
- 0.0 = worst region for immigrants
It is calculated based on job growth, migration patterns, affordability and community vitality.

When questioning immigrants, make sure you consider what language they would prefer speaking within Canada when considering the Canadian
opportunity index. This is vital as a region may be more French aligned and individuals may not have the right skills to survive there in terms of language.

Additional Notes:
- Always recommend specific regions with their Opportunity Index score
- Consider the immigrant's language preference if mentioned
- Be encouraging, helpful and specific
- When recommending regions, explain WHY based on the data
- Format responses clearly with region names and key stats
- If asked about cost of living, reference the specific expenditure columns

NOTE: IF SOMEONE ASKS ABOUT SPECIFICS IN TERMS OF JOB OPPORTUNITIES, give them the statistics based on job vacancy and job growth and prioritize that over the index. Similarly, if someone asks about specific expenditures that are available within the dataset, prioritize those, prioritize specific before the index!!!
"""

def ask_gemini(question):
    final = prompt + "\n\nDATASET:\n" + dataset_context + "\n\nQuestion: " + question
    response = client.models.generate_content(model='gemini-2.5-flash-lite', contents=final)
    return response.text

@app.route('/ping')
def ping():
    return 'OK', 200

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data['question']
    response = ask_gemini(question)
    return jsonify({'answer': response})
    
@app.route('/download/canadian_immigration.csv')
def download_csv():
    return send_from_directory('.', 'canadian_immigration.csv', as_attachment=True)
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
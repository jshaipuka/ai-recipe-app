from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from recipe_llm import get_recipe

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/hello')
def hello():
    print('Hello, World!')
    return 'Hello, World!'

@app.route('/recipe', methods=['POST'])
def recipe():
    user_request = request.data.decode('utf-8')
    print(f"[REQUEST]: {user_request}")

    recipe = get_recipe(user_request)
    print(f"[RESPONSE]: {recipe}")
    return jsonify({ 'query': user_request, 'recipe': recipe })

if __name__ == '__main__':
    app.run()
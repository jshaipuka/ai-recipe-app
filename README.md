# ai-recipe-app
Test playground. Recipes are generated using basic llm capabilities and are purely made up.

App uses Azure Open AI API. You need to create an account and get the API key.

### Setup environment

Create .env from .env.example and fill in the values.

### Running the API locally

On windows:

```bash
cd api
```

```bash
py -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
```

Run api:

```bash
flask run
```

Browse to the API at `http://localhost:5000` in a web browser.


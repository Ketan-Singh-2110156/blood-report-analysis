import pathlib
import textwrap
from flask import Flask, request, jsonify
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import requests
import json
from io import BytesIO
import os
import PIL


genai.configure(api_key=os.environ.get("GENAI_API_KEY"))
model = genai.GenerativeModel('gemini-pro-vision')

app = Flask(__name__)
@app.route('/chat', methods=['GET', 'POST'])
def chat():
  try:
    data = request.json
    if input not in data:
      text = data['input']
    else:
      return jsonify({"error": "No input provided"})
    response = requests.get(text)
    img = PIL.Image.open(BytesIO(response.content))
    response = model.generate_content(["can you return the data of picture in json format with only quantiy and only numeric data and send only within {}", img], stream=True)
    response.resolve()
    result=response.text
    res = json.loads(result)
    return res
  except Exception as e:
    return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
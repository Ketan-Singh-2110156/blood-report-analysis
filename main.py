import pathlib
import textwrap
from flask import Flask, request, jsonify
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import os

genai.configure(api_key=os.environ.get("GENAI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')


app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat():
  try:
    data = request.json
    if input not in data:
      text = data['input']
    else:
      return jsonify({"error": "No input provided"})
    response = model.generate_content(text)
    result = response.text
    return jsonify({"result": result})
  except Exception as e:
    return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
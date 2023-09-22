from flask import Flask, render_template, request, jsonify
import random
import openai
openai.api_key = "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"
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_chat(prompt):
    messages=[{"role":"user","content":prompt},]
    response = openai.ChatCompletion.create(
        messages = messages, 
        model = "gpt-3.5-turbo",
        temperature=0.6
    )
    return response['choices'][0].message.content

def get_image(prompt):
    response = openai.Image.create(
    prompt = "a lady in a professional dress in front of office building",
    n = 1,
    size = "512x512" )
    return response['data'][0]['url']

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.form['text-prompt']
    # Generate text based on prompt
    generated_text = get_chat(prompt)
    return render_template('index.html', generated_text=generated_text)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['image-prompt']
    # Generate image based on prompt
    generated_image = get_image(prompt)
    return render_template('index.html', generated_image=generated_image)

if __name__ == '__main__':
    app.run(debug=True)
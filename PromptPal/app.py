from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_text', methods=['POST'])
def generate_text():
    prompt = request.form['text-prompt']
    # Generate text based on prompt
    generated_text = 'This is a random text.'
    return render_template('index.html', generated_text=generated_text)

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form['image-prompt']
    # Generate image based on prompt
    generated_image = 'https://example.com/random-image.jpg'
    return render_template('index.html', generated_image=generated_image)

if __name__ == '__main__':
    app.run(debug=True)
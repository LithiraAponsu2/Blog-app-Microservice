from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)
BACKEND_URL = f"http://{os.environ.get('BACKEND_HOST', 'localhost')}:5000"

@app.route('/')
def index():
    response = requests.get(f"{BACKEND_URL}/posts")
    posts = response.json()
    return render_template('index.html', posts=posts)

@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    requests.post(f"{BACKEND_URL}/posts", json={'title': title, 'content': content})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
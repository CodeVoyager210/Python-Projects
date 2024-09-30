from flask import Flask, render_template
import requests
app = Flask(__name__)
@app.route('/')
def home():
    url = 'https://api.npoint.io/674f5423f73deab1e9a7'
    posts = requests.get(url=url).json()
    return render_template('index.html',posts = posts)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/<num>')
def post(num):
    url = 'https://api.npoint.io/674f5423f73deab1e9a7'
    posts = requests.get(url=url).json()
    return render_template('post.html',num=int(num),posts=posts)
if __name__ == '__main__':
    app.run()
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=url_blog).json()
    return render_template("index.html",posts = response)
@app.route('/blog/<num>')
def blog_page(num):
    url_blog = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=url_blog).json()
    return render_template("post.html",number = int(num),posts= response)


if __name__ == "__main__":
    app.run(debug=True)

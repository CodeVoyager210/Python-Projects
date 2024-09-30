from flask import Flask, render_template,request
import requests
import smtplib
app = Flask(__name__)
EMAIL = 'athanasopoulos.efth@gmail.com'
PASS = 'fxlansnnhzaylvac'
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
@app.route('/form_sent',methods=['POST'])
def form_submit():
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=EMAIL,password=PASS)
    connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL,msg=f'Subject:Customer Form \n\nEmail: {email} \nPhone: {phone} \nMessage: {message}')
    connection.close()
    return render_template('form.html')
if __name__ == '__main__':
    app.run()
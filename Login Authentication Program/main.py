from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from sqlalchemy.exc import NoResultFound
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
# CREATE DATABASE

login_manager = LoginManager()
login_manager.init_app(app)
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model,UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)
@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect('secrets')
    return render_template("index.html")


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        encrypted_password = generate_password_hash(password,method='pbkdf2',salt_length=8)
        new_user = User(email=email,password=encrypted_password,name=name)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        except NoResultFound:
            flash('That email does not exist,please try again later')
            return redirect(url_for('login'))
        hashed_pass = user.password
        check = check_password_hash(pwhash=hashed_pass,password=password)
        if check:
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Password was incorrect,please try again later')
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    UPLOAD_FOLDER = 'static/files'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return send_from_directory(app.config['UPLOAD_FOLDER'],'cheat_sheet.pdf',as_attachment=True)



if __name__ == "__main__":
    app.run(debug=True)

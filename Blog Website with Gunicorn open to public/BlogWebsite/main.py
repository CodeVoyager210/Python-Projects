from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError,NoResultFound
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column, foreign
from sqlalchemy import Integer, String, Text, ForeignKey
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# Import your forms from the forms.py
from forms import CreatePostForm, RegisterForm, LoginForm,CommentForm
import os
'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('API_KEY')
ckeditor = CKEditor(app)
Bootstrap5(app)
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)
def admin_only(func):
    @wraps(func)
    @login_required
    def wrapper(*args,**kwargs):
        if current_user.id == 1:
            return func(*args, **kwargs)
        else:
            return abort(403,*args,**kwargs)
    return wrapper

# TODO: Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def user_loader(user_id):
    return db.get_or_404(UserTable,user_id)
# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DOMAIN_DATABASE')
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLES
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author = relationship('UserTable',back_populates='posts')
    comments = relationship('Comment',back_populates='blogs')

    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# TODO: Create a User table for all your registered users. 
class UserTable(db.Model,UserMixin):
    __tablename__ = 'users'
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    email : Mapped[str] = mapped_column(unique=True,nullable=False)
    password : Mapped[str] = mapped_column(unique=True,nullable=False)
    name : Mapped[str] = mapped_column(nullable=False)
    posts = relationship('BlogPost',back_populates='author')
    comments = relationship('Comment',back_populates='users')
class Comment(db.Model):
    __tablename__ = 'comment'
    id : Mapped[int] = mapped_column(Integer,primary_key=True)
    text : Mapped[str] = mapped_column(Text,unique=True,nullable=False)
    user_id : Mapped[int] = mapped_column(Integer,db.ForeignKey('users.id'))
    blog_id : Mapped[int] = mapped_column(Integer,db.ForeignKey('blog_posts.id'))
    users = relationship('UserTable',back_populates='comments')
    blogs = relationship('BlogPost',back_populates='comments')
with app.app_context():
    db.create_all()

# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register',methods=['POST','GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        name = form.name.data
        encrypted_pass = generate_password_hash(password,method='pbkdf2',salt_length=5)
        add_user = UserTable(email=email, password=encrypted_pass, name=name)
        db.session.add(add_user)
        try:
            db.session.commit()
        except IntegrityError:
            flash('This email already exists,Login with it instead')
            return redirect(url_for('login'))
        login_user(add_user)
        return redirect(url_for('get_all_posts'))
    return render_template("register.html",form=form)

# TODO: Retrieve a user from the database based on their email. 
@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        try:
            user = db.session.execute(db.select(UserTable).filter_by(email=email)).scalar_one()
        except NoResultFound:
            flash('The email was not found,use register to create an account')
            return redirect(url_for('login'))
        hashed_pass = user.password
        check_pass = check_password_hash(pwhash=hashed_pass,password=password)
        if check_pass:
            login_user(user)
            return redirect(url_for('get_all_posts'))
        else:
            flash('Password was incorrect,try again')
            return redirect(url_for('login'))
    return render_template("login.html",form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


# TODO: Allow logged-in users to comment on posts
@app.route("/post/<int:post_id>",methods=['POST','GET'])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_section = CommentForm()
    if comment_section.validate_on_submit():
        if current_user.is_authenticated:
            comment = comment_section.body.data
            new_comment = Comment(text=comment,users=current_user,blogs=requested_post)
            db.session.add(new_comment)
            db.session.commit()
            return redirect(url_for('show_post',post_id=requested_post.id))
        else:
            flash('You need to login or register to comment')
            return redirect(url_for('login'))
    comments = db.session.execute(db.select(Comment).order_by(Comment.id)).scalars()
    return render_template("post.html", post=requested_post,comment_send=comment_section,comments=comments)


# TODO: Use a decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)



# TODO: Use a decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=current_user,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# TODO: Use a decorator so only an admin user can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=False, port=5002)

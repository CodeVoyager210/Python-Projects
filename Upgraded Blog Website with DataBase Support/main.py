from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from requests import URLRequired
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date, datetime

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()

class edit_form(FlaskForm):
    blog_title = StringField(validators=[DataRequired()],name='Blog Post Title')
    blog_subtitle = StringField(validators=[DataRequired()],name='Subtitle')
    name = StringField(validators=[DataRequired()],name='Your Name')
    blog_img_url = StringField(validators=[URL()],name='Blog Image URL')
    body = CKEditorField(name='Body')
    submit_post = SubmitField(name='Submit Post')

@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    search_posts = db.session.execute(db.select(BlogPost).order_by(BlogPost.id)).scalars()
    posts = [x for x in search_posts]
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).filter_by(id=post_id)).scalar_one()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post',methods=['POST','GET'])
def add_new_post():
    form = edit_form()
    if form.validate_on_submit():
        title = form.blog_title.data
        subtitle = form.blog_subtitle.data
        name = form.name.data
        img  = form.blog_img_url.data
        body = form.body.data
        today_date = datetime.now().strftime('%B %m, %Y')
        new_blog = BlogPost(title=title,subtitle=subtitle,date=today_date,body=body,author=name,img_url=img)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('make-post.html',form=form)
# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>',methods=['GET','POST'])
def edit_post(post_id):
    form = edit_form()
    tp = request.args.get('type')
    search_post = db.session.execute(db.select(BlogPost).filter_by(id=post_id)).scalar_one()
    if form.validate_on_submit():
        search_post.title = form.blog_title.data
        search_post.subtitle = form.blog_subtitle.data
        search_post.author = form.name.data
        search_post.img_url = form.blog_img_url.data
        search_post.body = form.body.data
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    form.blog_title.data = search_post.title
    form.blog_subtitle.data = search_post.subtitle
    form.name.data = search_post.author
    form.blog_img_url.data = search_post.img_url
    form.body.data = search_post.body
    return render_template('make-post.html',type=tp,form=form)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>')
def delete_post(post_id):
    find_blog = db.session.execute(db.select(BlogPost).filter_by(id=post_id)).scalar_one()
    db.session.delete(find_blog)
    db.session.commit()
    return redirect(url_for('get_all_posts'))
# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired, URL,Email,Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8,message='Please enter a password longer than 8 characters')])
    name = StringField('Name',validators=[DataRequired()])
    submit = SubmitField('Register')


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Login')

# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    body = CKEditorField(name='Comment',validators=[DataRequired()])
    submit = SubmitField('SUBMIT COMMENT')
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Integer,String,Float


class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)
book_list = []
class Book(db.Model):
    __tablename__ = 'book'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
with app.app_context():
    db.create_all()
@app.route('/',methods=['GET','POST'])
def home():
    global book_list
    book_list = []
    if request.method == 'POST':
        if request.form.get('rating'):
            with app.app_context():
                book_id = request.form.get('id')
                rating = request.form.get('rating')
                book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
                book_to_update.rating = rating
                db.session.commit()


    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.id))
        all_books = result.scalars()
        for book in all_books:
            template = {
                'id' : book.id,
                'title' : book.title,
                'author' : book.author,
                'rating' : book.rating
            }
            if template not in book_list:
                try:
                    book_list.append(template)
                except UnboundLocalError:
                    continue
    return render_template('index.html',books = book_list)


@app.route("/add")
def add():
    return render_template('add.html')
@app.route('/added',methods=['POST'])
def added():
    name = request.form.get('name')
    author = request.form.get('author')
    rating = request.form.get('rating')
    with app.app_context():
        new_book = Book(title=name, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
    return render_template('added.html')

@app.route('/change')
def change():
    id_num = request.args.get('id')
    return render_template('change.html',id=int(id_num),books=book_list)
@app.route('/delete')
def delete():
    book_id = request.args.get('id')
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.run(debug=True)


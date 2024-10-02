from wsgiref.validate import validator

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired,URL
import csv

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
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
coffee_icons = ['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕']
wifi_icons = ['✘','💪','💪💪','💪💪💪']
power_icons = ['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌']
class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location',validators=[DataRequired(),URL()])
    open = StringField('What time does it open?',validators=[DataRequired()])
    close = StringField('What time does it close?',validators=[DataRequired()])
    coffe_rating = SelectField('Cafe Rating',choices=[(coffee_icons[0],coffee_icons[0]),(coffee_icons[1],coffee_icons[1]),(coffee_icons[2],coffee_icons[2]),(coffee_icons[3],coffee_icons[3]),(coffee_icons[4],coffee_icons[4])])
    wifi_strength = SelectField('Wifi Strength',choices=[(wifi_icons[0],wifi_icons[0]),(wifi_icons[1],wifi_icons[1]),(wifi_icons[2],wifi_icons[2]),(wifi_icons[3],wifi_icons[3])])
    power = SelectField('Power',choices=[(power_icons[0],power_icons[0]),(power_icons[1],power_icons[1]),(power_icons[2],power_icons[2]),(power_icons[3],power_icons[3]),(power_icons[4],power_icons[4])])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv','a',encoding="utf-8") as file:
            file.write(f'\n{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},{form.coffe_rating.data},{form.wifi_strength.data},{form.power.data}')
        return render_template('form.html')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

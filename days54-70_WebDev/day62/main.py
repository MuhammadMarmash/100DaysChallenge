from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps(URL)', validators=[DataRequired(), URL(require_tld=True,
                                                                                                     message='Please '
                                                                                                             'enter a '
                                                                                                             'valid '
                                                                                                             'url')])
    cafe_opening = StringField('Opening Time e-g-8AM', validators=[DataRequired()])
    cafe_closing = StringField('Closing Time e-g-5:30PM', validators=[DataRequired()])
    cafe_rating = StringField('Coffe Rating', validators=[DataRequired()])
    cafe_strength = StringField('Wifi Strength Rating', validators=[DataRequired()])
    cafe_power = StringField('Power Socket Availability', validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:
# add: Location URL, open time, closing time, coffee rating, Wi-Fi rating, power outlet rating fields
# make coffee/Wi-Fi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    form.validate_on_submit()

    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as csv_file:
            data = [form.cafe_name.data, form.cafe_location.data,
                    form.cafe_opening.data, form.cafe_closing.data,
                    form.cafe_rating.data, form.cafe_strength.data,
                    form.cafe_power.data]
            csv_file.write('\n'+",".join(data))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class InformationForm(FlaskForm):
    name = StringField('Name')
    email = StringField('Email')
    submit = SubmitField('Send Request')

@app.route("/", methods=['GET', 'POST'])
def home_page():
    form = InformationForm()

    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        print(f"Received data: Name - {name}, Email - {email}")

    return render_template("home.html", form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

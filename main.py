from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import joblib

app = Flask(__name__)
Bootstrap5(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

model = joblib.load('hoaxhoundmodel')


class NewsForm(FlaskForm):
    news = StringField("Paste in a news article", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/', methods=['GET', 'POST'])
def home():
    form = NewsForm()
    if form.validate_on_submit():
        article = form.news.data
        ans = int(model.predict([article]) == 'REAL')
        return redirect(url_for('answer', ans=ans))
    return render_template('index.html', form=form)


@app.route('/answer/<int:ans>')
def answer(ans):
    return render_template('answer.html', ans=ans)


if __name__ == "__main__":
    app.run(debug=True)

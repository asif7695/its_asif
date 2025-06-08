from flask import Flask, render_template, flash, redirect, request, url_for
from flask_wtf import CSRFProtect
from webforms import ContactForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = "nothing is that secret here"
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)
migrate = Migrate(app,db)


# feedback model 
class Feedback(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(50),nullable=False)
    message = db.Column(db.String(2000),nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
        
    #create a string
    def __repr__(self):
        return '<Name %r>' %self.name
    
    

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/highlights')
def highlights():
    return render_template("highlights.html")


@app.route('/personal')
def personal():
    return render_template("personal.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data
        flash(f'Thank you, {name}! Your message has been received.', 'success')
        feedback = Feedback(name = form.name.data, email = form.email.data, message = form.message.data)
        db.session.add(feedback)
        db.session.commit()
        return redirect(url_for('contact'))
    return render_template("contact.html", form=form)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")


@app.route('/photography')
def photography():
    return render_template("photography.html")

@app.route('/skills')
def skills():
    return render_template("skills.html")


@app.route('/hangman')
def hangman():
    return render_template("hangman.html")



@app.route('/blog_p')
def blog_p():
    return render_template("blog_p.html")


@app.route('/telebot')
def telebot():
    return render_template("telebot.html")

@app.route('/hotel')
def hotel():
    return render_template("hotel.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")






if __name__ == '__main__':
    app.run(debug = True)
 
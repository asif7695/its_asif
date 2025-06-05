from flask import Flask, render_template

app = Flask(__name__)

@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/blog')
def blog():
    return render_template("blog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template("projects.html")

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




if __name__ == '__main__':
    app.run(debug = True)
 
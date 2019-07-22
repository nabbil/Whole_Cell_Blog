from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '12345678910'

posts = [
    {
        'author': 'Nabbil Khan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 3, 2019'

    },
    {
        'author': 'Nadeem Khan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 21, 1994'

    }
]


@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def register():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(port=5001, debug=True)

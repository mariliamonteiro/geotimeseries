from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd5fda74dcf2c2fdbfca06a4ebfc65b86a9e0da08d0115dce61f522f183b156d8'

posts = [
    {
        'author': 'Tiago',
        'title': 'Post',
        'content': 'marilia linda demais',
        'date_posted': '2018-10-01'
    },
    {
        'author': 'Marilia',
        'title': 'Post 2',
        'content': 'c2',
        'date_posted': '2018-10-02'
    }
]

@app.route('/')
@app.route('/home')
def home():    
    return render_template('home.html', posts= posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title= 'Register', form= form)

@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', title= 'Login', form= form)

if __name__ == '__main__':
    app.run(debug= True)

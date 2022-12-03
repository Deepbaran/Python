from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
# from data import Articles
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

# Config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345678'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' # Data will be fetched as a dictionary. By default it is fetched as tuple

# init MySQL
mysql = MySQL(app)

# Articles = Articles()

# Index
@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html')

# About
@app.route('/about')
def about():
    return render_template('about.html')

# Articles
@app.route('/articles')
def articles():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles")
    articles = cur.fetchall()
    cur.close()
    if result > 0:
        return render_template('articles.html', articles=articles) # We are passing the Articles data along with the template name.
    msg = 'No Articles Found'
    return render_template('dashboard.html', msg=msg)

# Single Article
@app.route('/article/<string:id>/') # dynamic value for the route
def article(id):
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles WHERE id = %s", [id])
    article = cur.fetchone()
    cur.close()
    return render_template('article.html', article=article)

# Register Form Class
class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.data_required(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

# User Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        
        # Create cursor
        cur = mysql.connection.cursor()
        # Execute query
        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))
        # Commit to DB
        mysql.connection.commit()
        # Close connection
        cur.close()

        flash('You are now registered and can log in', 'success')
        return redirect(url_for('login')) # route for home.html
    return render_template('register.html', form=form)

# User login - does not use WTForm like register
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = mysql.connection.cursor()
        
        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone() # fetched the first one in result
            password = data['password'] # The MYSQL_CURSORCLASS is making sure we are gettign a dictionary instead of usual tuple
            # Close connection
            cur.close()
            # Compare passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True # No need to pass session to templates. It is accessible throughout the application.
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template("login.html", error=error)
        else:
            error = 'Username not found'
            return render_template("login.html", error=error)
    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# Dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM articles")
    articles = cur.fetchall()
    cur.close()
    if result > 0:
        return render_template('dashboard.html', articles=articles)
    msg = 'No Articles Found'
    return render_template('dashboard.html', msg=msg)

# Article Form Class
class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=200)])
    body = TextAreaField('Username', [validators.Length(min=30)])

# Add Article
@app.route('/add_article', methods=['GET', 'POST'])
@is_logged_in
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        body = form.body.data

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO articles(title, body, author) VALUES(%s, %s, %s)', (title, body, session['username']))
        mysql.connection.commit()
        cur.close()

        flash('Article Created', 'success')

        return redirect(url_for('dashboard'))
    return render_template('add_article.html', form=form)

# Edit Article
@app.route('/edit_article/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_article(id):
    cur = mysql.connection.cursor()
    result = cur.execute('SELECT * FROM articles WHERE id = %s', [id])
    article = cur.fetchone()

    form = ArticleForm(request.form)

    # Populate article form fileds
    form.title.data = article['title']
    form.body.data = article['body']

    if request.method == 'POST' and form.validate():
        title = request.form['title']
        body = request.form['body']

        cur = mysql.connection.cursor()
        cur.execute('UPDATE articles SET title=%s, body=%s WHERE id = %s', (title, body, id))
        mysql.connection.commit()
        cur.close()

        flash('Article Updated', 'success')

        return redirect(url_for('dashboard'))
    return render_template('edit_article.html', form=form)

# Delete Article
@app.route('/delete_article/<string:id>', methods=['POST']) # We do not need a GET request here
@is_logged_in
def delete_article(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM articles WHERE id = %s", [id])
    mysql.connection.commit()
    cur.close()
    
    flash("Article Deleted")
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True) # debug=True will ensure that the server runs in the debug mode and everytime, we make any changes, it gets reflected on the server.

# Flask uses Jinja template engine to create it's templates.
# {% LOGIC %}
# {{ VALUE }
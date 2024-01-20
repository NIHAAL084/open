from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration purposes
users = {'username': 'password'}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            # Authentication successful, redirect to the home page
            return redirect(url_for('home'))
        else:
            # Authentication failed, show login page with an error message
            return render_template('login.html', error='Invalid credentials')

    # If it's a GET request, just render the login page
    return render_template('login.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)

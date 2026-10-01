from flask import Flask, render_template, request, redirect

app = Flask(__name__)

senha = '123'

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.post('/user')
def user():
    req = request.form
    if req['user_passwd'] == senha:
        return render_template('user.html', name=req['user_name'], passwd=req['user_passwd'])
    return f'<script>alert("senha inválida")</script>'

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect
from User import User

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

@app.post('/cadastro')
def user_cadastro():
    r = request.form
    name = r['user_name']
    email = r['user_email']
    passwd = r['user_passwd']

    try:
        new_user = User(name, email, passwd)
        print(new_user.name)
        return render_template('cadastro.html', user=new_user)
    except ValueError as e:
        return f'<h1>{e}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

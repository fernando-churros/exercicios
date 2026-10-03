from flask import Flask, render_template, request, redirect
from User import User
import mariadb
import hashlib

conn_dict = {
    'user': 'root',
    'password': '2357',
    'host': 'localhost',
    'database': 'cadastro'
}

app = Flask(__name__)

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
    try:
        req = request.form
        with mariadb.connect(**conn_dict) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT name, email, passwd FROM users WHERE email = '{req["user_email"]}'")
                info = cursor.fetchone()

        if info is None:
            return '<h1>email ou senha inválidos</h1>'

        name, email, passwd = info[0], info[1], info[2]

        if hashlib.sha256(req['user_passwd'].encode()).hexdigest() == passwd:
            return render_template('user.html', name = name, email = email, passwd = passwd)

        return '<h1>email ou senha inválidos</h1>'
    except Exception as e:
        return f'<h1>{e}</h1>'

@app.post('/cadastro')
def user_cadastro():
    r = request.form
    name = r['user_name']
    email = r['user_email']
    passwd = r['user_passwd']

    try:
        u = User(name, email, passwd)
        with mariadb.connect(**conn_dict) as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"INSERT INTO users (name, email, passwd) values ('{u.name}', '{u.email}', '{u.passwd}')")
                conn.commit()

        return render_template('cadastro.html', user=u)
    except Exception as e:
        return f'<h1>{e}</h1>'


if __name__ == '__main__':
    app.run(debug=True)

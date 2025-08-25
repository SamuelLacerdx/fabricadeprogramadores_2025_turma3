from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        print(username)
        password = request.form.get('password')
        print(password)
        return f"<h1>BEM vindo: {username}"
    
    else: 
        return render_template('index.html')

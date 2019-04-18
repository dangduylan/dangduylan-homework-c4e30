from flask import Flask, render_template, request
app = Flask(__name__)
accounts = [
    {
    'username':'dangduylan',
    'password':'khongbiet123'
},
    {
    'username':'landangduy',
    'password':'vankhongbiet'
    }]

@app.route('/',methods = ["POST"])
def login():
    for user in accounts:
        if request.form.get('username') == user['username'] and request.form.get('password') == user['password']:
           return 'Login Successful!'
        else:
            return 'Login Failed!'
@app.route('/')
def get():  
    return render_template('users.html')
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
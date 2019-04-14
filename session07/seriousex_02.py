from flask import Flask, render_template
import jinja2
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    users = {
        'lan':{
                'name': 'Dang Duy Lan',
                'age': 24,
                'gender': 'male',
                'hobbies': 'game, music'
                },
        'hung':{
                'name': 'Vu Manh Hung',
                'age': 24,
                'gender': 'male',
                'hobbies': 'music, technology'
                }
    }
    for i in users:
        if username in users:
            return render_template('users.html', data=users[username])
        else:
            return 'User not found'

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/school')
def school():
    return redirect('https://mindx.edu.vn/')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 
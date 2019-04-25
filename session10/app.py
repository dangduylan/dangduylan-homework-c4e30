from flask import Flask, render_template, request
from db import add_bike, get_bike
app = Flask(__name__)

@app.route('/new_bike')
def get_newbike():
    return render_template('new_bike.html')

@app.route('/new_bike', methods=['POST'])
def post_newbike():

    model = request.form.get('model')
    daily_fee = request.form.get('daily_fee')
    image = request.form.get('image')
    year = request.form.get('year')
    add_bike(model,daily_fee,image,year)

    print(get_bike())

    return render_template('new_bike.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
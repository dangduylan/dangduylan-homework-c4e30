from flask import Flask, render_template
app = Flask(__name__)

#without_template
# @app.route('/bmi/<weight>/<height>')
# def bmi(weight,height):
#     bmi = int(weight)/((int(height)/100)**2)
#     if bmi < 16:
#         return 'You are severely underweight'
#     elif 16 <= bmi < 18.5:
#         return 'You are underweight'
#     elif 18.5 <= bmi < 25:
#         return 'You are normal'
#     elif 25 <= bmi < 30:
#         return 'You are overweight'
#     else:
#         return 'You are obese'


#with_template
@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    your_body = {
        'weight': int(weight),
        'height': int(height),
        'bmi': int(weight)/((int(height)/100)**2)
    }
    if your_body['bmi'] < 16:
        your_body['condition']='You are severely underweight'
    elif 16 <= your_body['bmi'] < 18.5:
        your_body['condition']='You are underweight'
    elif 18.5 <= your_body['bmi'] < 25:
        your_body['condition']='You are normal'
    elif 25 <= your_body['bmi'] < 30:
        your_body['condition']='You are overweight'
    else:
        your_body['condition']='You are obese'
    return render_template('bmi.html',data=your_body)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 
from flask import Flask, render_template, request
from tracking import fetch_status

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        tracking_number = request.form.get('tracking_number', '')
        result = fetch_status(tracking_number)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

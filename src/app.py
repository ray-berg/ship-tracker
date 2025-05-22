from flask import Flask, render_template, request
from tracking import fetch_status

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        tracking_number = request.form.get('tracking_number', '')
        result = fetch_status(tracking_number)
        if result is None:
            error = 'Courier could not be detected.'
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

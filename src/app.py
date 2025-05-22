from flask import Flask, render_template, request
from tracking import fetch_status, parse_tracking_numbers, get_courier_link

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    results = []
    errors = []
    if request.method == 'POST':
        numbers_raw = request.form.get('tracking_numbers', '')
        numbers = parse_tracking_numbers(numbers_raw)
        for number in numbers:
            info = fetch_status(number)
            if info is None:
                errors.append(f"Courier could not be detected for {number}.")
            else:
                link = get_courier_link(info.courier, number)
                results.append({'number': number, 'courier': info.courier, 'link': link})
    return render_template('index.html', results=results, errors=errors)

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

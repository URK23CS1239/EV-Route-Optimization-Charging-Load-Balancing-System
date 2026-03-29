from flask import Flask, request, render_template
from logic import select_best_station, update_station

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', result="", best_station="")

@app.route('/route', methods=['POST'])
def route():
    start = request.form['start']
    end = request.form['end']
    battery = int(request.form['battery'])

    best = None

    if battery < 30:
        best = select_best_station()
        update_station(best)
        result = f"⚡ Route: {start} → {best['name']} → {end}"
        best_station = best['name']
    else:
        result = f"✅ Route: {start} → {end}"
        best_station = ""

    return render_template('index.html',
        result=result,
        best_station=best_station
    )

if __name__ == '__main__':
    app.run(debug=True)
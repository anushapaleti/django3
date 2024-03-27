from os import name

from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)
API_KEY = '6f329cb4617cdebb502f7ae74c50fac4'

@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = ('delhi')

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    try:
        response = urllib.request.urlopen(url)
        data = json.load(response)

        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15

        weather_data = {
            "city": data['name'],
            "country_code": data['sys']['country'],
            "temp_cell": f"{temperature_celsius:.2f}°C",
            "humidity": data['main']['humidity'],
        }

        return render_template('w2.html', data=weather_data)

    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return render_template('error.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
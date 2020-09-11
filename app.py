from flask import Flask, render_template,request,redirect
import requests
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def weather():
    if request.method == 'POST':
        cityName = request.form['city']

        apiKey = "b34666af0b4c73b31515c68b4e2f7cea"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&units=imperial&appid={apiKey}"

        try:
            r = requests.get(url).json()

            weatherData ={
                'user':cityName,
                'city':r['name'],
                'temperature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon']
            }

            return render_template('message.html',weather=weatherData)
        
        except:
            return render_template('error.html',city=cityName)
    else:
        return render_template('weather.html')

if __name__ == '__main__':
    app.run()
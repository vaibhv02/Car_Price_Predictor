from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
car = pd.read_csv("Cleaned Car.csv")

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = {}
    for company in companies:
        models = sorted(car[car['company'] == company]['name'].unique())
        car_models[company] = models
    years = sorted(car['year'].unique())
    fuel_types = sorted(car['fuel_type'].unique())

    return render_template('index.html', companies=companies, car_models=car_models, years=years, fuel_types=fuel_types)

if __name__ == "__main__":
    app.run(debug=True)

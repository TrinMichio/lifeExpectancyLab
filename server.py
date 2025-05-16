# flask --app data_server run
from flask import Flask
from flask import render_template, request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("data/life_expectancy_cleaned.json", "r")
    data = json.load(f)
    f.close()
    years = list(data['United States'].keys())
    years = years[:-2]
    usval = list(data['United States'].values())
    mexval = list(data['Mexico'].values())
    canval = list(data['Canada'].values())
    
    avg = [(float(usval[i])+float(mexval[i])+float(canval[i]))/3 for i in range(len(usval))]
    return render_template('index.html', years = years, data = data, avg = avg)

@app.route('/year')
def year():
    f = open("data/life_expectancy_cleaned.json", "r")
    data = json.load(f)
    f.close()
    regions = {
        "AB": "Alberta",
        "AK": "Alaska",
        "AL": "Alabama",
        "AR": "Arkansas",
        "AZ": "Arizona",
        "BC": "British Columbia",
        "CA": "California",
        "CO": "Colorado",
        "CT": "Connecticut",
        "DC": "District Of Columbia",
        "DE": "Delaware",
        "FL": "Florida",
        "GA": "Georgia",
        "GU": "Guam",
        "HI": "Hawaii",
        "IA": "Iowa",
        "ID": "Idaho",
        "IL": "Illinois",
        "IN": "Indiana",
        "KS": "Kansas",
        "KY": "Kentucky",
        "LA": "Louisiana",
        "MA": "Massachusetts",
        "MB": "Manitoba",
        "MD": "Maryland",
        "ME": "Maine",
        "MI": "Michigan",
        "MN": "Minnesota",
        "MO": "Missouri",
        "MS": "Mississippi",
        "MT": "Montana",
        "Mexico": "Mexico",
        "NB": "New Brunswick",
        "NC": "North Carolina",
        "ND": "North Dakota",
        "NE": "Nebraska",
        "NF": "Newfoundland",
        "NH": "New Hampshire",
        "NJ": "New Jersey",
        "NM": "New Mexico",
        "NS": "Nova Scotia",
        "NT": "Northwest Territories",
        "NU": "Nunavut",
        "NV": "Nevada",
        "NY": "New York",
        "OH": "Ohio",
        "OK": "Oklahoma",
        "ON": "Ontario",
        "OR": "Oregon",
        "PA": "Pennsylvania",
        "PE": "Prince Edwards Island",
        "PR": "Puerto Rico",
        "QC": "Quebec",
        "RI": "Rhode Island",
        "SC": "South Carolina",
        "SD": "South Dakota",
        "SK": "Saskatchewan",
        "TN": "Tennessee",
        "TX": "Texas",
        "UT": "Utah",
        "VA": "Virginia",
        "VI": "Virgin Islands",
        "VT": "Vermont",
        "WA": "Washington",
        "WI": "Wisconsin",
        "WV": "West Virginia",
        "WY": "Wyoming",
        "YT": "Yukon"
    }
    year = request.args.get("year")
    ageMex = float(data["Mexico"][year])
    ageUS = float(data["United States"][year])
    ageCan = float(data["Canada"][year])
    ageMax = max(ageMex, ageUS, ageCan)
    ageMin= min(ageMex, ageUS, ageCan)

    mexico_saturation = (ageMex - ageMin)/(ageMax - ageMin) * 100
    canada_saturation = (ageCan - ageMin)/(ageMax - ageMin) * 100 
    us_saturation = (ageUS - ageMin)/(ageMax - ageMin) * 100 
    print(ageMin)
    print(ageMax)
    
    return render_template('year.html', year=year, ids=list(regions.values()), ageMex=ageMex, ageUS=ageUS, ageCan=ageCan, ageMax=ageMax, ageMin=ageMin, mexico_saturation=mexico_saturation, canada_saturation=canada_saturation, us_saturation=us_saturation)

app.run(debug=True)

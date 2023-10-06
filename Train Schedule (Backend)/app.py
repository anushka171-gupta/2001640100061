from flask import Flask, render_template , request, jsonify
import requests
from datetime import datetime, time
import math
from flask_cors import CORS

app = Flask(__name__) 
cors = CORS(app)

app.config['DEBUG'] = True 

@app.route('/send_data_to_external_api')
def send_data_to_external_api():
    api_endpoint = 'http://20.244.56.144/train/auth'

    try:
        data = {
            "companyName": "Train Central",
            "clientID": "512aa727-92db-4820-acb9-c1e666c08915",
            "ownerName": "Anushka Gupta",
            "ownerEmail": "anushka171.gupta@gmail.com",
            "rollNo": "2001640100061",
            "clientSecret": "dEktBDrWMYZTPdmD"
        }

        response = requests.post(api_endpoint, json=data)

        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            return 'Error: Failed to send data to the API', response.status_code
    except Exception as e:
        return f'Error: {str(e)}', 500
    

@app.route('/')
def home():
    return "hello world"

@app.route('/allTrains')
def get_trains_list():
    api_endpoint = 'http://20.244.56.144/train/trains'
    auth_token = send_data_to_external_api()["access_token"]

    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        response = requests.get(api_endpoint, headers=headers)
        if response.status_code == 200:
            filtered_train_list = get_filtered_train_list(response.json())
            # print(filtered_train_list)
            sorted_train_list = get_sorted_train_list(filtered_train_list)
            print("\n\n", len(sorted_train_list), "\n\n")
            print(sorted_train_list)
            return list(sorted_train_list), 200
        else:
            return 'Error: Failed to fetch data from the API', response.status_code
    except Exception as e:
        return f'Error: {str(e)}', 500
    
@app.route('/train/<train_number>', )
def get_train(train_number):

    print(train_number)

    api_endpoint = 'http://20.244.56.144/train/trains/' + str(train_number)
    auth_token = send_data_to_external_api()["access_token"]

    print(api_endpoint)
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }

    try:
        response = requests.get(api_endpoint, headers=headers)
        # print(response)
        if response.status_code == 200:
            return response.json(), 200
        else:
            return 'Error: Failed to fetch data from the API', response.status_code
    except Exception as e:
        return f'Error: {str(e)}', 500
    

def custom_sort_key(item):
    departureTime = item['departureTime']["Hours"] * 60 + item['departureTime']["Minutes"]
    seatsAvailable = item['seatsAvailable']['AC'] + item['seatsAvailable']['sleeper']
    price = item['price']['AC'] = item['price']['sleeper']
    return (price, -seatsAvailable, -departureTime)

def get_sorted_train_list(train_list):
    train_list = sorted(train_list, key = custom_sort_key)
    return train_list

def custom_filter(item):

    # Define two time objects
    time1 = datetime.strptime(str(time(item['departureTime']["Hours"], item['departureTime']["Minutes"], item['departureTime']["Seconds"])), "%H:%M:%S")

    current_datetime = datetime.now()

    time2 = datetime.strptime(str(time(current_datetime.hour, current_datetime.minute, current_datetime.second)), "%H:%M:%S")

    time_difference = (time1 - time2).total_seconds() / 60

    return time_difference > 30

def get_filtered_train_list(train_list):
    l = filter(custom_filter, train_list)
    return list(l)

if __name__ == "__main__":
    app.run()
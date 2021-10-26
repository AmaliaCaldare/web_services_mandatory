from bottle import run, post, request
import json
import csv
import requests

@post("/number")
def get_number():
    data = json.load(request.body)
    print("Received number: ", data['data'])
    number = data['data']*3
    print("Sending number: ", number)
    
    with open('number.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([number])

    files = {'file': ('number.csv', open('number.csv', 'rb'), 'text/csv')}
    response = requests.post('http://127.0.0.1:3333/new-number', files=files)
    if response.status_code == 200:
        print("Successfully sent csv file to port 3333")

run(host="127.0.0.1", port=7777, debug=True, reloader=True, server="paste")
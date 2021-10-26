import requests

while True:
    number = input("Enter number: ")
    xml = """<?xml version='1.0' encoding='utf-8'?>
    <data>{number}</data>""".format(number=number)
    headers = {'Content-Type': 'application/xml'} 
    print("Sending number in xml", xml)
    try:
      result1 = requests.post('http://127.0.0.1:3333/send-number', headers=headers, data=xml)
      if result1.status_code == 200:
        print("Successfully sent number to port 3333")
      result2 = requests.get('http://127.0.0.1:3333/get-new-number')
      if result2.status_code == 200:
        print("Successfully received number from port 3333")
        print(result2.text)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
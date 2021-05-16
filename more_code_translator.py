import requests, json

url = "https://gsamuel-morse-code-v1.p.rapidapi.com/"

fromw = input("Do you want to translate to morse code or text\n")
trans = input("Type what you want to be translated\nNote: It should be morse code or plain text\n")

if fromw == "text":
    payload = {
        "code": trans
    }
else:
    payload = {
        "text": trans
    }

headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "GET KEY FROM RAPIDAPI",
    'x-rapidapi-host': "gsamuel-morse-code-v1.p.rapidapi.com"
    }

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

if fromw == "text":
    print(response.json()['text'])
else:
    print(response.json()['code'])
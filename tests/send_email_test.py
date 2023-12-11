import requests

url = 'http://127.0.0.1:5000/send'
data = {
    'sender': 'example@example.com',
    'recipient': 'recipient@example.com',
    'subject': 'Test Subject',
    'body': 'This is the body of the email.'
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

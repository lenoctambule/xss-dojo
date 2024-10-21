from flask import Flask,\
                    render_template,\
                    request
import threading
from selenium import webdriver
import time
from requests.utils import requote_uri

def bot_routine(driver : webdriver.Firefox):
    global links
    global lock
    while True :
        lock.acquire()
        if len(links) != 0 :
            target = links.pop()
            lock.release()
            try:
                driver.get(target)
                driver.add_cookie(SECRET_COOKIE)
                driver.refresh()
            except :
                pass
            continue
        lock.release()
        time.sleep(0.5)

SECRET_COOKIE   = {'name' : 'secret', 'value' : 'secret squirrel\'s cookie'}
BASE_URL        = 'http://vulnerable_app:5000/'
links           = list()
lock            = threading.Lock()
app             = Flask(__name__)
options         = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver          = webdriver.Firefox(options=options)
bot_thread      = threading.Thread(target=bot_routine, args=[driver])
bot_thread.start()

@app.route("/")
def bot_control():
    global lock
    value = request.args.get("value", None)
    if value :
        if not value.startswith(BASE_URL) :
            return render_template("bot.html")
        # value = requote_uri(value)
        lock.acquire()
        links.append(value)
        lock.release()
    return render_template("bot.html", value=value)

if __name__ == '__main__':
    port = int(5001)
    app.run(host='0.0.0.0', port=port)
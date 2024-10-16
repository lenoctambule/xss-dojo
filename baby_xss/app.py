from flask import Flask,\
                    render_template,\
                    request

app = Flask(__name__)

@app.route("/")
def main():
    value = request.args.get("value", None)
    return render_template("app.html", value=value)

@app.route("/bot")
def bot_control():
    value = request.args.get("value", None)
    return render_template("bot.html", value=value)
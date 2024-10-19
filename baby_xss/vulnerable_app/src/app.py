from flask import Flask,\
                    render_template,\
                    request

app         = Flask(__name__)

@app.route("/")
def main():
    value = request.args.get("value", None)
    return render_template("app.html", value=value)

if __name__ == '__main__':
    port = int(5000)
    app.run(host='0.0.0.0', port=port)
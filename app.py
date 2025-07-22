from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat")
def chat():
    tipo = request.args.get("terapia", "humanista")
    return render_template("chat.html", tipo=tipo)

@app.route("/terminos")
def terminos():
    return render_template("terminos.html")

@app.route("/privacidad")
def privacidad():
    return render_template("privacidad.html")

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5123)

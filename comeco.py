from flask import Flask
app= Flask(__name__)
@app.route("/")
def index():
    return "Pau no cu do mundo!:)"

@app.route("/<string:name>")

def pao(name):
    name = name.capitalize()
    return f"<h1>eae,{name}</h1>"

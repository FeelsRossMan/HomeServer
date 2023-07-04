from flask import Flask

app = Flask(__name__)
app.run(debug=True, port=5000, host='0.0.0.0')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
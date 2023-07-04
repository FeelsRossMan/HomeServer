from flask import Flask
import change_txt
import get_number_from_txt


app = Flask(__name__)

@app.route("/")
def hello_world():
    count = get_number_from_txt.get_number_from_txt()
    html = """
    <p> Current count is: {count} </p>
    """.format(count = count)
    return html

@app.route("/add")
def add_one():
    change_txt.change_txt()
    return "<p> adding </p>"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')
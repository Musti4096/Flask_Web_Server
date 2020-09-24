#Import Flask modules
from flask import Flask, redirect, url_for, render_template
#Create an object named app 
app = Flask(__name__)


@app.route("/")
def head():
    return render_template("index.html")

if __name__ == '__main__':
    #app.run(debug = True)
    app.run(host="0.0.0.0", port=80)
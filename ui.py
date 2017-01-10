import sqlite3, flask
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  #get the recipes and give them to template
  return flask.render_template('index.html')

if __name__ == "__main__":
  app.debug = True
  app.run(host='0.0.0.0', port=8080)
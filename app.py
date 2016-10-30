from flask import Flask
from flask import jsonify
import csv
import datetime

app = Flask(__name__)

@app.route('/')
def index():
  with open("/var/opt/dylos/data.txt", "r") as csv_f:
    data = csv.DictReader(csv_f, fieldnames=['timestamp', 'small', 'large'], delimiter=',')
    list = []
    for row in data:
      list.append(row)
    res = jsonify(list)
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0')

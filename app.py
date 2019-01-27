from flask import Flask
from flask import render_template as rt
from flask import request, jsonify
import json, requests, re
import parser

#from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


@app.route('/')
def run_index():
    return rt('index.html')


@app.route('/receiver', methods=['POST'])

def pusher():
    readydict = parser.readydict
    namedlist = parser.namedlist
    names = parser.names

    data = request.json

    idx = int(data[0])
    if 0 <= idx < 30:
        result = readydict[names[idx]] + tempchecker(namedlist, idx) + windchecker(namedlist, idx) \
                 + presschecker(namedlist, idx)
    else:
        result = ["No Data"]

    result = jsonify(result)
    return result

# searching temp for namedlist
def tempchecker(array, index):
    celcresult = re.search(r"(F\s[(])(.*)(\sC[)])", array[index])
    if celcresult == None:
        return ["No data about temperature"]
    elif float(celcresult.group(2)) <= 0:
        return ['WARNING: cold weather']
    else:
        return ["Typical temperature"]


# searching wind for namedlist
def windchecker(array, index):
    mphresult = re.search(r"(at\s)(.*)(\sMPH)", array[index])
    if mphresult == None:
        return ["No data about wind"]
    else:
        try:
            float(mphresult.group(2))
        except ValueError:
            anothermphresult = re.search(r"(at\s)(.*)(\s............g)", array[index])
            if float(anothermphresult.group(2)) >= 20:
                return ['WARNING: Storm']
            else:
                return ["Sight wind"]
        else:
            if float(mphresult.group(2)) >= 20:
                return ['WARNING: Storm']
            else:
                return ["Sight wind"]


# searching pressure
def presschecker(array, index):
    hparesult = re.search(r"(Hg\s[(])(.*)(\shPa[)])", array[index])
    if hparesult == None:
        return ["No data about atmosphere pressure"]
    elif float(hparesult.group(2)) >= 1016:
        return ['WARNING: high atmosphere pressure']
    else:
        return ["Normal atmosphere pressure"]


if __name__ == '__main__':
    app.run('127.0.0.1', port=4096)

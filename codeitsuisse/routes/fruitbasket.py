import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/fruitbasket', methods=['POST'])
def evaluateFruit():
    dataByteString = request.get_data()
    dataString = dataByteString.decode('utf-8')
    data = json.loads(dataString)
    logging.info("data sent for evaluation {}".format(data))

    weights = {
        "maApple" : 17,
        "maAvocado" : 28,
        "maPineapple" : 57,
        "maPomegranate" : 11,
        "maRamubutan" : 13,
        "maWatermelon" : 130
    }

    result = 0

    for x in data:
        result += data[x] * weights[x]

    logging.info("My result :{}".format(result))
    return json.dumps(result);

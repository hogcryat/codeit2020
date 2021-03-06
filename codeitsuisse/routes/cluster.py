import logging
import json
from queue import Queue

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)

@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))

    M = len(data[0])
    N = len(data)

    ans = 0
    if 3 <= M <= 1000 and 3 <= N <= 1000:
        read = [[False for j in range(M)] for i in range(N)]


        def search(i, j):
            q = Queue()
            q.put([i, j])
            read[i][j] = True
            while not q.empty():
                y, x = q.get()
                for i1 in range(-1, 2):
                    for j1 in range(-1, 2):
                        if i1 == 0 and j1 == 0:
                            continue
                        inew = y + i1
                        jnew = x + j1
                        if 0 <= inew < N and 0 <= jnew < M and data[inew][jnew].isnumeric() and not read[inew][jnew]:
                            q.put([inew, jnew])
                            read[inew][jnew] = True


        for i, row in enumerate(data):
            for j, unit in enumerate(row):
                if unit == "1" and not read[i][j]:
                    search(i, j)
                    ans += 1

    logging.info("My result :{}".format(ans))
    return json.dumps({"answer": ans});




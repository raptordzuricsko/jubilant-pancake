from flask import Flask, jsonify, request
import unittest
app = Flask(__name__)

@app.route("/")
def hello():
    val1 = request.args.get('val1')
    val2 = request.args.get('val2')
    result = computeDistance(val1, val2)
    response = jsonify({'result':result})
    # for a code test, just let cors through. 
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def computeDistance(val1, val2):
    #to be returned
    opCount = 0

    #turn strings into lists of characters to be worked with
    val1List = list(val1)
    val2List = list(val2)

    #the for loop below is a bit easier when you know which is bigger
    biggerList = val2List
    smallerList = val1List
    if len(val1List) > len(val2List):
        biggerList = val1List
        smallerList = val2List

    for i in range(len(smallerList)):
        if i < len(biggerList):
            if smallerList[i] != biggerList[i]:
                opCount += 1
    opCount += (len(biggerList) - len(smallerList))
    return opCount


class TestStringMethod(unittest.TestCase):
    def test_test(self):
        self.assertEqual(computeDistance("test","test"), 0)
        self.assertEqual(computeDistance("",""), 0)
        self.assertEqual(computeDistance("12345","123456"), 1)
        self.assertEqual(computeDistance("123456","12345"), 1)

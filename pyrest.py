# A significant amount of the code was taken from this website:
# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
# Most of the consumer() function below was taken from this site:
# https://www.programiz.com/python-programming/examples/fibonacci-sequence
# This will only be available on the 127.0.0.1 IP address from the server it is running on.
# You could change 127.0.0.1 to 0.0.0.0. Then it would be available to external web taffic, but this is not a secure way of doing it.

import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
defaultdat = [
    { 'val1': 100,
      'val2': 200,
      'val3': 300},
    { 'val1': 111,
      'val2': 222,
      'val3': 333},
    { 'val1': 1,
      'val2': 2,
      'val3': 3}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>A RESTful API Program Powered by Flask and Python</h1>
<p>This is a basic API for displaying the Fibonacci sequence based on an integer value provided through a POST.</p>'''


# A route to return the default values.
@app.route('/api/v1/resources/defaultdat/all', methods=['GET'])
def api_all():
    return jsonify(defaultdat)

@app.route('/api/v1/resources/fibonacci', methods=['GET', 'POST'])
def consumer():
    data = "You did not enter an integer.  Please only enter integers greater than 1."
    n1 = 0
    n2 = 1
    count = 0
    builder = [0]
    if request.method == 'POST':
        stest = str(request.form['InputValue'][1:-1])
        if (stest[0] == '-'):
          stest = stest[1:len(stest)]
        justnum = stest.isnumeric()
        if(justnum):
          nterms = int(request.form['InputValue'][1:-1])
          if nterms <= 0:
             count = "Please enter a positive integer"
             print("Please enter a positive integer")
          elif nterms == 1:
             print("Fibonacci sequence up to",nterms,":")
             print(n1)
             count = str(count) + ", " + str(n1)
          else:
             print("Fibonacci sequence:")
             while count < nterms:
                 nth = n1 + n2
                 # update values
                 n1 = n2
                 n2 = nth
                 count += 1

                 builder.append(str(n1))

          builder = str(builder)
          if len(builder) > 1:
              data = '''
The Fibonacci sequence for the number you entered is ''' + builder[0:-1] + "]" + '''
                                                                       '''
          else:
            data = "  \
Please enter an integer higher than 1.                   \
                          "
        return data

app.run(host="127.0.0.1", port="5050")

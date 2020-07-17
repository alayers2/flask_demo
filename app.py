import random

from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    """
    This is about as basic as a request can get. Here we're saying that at the route '/' we'll accept requests, and
    return the text 'Hello World'.
    """
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


@app.route('/greeting', methods=['GET'])
def hello_name():
    """
    This request demonstrates how to access values passed in as query parameters in a GET request, for example:
    curl http://localhost:5000/greeting?name=Andy
    will return 'Hello Andy'
    """
    name = request.args.get('name')
    return f'Hello {name}!'


@app.route('/recommendations/<crop>/<nutrient>', methods=['GET'])
def hello_url_path_elements(nutrient, crop):
    """
    This method demonstrates how we can use segments of the url to provide input to the method as well
    curl http://localhost:5000/recommendations/corn/nitrogen
    """
    return f'The recommended amount of {nutrient} for {crop} is {random.randint(1, 100)}.'


@app.route('/recommendations', methods=['POST'])
def recommendations_post():
    """
    This method shows how we can pull data out of the body of a post request. We don't have anything attached to
    this app to persist data, but if we did, you can imagine that this method would be used to insert a new
    recommendation of some sort into a database.
    curl -d '{"crop":"soybeans", "nutrient":"sulfur"}' -H "Content-Type: application/json" -X POST http://localhost:5000/recommendations
    """
    # We can get the body of the post request here, and parse it as json
    data = request.json
    return f"We would have saved a record here for {data['crop']} and {data['nutrient']}."


if __name__ == '__main__':
    app.run()

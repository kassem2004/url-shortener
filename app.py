from flask import Flask, render_template, request
from flask_restful import Api, Resource
import random, string

app = Flask(__name__)
api = Api(app)

@app.route('/')
def Home():
    return render_template('index.html')

url_mapping = {}

def shorten_url():
    return "https://gde.ly/" + ''.join(random.choices(string.ascii_letters, k = 7))

class Shorten_URL(Resource):
    def get(self):
        url = request.args.get('url_input')
        shortened_url = shorten_url()
        return {"original" : url, "shortened": shortened_url}

api.add_resource(Shorten_URL, "/url_shortener")

if __name__ == '__main__':
    app.run(debug=True)

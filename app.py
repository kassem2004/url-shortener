from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource
import random, string

app = Flask(__name__)
api = Api(app)

@app.route('/')
def Home():
    return render_template('index.html')

url_mapping = {}

def shorten_url():
    return "https://gde.ly/" + ''.join(random.choices(string.ascii_letters, k=7))

# just for testing
@app.route('/view_mappings')
def view_mappings():
    return jsonify(url_mapping)

class Shorten_URL(Resource):
    def post(self): #handle post request at /url_shortener endpoint
        data = request.get_json()  
        url = data.get('url_input')

        shortened_url = shorten_url()
        url_mapping[url] = shortened_url
        return jsonify({
            "original_url": url,
            "shortened_url": shortened_url
        })

api.add_resource(Shorten_URL, "/url_shortener")

if __name__ == '__main__':
    app.run(debug=True)

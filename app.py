from flask import Flask, render_template, request, jsonify, redirect
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as db
import random, string
import os

password = os.getenv('SQL_PASS')

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost:3306/url_shortener_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Urls(db.Model):
    __tablename__ = "url_data"
    url_ID = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    shortened_url = db.Column(db.String(100), unique=True, nullable=False)
    click_count = db.Column(db.Integer, default=0)

@app.route('/')
def Home():
    return render_template('index.html')

url_mapping = {}

def shorten_url():
    return ''.join(random.choices(string.ascii_letters, k=7))

# just for testing
@app.route('/view_mappings')
def view_mappings():
    return jsonify(url_mapping)

class Shorten_URL(Resource):
    def post(self): #handle post request at /url_shortener endpoint
        data = request.get_json()  
        url = data.get('url_input')

        shortened_url = shorten_url()
        
        new_mapping = Urls(original_url=url, shortened_url=shortened_url)
        db.session.add(new_mapping)
        db.session.commit()

        return jsonify({
            "original_url": url,
            "shortened_url": f"https://gde.ly/{shortened_url}"
        })
    
class URL_Redirect(Resource):
    def get(self, shortened_url):
        url = Urls.query.filter_by(shortened_url=shortened_url).first()
        url.click_count += 1
        db.session.commit()
        return redirect(url.original_url)

api.add_resource(Shorten_URL, "/url_shortener")
api.add_resource(URL_Redirect, "/gde.ly/<shortened_url>")

if __name__ == '__main__':
    app.run(debug=True)

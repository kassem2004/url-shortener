from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template("index.html")

if __name__ == ("__main__"):
    app.run(debug=True)
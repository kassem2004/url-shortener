from flask import request, jsonify, redirect
from flask_restful import Api, Resource
from app import app, db
from models import URL
import random
import string

api = Api(app)

def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

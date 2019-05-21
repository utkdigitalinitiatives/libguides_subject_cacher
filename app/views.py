from app import app
import os
from flask import jsonify
import json

api_key = os.environ['api-key']


@app.route('/<page>', methods=['GET'])
def route_subject(page):
    x = open(f'app/templates/{page}', 'r')
    return jsonify(json.loads(x.read()))


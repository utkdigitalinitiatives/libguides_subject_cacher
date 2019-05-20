from app import app
import os
from flask import jsonify, render_template

api_key = os.environ['api-key']


@app.route('/<page>', methods=['GET'])
def route_subject(page):
    return render_template(jsonify(page))

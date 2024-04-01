#!/usr/bin/python3
'''api status'''

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def api_status():
    '''JSON Responses'''
    response = {'status': "OK"}
    return jsonify(response)

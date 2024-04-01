#!/usr/bin/python3
'''api status'''

from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    '''JSON Responses'''
    response = {'status': "OK"}
    return jsonify(response)
    
@app_views.route('/status')
def get_stats():
     '''JSON Responses'''
     stats = {
     'amenities': storage.count('Amenity'),
     'cities': storage.count('City'),
     'places': storage.count('Place'),
     'reviews': storage.count('Review'),
     'states': storage.count('State'),
     'users': storage.count('User),
     }
     
     return jsonify(stats)

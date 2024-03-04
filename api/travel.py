from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from model.travel import Travel  # Import the Travel model
from __init__ import db

# Create a Blueprint for the travel API
travel_api = Blueprint('travel_api', __name__, url_prefix='/api/travel')

# Create the API instance
api = Api(travel_api)

class TravelAPI:
    class Create(Resource):
        def post(self):
            # Get request JSON data
            body = request.get_json()

            # Extract travel information
            destination = body.get('destination')
            language = body.get('language')
            time_zone = body.get('time_zone')
            weather = body.get('weather')

            # Create a new travel object
            travel_obj = Travel(destination=destination, language=language, time_zone=time_zone, weather=weather)

            # Add travel destination to database
            travel = travel_obj.create()

            # Return the JSON response of the created travel destination
            if travel:
                return jsonify(travel.read())
            else:
                return {'message': 'Failed to create travel destination.'}, 400

    class Read(Resource):
        def get(self):
            # Retrieve all travel destinations from the database
            travels = Travel.query.all()

            # Convert travel destinations to JSON-ready format
            json_ready = [travel.to_dict() for travel in travels]

            # Return the JSON response
            return jsonify(json_ready)

# Building REST API resources/interfaces, these routes are added to the Web Server
api.add_resource(TravelAPI.Create, '/create')
api.add_resource(TravelAPI.Read, '/')

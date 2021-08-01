from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
import sys
import flask

from dataset_builder import*

flask_app = Flask(__name__)
app = Api(
    app=flask_app,
    version="1.0",
    title="Magma",
    description="automatically build datasets using web search"
)

name_space = app.namespace('builder', description="search and fetch dataset items")

builder = app.model('Dataset Parameters',
                    {
                        'datasetName': fields.String(required=True, description="name"),
                        'datasetType': fields.String(required=True, description="choose one among types: Image, Video, Audio or Text"),
                        'datasetClasses': fields.List(fields.String)(required=True, description="list of class names"),
                        'datasetClassSize': fields.Integer(required=True, description="how many samples per class"),
                    }
)

@name_space.route("/")

class MainClass(Resource):
    def options(self):
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "*")
        response.headers.add("Access-Control-Allow-Methods", "*")
        return response
    
    @app.expect(model)
    def post(self):
        try:
            input = request.json.values()
            builder = DatasetBuilder(
                name=input['datasetName'],
                data_type=input['datasetType'],
                classes=input['datasetClasses'],
                class_size=input['datasetClassSize'],
            ) 
            dataset = builder.get_data()
            response = jsonify({
                "statusCode": 200,
                "status": "Created Dataset!",
                "dataset": dataset,
            })
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except Exception as error:
            return jsonify({
                "statusCode": 500,
                "status": "Unable to Create Dataset",
                "error": str(error),
            })


    
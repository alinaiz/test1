from flask import Blueprint, render_template, jsonify, request, g

index = Blueprint('index', __name__, url_prefix='')
api = Blueprint('api', __name__, url_prefix='/api')


@index.route('/')
def root():
    return jsonify({'hello start': 334455}), 200


@api.route('/health')
def health():
    return jsonify([{'hello health': 985, 'hello health2': 654}]), 200


@api.route('/telemetry')
def telemetry():
    return jsonify({'hello telemetry': 123}), 200

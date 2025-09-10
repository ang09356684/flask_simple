"""
API v1 Blueprint
Provides RESTful API endpoints
"""

from flask import Blueprint, jsonify, request

# Create API Blueprint
api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def index():
    """
    Root endpoint - API information
    
    Returns:
        JSON: API information
    """
    return jsonify({
        'message': 'Flask API',
        'version': '1.0.0',
        'status': 'running',
        'endpoints': {
            'health': '/api/v1/health',
            'data': '/api/v1/data'
        }
    })


@api_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint
    
    Returns:
        JSON: Health status information
    """
    return jsonify({
        'status': 'healthy',
        'message': 'API is running',
        'version': '1.0.0'
    })



@api_bp.route('/data', methods=['POST'])
def create_data():
    """
    Create data endpoint - simplified version
    
    Request Body (JSON):
        {
            "name": "string"
        }
    
    Returns:
        JSON: Creation result
    """
    try:
        # Get JSON data
        data = request.get_json()
        
        # Check if name exists
        if not data or 'name' not in data:
            return jsonify({
                'error': 'Missing required field: name'
            }), 400
        
        # Get name
        name = data['name']
        
        return jsonify({
            'message': 'Data created successfully',
            'name': name,
            'status': 'created'
        }), 201
        
    except Exception as e:
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

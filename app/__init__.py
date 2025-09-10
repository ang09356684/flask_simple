"""
Flask Application Factory Pattern
Create and configure Flask application instance
"""

import logging
from flask import Flask, request, jsonify

from config import config

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")


def create_app(config_name='default'):
    """
    Application factory function
    
    Args:
        config_name (str): Configuration name ('development', 'production', 'testing', 'default')
    
    Returns:
        Flask: Configured Flask application instance
    """
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    
    # Register Blueprint
    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    # Request Logging
    @app.before_request
    def before_request():
        """Log request information"""
        logger.info(f'{request.method} {request.path}, '
                   f'args={request.args.to_dict()}, '
                   f'form={request.form.to_dict()}, '
                   f'data={request.get_json(silent=True)}')
    
    @app.after_request
    def after_request(response):
        """Log response information"""
        logger.info(f'Response: {request.method} {request.path}, {response.status_code}, '
                   f'data={response.get_data(as_text=True)[:200]}...' if len(response.get_data(as_text=True)) > 200 
                   else f'data={response.get_data(as_text=True)}')
        return response
    
    # Error handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    # Root route
    @app.route('/')
    def index():
        return jsonify({
            'message': 'Flask API',
            'version': '1.0.0',
            'status': 'running'
        })
    
    return app

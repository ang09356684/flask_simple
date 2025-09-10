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
    
    # Error handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500

    # Register Blueprint
    from app.api.api_v1 import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    
    
    return app

"""
Flask Application Entry Point
Load and register blueprints
"""

import logging
from flask import request
from app import create_app

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app")

# Create Flask application instance for WSGI
app = create_app()



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


if __name__ == '__main__':
    # Development environment startup
    app.run(host='0.0.0.0', port=5000, debug=True)


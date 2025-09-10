"""
Flask Application Entry Point
Load and register blueprints
"""

from app import create_app

# Create Flask application instance for WSGI
app = create_app()

if __name__ == '__main__':
    # Development environment startup
    app.run(host='0.0.0.0', port=5000, debug=True)


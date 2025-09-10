"""
Flask Configuration Settings
All parameters are written directly in the Config class, no environment variables used
"""

import os

class Config:
    """Basic configuration class"""
    
    # Flask basic settings
    SECRET_KEY = 'your-secret-key-change-in-production'
    DEBUG = False
    TESTING = False
    
    
    # API settings
    API_TITLE = 'Flask API'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'
    
    # Logging settings
    LOG_LEVEL = 'INFO'
    
    # Server settings
    HOST = '0.0.0.0'
    PORT = 5000

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True


# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}

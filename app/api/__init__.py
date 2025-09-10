"""
API Blueprint module
"""

from flask import Blueprint

# Create API Blueprint
api_bp = Blueprint('api', __name__)

# Import all API routes
from app.api import api_v1


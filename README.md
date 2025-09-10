# Flask Project

This is a Flask framework project template using application factory pattern with clean architecture separation.

## Project Structure

```
flask-project/
│  app.py               # Application entry point; loads and registers blueprints
│  config.py            # Configuration settings (all parameters directly in Config class)
│  pyproject.toml       # uv dependency management
│  README.md
│  .gitignore
│
├─app/
│  ├─__init__.py        # Application factory pattern
│  ├─api/               # API routes; each file is a blueprint
│  │  ├─__init__.py
│  │  └─api_v1.py       # Blueprint: /api/v1
│  │
│  ├─dao/               # Data access layer (DB I/O)
│  │  └─__init__.py
│  │
│  └─model/             # ORM models / schema
│     └─__init__.py
```

## Installation and Running

### Install dependencies using uv

```bash
# Install uv (if not already installed)
pip install uv

# Install project dependencies
uv sync

# Install development dependencies
uv sync --extra dev
```

### Start the application

#### Development environment
```bash
uv run python app.py
```

#### Production environment (Windows)
```bash
uv run waitress-serve --host=0.0.0.0 --port=5000 app:app
```

#### Production environment (Linux)
```bash
uv run gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## API Endpoints

- `GET /api/v1/health` - Health check endpoint

## Configuration

All configuration parameters are defined in `config.py`, supporting multiple environments:
- `development` - Development environment
- `production` - Production environment  
- `testing` - Testing environment

Note: This project does not include database functionality, focusing on API services.

## Logging

The application automatically logs all HTTP requests and responses, including:
- Request method, path, parameters
- Form data and JSON data
- Response status code and data

## Development

### Code formatting
```bash
uv run black .
```

### Code linting
```bash
uv run flake8 .
```

### Run tests
```bash
uv run pytest
```
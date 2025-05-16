# Saguaro - Task Management API

A robust and secure Task Management API built with FastAPI and PostgreSQL. The API provides a complete solution for managing tasks with features like task creation, retrieval, updating, and deletion.

## Features

- **RESTful API**: Built with FastAPI for high performance and automatic API documentation
- **Database**: PostgreSQL for reliable data storage
- **Async Operations**: Asynchronous database operations for better performance
- **API Documentation**: Interactive API documentation available at `/docs` endpoint
- **Security**: Production deployment secured with SSL/TLS
- **Scalability**: Multiple worker processes for handling concurrent requests

## Local Development Setup

The project uses Docker and Docker Compose for local development. Follow these steps to get started:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Saguaro
   ```

2. Create a `.env` file in the project root with the following variables:
   ```
   POSTGRES_USER=your_username
   POSTGRES_PASSWORD=your_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   POSTGRES_DB=saguaro
   ```

3. Start the application:
   ```bash
   docker-compose up -d
   ```

The application will be available at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

## Production Deployment

The project is deployed using a combination of:
- Systemd for process management
- Uvicorn as the ASGI server
- Nginx as the reverse proxy
- SSL/TLS for secure communication

### Deployment Components

1. **saguaro_uvicorn.service**
   - Systemd service file that manages the FastAPI application
   - Runs multiple worker processes for better performance
   - Automatically restarts on failure
   - Runs as a specific user for security

2. **saguaro_nginx.conf**
   - Nginx configuration for SSL termination and reverse proxy
   - Handles HTTP to HTTPS redirection
   - Configures SSL certificates and security headers
   - Manages proxy settings for the FastAPI application

### Deployment Steps

1. Set up the Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure Nginx:
   ```bash
   sudo cp saguaro_nginx.conf /etc/nginx/sites-available/saguaro
   sudo ln -s /etc/nginx/sites-available/saguaro /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

3. Set up the systemd service:
   ```bash
   sudo cp saguaro_uvicorn.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable saguaro_uvicorn
   sudo systemctl start saguaro_uvicorn
   ```

## Live Demo

The API is currently running at: [https://saguaro.alieskandari.online/docs/](https://saguaro.alieskandari.online/docs/)

## API Documentation

Once the application is running, you can access:
- Interactive API documentation: `/docs`
- Alternative API documentation: `/redoc`

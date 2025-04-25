# Task Management System (TMS)

## Overview
The Task Management System (TMS) is a backend system designed to manage tasks, projects, user requests, and user authentication and authorization. The system supports role-based access control and provides different functionalities based on user roles.

## Features

### User Management
- Create, read, update, and delete user records.
- Manage user roles (Admin, Project Manager, Project Lead, Developer, Client).

### Project Management
- Create, read, update, and delete projects.
- Assign users to projects.

### Task Management
- Create, read, update, and delete tasks.
- Assign tasks to projects and users.

### Comment Management
- Create, read, update, and delete comments.
- Tag comments to projects and tasks.

### Authentication and Authorization
- Token-based authentication using Django Rest Framework.
- Role-based access control for all CRUD operations.

## Setup Instructions

### Prerequisites
- Python 3.10 or later
- pip (Python package manager)
- Virtual environment tool (optional but recommended)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd django
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000`.

## API Endpoints

### User Endpoints
- `GET /users/`: List all users
- `POST /users/`: Create a new user
- `GET /users/{id}/`: Retrieve a specific user
- `PUT /users/{id}/`: Update a specific user
- `DELETE /users/{id}/`: Delete a specific user

### Project Endpoints
- `GET /projects/`: List all projects
- `POST /projects/`: Create a new project
- `GET /projects/{id}/`: Retrieve a specific project
- `PUT /projects/{id}/`: Update a specific project
- `DELETE /projects/{id}/`: Delete a specific project

### Task Endpoints
- `GET /tasks/`: List all tasks
- `POST /tasks/`: Create a new task
- `GET /tasks/{id}/`: Retrieve a specific task
- `PUT /tasks/{id}/`: Update a specific task
- `DELETE /tasks/{id}/`: Delete a specific task

### Comment Endpoints
- `GET /comments/`: List all comments
- `POST /comments/`: Create a new comment
- `GET /comments/{id}/`: Retrieve a specific comment
- `PUT /comments/{id}/`: Update a specific comment
- `DELETE /comments/{id}/`: Delete a specific comment

### Authentication Endpoints
- `POST /api/token/`: Obtain a token
- `POST /api/token/refresh/`: Refresh a token

## Testing
Run unit tests using the following command:
```bash
python manage.py test
```

## Non-Functional Requirements

### Scalability and Performance
- Use Django's caching framework to cache frequently accessed data.
- Implement pagination for list endpoints to handle large datasets efficiently.

### Error Handling
- Custom exception handling provides meaningful error messages.
- Appropriate HTTP status codes are returned for different error scenarios.

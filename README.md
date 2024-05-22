# Task Manager Web Application

## Introduction
This Task Manager web application is developed using Django and Django Rest Framework. It allows users to organize and track tasks, projects, users, task assignments, and comments, facilitating efficient task management and collaboration within teams.

## Key Features
- **Project Setup**: Create and configure a new Django project.
- **Database Configuration**: Use SQLite as the database for the project.
- **Models Definition**: Define models for projects, tasks, users, task assignments, and comments.
- **Admin Integration**: Integrate and customize the Django admin interface.
- **API Creation**: Build RESTful APIs using Django Rest Framework for CRUD operations.

## Skills Developed
By completing this assignment, the following skills are developed:
- Django project setup and configuration.
- Database modeling and management using Django models.
- Integration of the Django admin interface.
- Building RESTful APIs using Django Rest Framework.
- Serialization and deserialization with DRF serializers.
- Implementing CRUD operations for different models.
- Code documentation for clarity and maintainability.

## Project Setup
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd TaskManager
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the migrations to set up the database:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser for accessing the admin site:
    ```sh
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```sh
    python manage.py runserver
    ```

## Models Definition
The following models are defined in the project:
- **Project**: Fields for project name, description, start date, and end date.
- **Task**: Fields for task name, description, status (e.g., to-do, in progress, completed), priority, and deadline.
- **User**: Fields for user details such as username, email, and password.
- **TaskAssignment**: ForeignKey relationship with Task and User to assign tasks to users.
- **Comment**: Fields for commenter name, email, content, and task relationship.

## Admin Integration
Models are registered with the Django admin site in the `admin.py` file of the app. The admin interface is customized for better usability.

## API Creation
Using Django Rest Framework, CRUD APIs are created for managing projects, tasks, users, task assignments, and comments. Serializers and views are implemented for each model to handle CRUD operations, and endpoints are defined for creating, reading, updating, and deleting records.






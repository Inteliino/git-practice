
# Task Manager

Python task management application developed for the
Software Development and Maintenance Lifecycle course
at Vidzeme University of Applied Sciences.

## Project Overview

Task Manager is a command-line application written in Python.

The application uses SQLite to store tasks and demonstrates
Git version control, database migrations, automated testing,
and continuous integration with GitHub Actions.

## Features

- Create new tasks
- View all tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Assign task priorities: Low, Medium, High
- Filter tasks by status and priority
- View task statistics
- Calculate task completion percentage
- Save tasks permanently in SQLite

## Technologies

- Python 3
- SQLite
- Git and GitHub
- Python unittest
- GitHub Actions

## Project Structure

    git-practice/
    |
    |-- src/
    |   |-- main.py
    |   |-- tasks.py
    |   |-- database.py
    |   |-- statistics.py
    |
    |-- migrations/
    |   |-- 001_create_tasks.sql
    |   |-- 002_add_priority.sql
    |
    |-- tests/
    |   |-- test_tasks.py
    |
    |-- .github/
    |   |-- workflows/
    |       |-- tests.yml
    |
    |-- .gitignore
    |-- README.md

## Installation

Clone the repository:

    git clone https://github.com/Inteliino/git-practice.git

Open the project directory:

    cd git-practice

Python 3 is required. No additional Python packages are needed.

## Database Migrations

Run database migrations:

    python src/database.py

On Windows, you can also use:

    py src/database.py

The project contains two database migrations:

1. 001_create_tasks.sql - Creates the tasks table.
2. 002_add_priority.sql - Adds task priority support.

Applied migrations are recorded in the schema_migrations
table to prevent duplicate execution.

## Running the Application

Start the application:

    python src/main.py

On Windows:

    py src/main.py

## Application Menu

1. Add task
2. List tasks
3. Edit task
4. Delete task
5. Complete task
6. Filter tasks
7. Task statistics
8. Exit

## Automated Tests

The application uses Python's built-in unittest framework.

Run all automated tests:

    python -m unittest discover -s tests -v

The project includes five tests:

1. Task creation
2. Task editing
3. Task deletion
4. Task statistics
5. Invalid task priority validation

Tests use a temporary SQLite database to avoid modifying
real application data.

## Continuous Integration

GitHub Actions automatically executes database migrations
and automated tests when changes are pushed to the main
branch or a pull request targets main.

Workflow configuration:

    .github/workflows/tests.yml

The workflow performs the following steps:

1. Checkout repository
2. Set up Python
3. Check Python version
4. Run database migrations
5. Run automated tests

## Git Version Control

This project demonstrates:

- Git repository initialization
- Git commits and version history
- Branch creation and switching
- Merge operations
- Merge conflict resolution
- Git remote synchronization
- Gitignore configuration
- GitHub repository management

The repository contains at least 30 commits documenting
the development process.

## Course Requirements

- Minimum 30 Git commits
- At least 3 automated tests
- Automated workflow
- Database migrations

## Author

GitHub: Inteliino

Vidzeme University of Applied Sciences

## License

Educational project.
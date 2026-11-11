# 

# \# Task Manager

# 

# A Python task management application developed for the Software Development and Maintenance Lifecycle course at Vidzeme University of Applied Sciences.

# 

# \## Project Description

# 

# Task Manager is a command-line application that allows users to create, manage and track tasks.

# 

# The project demonstrates:

# \- Git version control

# \- Python programming

# \- SQLite database integration

# \- Database migrations

# \- Automated unit testing

# \- GitHub Actions CI automation

# 

# \## Features

# 

# \- Add new tasks

# \- View existing tasks

# \- Edit task titles

# \- Delete tasks

# \- Mark tasks as completed

# \- Assign task priorities (Low, Medium, High)

# \- Filter tasks by status and priority

# \- View task statistics

# \- Store tasks in an SQLite database

# 

# \## Technologies

# 

# \- Python 3

# \- SQLite

# \- Git and GitHub

# \- Python unittest

# \- GitHub Actions

# 

# \## Installation

# 

# Clone the repository:

# 

# ```bash

# git clone https://github.com/Inteliino/git-practice.git

# ```

# 

# Open the project directory:

# 

# ```bash

# cd git-practice

# ```

# 

# No additional Python packages are required.

# 

# \## Database Setup

# 

# Run database migrations:

# 

# ```bash

# python src/database.py

# ```

# 

# The application uses SQLite.

# 

# Database migrations are stored in the `migrations` directory:

# 

# \- `001\_create\_tasks.sql` - Creates the tasks table.

# \- `002\_add\_priority.sql` - Adds task priority support.

# 

# The migration system records applied migrations to avoid running them repeatedly.

# 

# \## Running the Application

# 

# Start the application:

# 

# ```bash

# python src/main.py

# ```

# 

# On Windows, you can also use:

# 

# ```bash

# py src/main.py

# ```

# 

# \## Application Menu

# 

# 1\. Add task

# 2\. List tasks

# 3\. Edit task

# 4\. Delete task

# 5\. Complete task

# 6\. Filter tasks

# 7\. Task statistics

# 8\. Exit

# 

# \## Automated Tests

# 

# The project uses Python's built-in unittest framework.

# 

# Run all tests:

# 

# ```bash

# python -m unittest discover -s tests -v

# ```

# 

# The tests cover:

# 

# 1\. Task creation

# 2\. Task editing

# 3\. Task deletion

# 4\. Task statistics

# 

# Tests use a temporary SQLite database to avoid modifying application data.

# 

# \## Continuous Integration

# 

# GitHub Actions automatically runs database migrations and automated tests.

# 

# The workflow is stored in:

# 

# `.github/workflows/tests.yml`

# 

# The workflow runs on pushes and pull requests targeting the `main` branch.

# 

# \## Git Version Control

# 

# The project demonstrates Git concepts such as:

# 

# \- Commits and version history

# \- Branch creation and switching

# \- Merge operations

# \- Merge conflict resolution

# \- Remote repository synchronization

# \- Gitignore configuration

# 

# \## Author

# 

# Student project - Vidzeme University of Applied Sciences

# 

# \## License

# 

# Educational project.

# 


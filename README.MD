
# 📝 To-Do List

A simple Django-based to-do list application that allows users to register, log in, and manage their personal tasks. Features include task creation, completion, deletion, and filtering based on status.

## Screenshots

Login Page:
![photo_1](/photos/login.png)

Register Page:
![photo_2](/photos/register.png)

Home Page:
![photo_3](/photos/home.png)

All active Task:
![photo_4](/photos/activ.png)

All completed task:
![photo_5](/photos/completed.png)


## Features

- User Authentication: Secure user registration and login system.
- Task Management: Create, complete, and delete tasks.
- Filtering: View all tasks, only active, or only completed tasks.
- Responsive UI: Clean and intuitive user interface.

## 🛠️ Technologies Used

- Backend: Django (Python)
- Database: Postgres (for development)
- Frontend: HTML, CSS (Bootstrap)
- Deployment: Render



## Installation

Clone the repository:

```bash
git clone https://github.com/SalanKatuwal/To-Do-List.git
cd To-Do-List
```
Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
Install dependencies:

```bash
pip install -r requirements.txt
```
Apply migrations:
```bash
python manage.py migrate
```
Run the development server:
```bash
python manage.py runserver
```
Access the application: Open your browser and navigate to 
```bash
http://127.0.0.1:8000/
```
## 🧪 Usage

- Register: Create a new account.

- Login: Access your personal task dashboard.

- Add Task: Enter a task title and submit.

- Complete Task: Click the ✅ icon next to a task.

- Delete Task: Click the 🗑 icon to remove a task.

- Filter Tasks: Use the filter buttons to view tasks by status.

## Deployment

The application is deployed on Render. To deploy your own version:

1. Create a render.yaml file in the project root with the following content:
```bash
services:
  - type: web
    name: todolist
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn core.wsgi:application
    envVars:
      - key: DEBUG
        value: False
      - key: SECRET_KEY
        generateValue: true

```
2. Push your code to GitHub.

3. Create a new Web Service on Render and connect your GitHub repository.

4. Set up environment variables and deploy.


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear messages.
4. Push your branch and create a pull request.

## Acknowledgments

- Thanks to the Django and Bootstrap communities for their excellent documentation and tools.
- Inspired by various to-do list applications for functionality and design ideas.
- Special thanks to all contributors and users for their support.
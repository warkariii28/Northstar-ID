# Northstar ID

Northstar ID is a beginner-friendly Flask authentication project.  
It shows how to build the basics of a user system: register, log in, log out, and store user data in a database.

## What this project teaches

- How a Flask app is structured
- How user registration works
- How login and logout work
- How passwords are hashed before storage
- How forms are validated
- How data is saved in SQLite using SQLAlchemy

## Features

- Create a new account
- Log in with an existing account
- Log out securely
- Password hashing with `Flask-Bcrypt`
- Form validation with `Flask-WTF` and `WTForms`
- User data stored in SQLite

## Tech used

- Python
- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-WTF
- Flask-Migrate
- SQLAlchemy
- SQLite

## Project structure

```text
Northstar-ID/
|-- app.py
|-- routes.py
|-- models.py
|-- forms.py
|-- manage.py
|-- requirements.txt
|-- templates/
|-- static/
|-- migrations/
```

## File explanation

- `app.py` creates and configures the Flask app
- `routes.py` contains page routes like login, register, home, and logout
- `models.py` defines the `User` database table
- `forms.py` contains the login and registration forms
- `manage.py` helps create and update the database
- `templates/` contains the HTML pages
- `static/` stores images and static assets

## How to run this project from scratch

### 1. Clone the repository

```bash
git clone https://github.com/warkariii28/User-Authentication.git
cd User-Authentication
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the database

```bash
python manage.py
```

### 6. Run the Flask app

#### Windows PowerShell

```powershell
$env:FLASK_APP="routes"
flask run
```

#### macOS/Linux

```bash
export FLASK_APP=routes
flask run
```

### 7. Open in browser

```text
http://127.0.0.1:5000/
```

## App routes

- `/` home page
- `/login/` login page
- `/register/` register page
- `/logout` logout route

## How authentication works here

1. A user registers with username, email, and password.
2. The password is hashed before saving to the database.
3. The user logs in with email and password.
4. Flask-Login keeps the user session active.
5. The user can log out to end the session.

## Beginner ideas to improve this project

- Add a profile page
- Add password reset
- Add email verification
- Add user roles like admin and normal user
- Move CSS into a separate file
- Add better flash messages and dashboard pages

## Author

Built and customized by Athar as a Flask authentication learning project.

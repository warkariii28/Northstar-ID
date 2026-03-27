# Northstar ID

Northstar ID is a customized Flask authentication starter that I reshaped from a basic login/signup example into a cleaner, more portfolio-friendly project.

## What changed

- Added a distinct product identity instead of leaving the app as a generic Flask auth demo
- Redesigned the landing page with a stronger visual style and clearer messaging
- Refreshed the login and registration screens so the project feels like a real app starter
- Kept the original authentication foundation simple and extendable

## Current features

- User registration
- User login
- Password hashing with `Flask-Bcrypt`
- Session handling with `Flask-Login`
- SQLite database with SQLAlchemy
- WTForms validation

## Project stack

- Flask
- Flask-Login
- Flask-Bcrypt
- Flask-Migrate
- Flask-WTF
- SQLAlchemy
- SQLite

## Run locally

1. Create a virtual environment

```bash
python -m venv venv
```

2. Activate it

```powershell
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create the database

```bash
python manage.py
```

5. Start the app

```powershell
$env:FLASK_APP="routes"
flask run
```

6. Open your browser

```text
http://127.0.0.1:5000/
```

## Main routes

- `/` for the landing page
- `/login/` for sign in
- `/register/` for account creation
- `/logout` to end the session

## Next ideas

- Add profile pages
- Add password reset
- Add email verification
- Add role-based access
- Move styling into a dedicated static CSS file

## Notes

This repo is now positioned as a customized auth starter, so if you publish it to GitHub, rename the repository and update the author details to match your own profile.

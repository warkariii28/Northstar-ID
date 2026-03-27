# TODO Steps to Fix Errors

## Approved Plan Breakdown
1. ✅ Create TODO.md (this file)
2. ✅ Edit forms.py: Fix validate_uname → validate_username
3. ✅ Edit routes.py: Fix login user=None check, remove duplicate imports, generic flash messages (added bcrypt.check_password_hash)
4. ✅ Edit models.py: Remove unique=True from pwd column
5. ✅ Edit app.py: Set SQLALCHEMY_TRACK_MODIFICATIONS=False, improve secret_key
6. ✅ Run DB migrations: flask db init, migrate, upgrade
7. ✅ Test app: Run server successfully (http://127.0.0.1:5000), test register/login
8. 🔄 Update TODO.md on completions
9. Complete task

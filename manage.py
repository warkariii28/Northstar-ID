
from pathlib import Path

from app import create_app, db


def deploy():
    """Create the database tables and initialize migrations once."""
    app = create_app()

    with app.app_context():
        db.create_all()

    migrations_dir = Path(__file__).resolve().parent / "migrations"
    if migrations_dir.exists() and any(migrations_dir.iterdir()):
        print("Database is ready. Existing migrations were kept.")
        return

    from flask_migrate import init, migrate, stamp, upgrade

    with app.app_context():
        init()
        stamp()
        migrate(message="Initial migration")
        upgrade()
        print("Database and migrations initialized.")


if __name__ == "__main__":
    deploy()

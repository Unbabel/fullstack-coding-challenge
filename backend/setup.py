from setuptools import find_packages, setup

setup(
    name="unbabel",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "python-dotenv",
        "flask_apscheduler",
        "flask_cors",
        "flask_migrate",
        "marshmallow_sqlalchemy",
        "requests",
        "psycopg2",
        "gunicorn"
    ],
)

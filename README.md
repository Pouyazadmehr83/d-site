# d-site

A learning Django web application focused on backend fundamentals and practical hands-on experience.

## Overview

This is a beginner-friendly Django project created to learn web backend development with Python and Django. The repo contains Django apps, templates, static assets (SCSS/CSS/JS), and example views showing models, forms, and admin usage.

## What is included
- Django project and one or more Django apps
- Python code (views, models, URLs)
- Templates and static files (SCSS/HTML/CSS/JS)

## Requirements
- Python 3.8+
- pip
- virtualenv (recommended)
- Node.js + npm or Dart Sass (if you want to compile SCSS locally)

## Installation (detailed)
1. Clone the repository:
   git clone https://github.com/Pouyazadmehr83/d-site.git
   cd d-site

2. Create and activate a virtual environment:
   # Linux / macOS
   python -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install Python dependencies (if requirements.txt exists):
   pip install -r requirements.txt
   
   If there is no requirements.txt, install Django and common deps:
   pip install django gunicorn psycopg2-binary

4. Configure environment variables (recommended):
   - SECRET_KEY: Django secret key
   - DEBUG: True (development) or False (production)
   - DATABASE_URL or configure DATABASES in settings.py

5. Apply migrations:
   python manage.py migrate

6. Create a superuser for admin access:
   python manage.py createsuperuser

7. (Optional) Compile SCSS to CSS:
   - If the project includes SCSS and a package.json, you may use npm scripts: npm install && npm run build
   - Or use Dart Sass directly: npx sass scss/:static/css/ --no-source-map --style=compressed

8. Collect static files (production):
   python manage.py collectstatic --noinput

9. Run the development server:
   python manage.py runserver 0.0.0.0:8000
   Open http://localhost:8000 in your browser.

## Running with Gunicorn (production example)
1. Ensure DEBUG=False and proper ALLOWED_HOSTS set.
2. Install gunicorn: pip install gunicorn
3. Run: gunicorn project_name.wsgi:application --bind 0.0.0.0:8000

## Database notes
- For development, SQLite works out of the box.
- For production, configure PostgreSQL/MySQL and update settings. Use environment variables for credentials.

## Tests
If the project includes tests, run:
   python manage.py test

## Contributing
- Fork the repository, create feature branches, add tests, and open a PR.

## License & Contact
Add a LICENSE file to clarify reuse.
Author: Pouyazadmehr83
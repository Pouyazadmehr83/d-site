# d-site

A production-minded blog application built with Django — designed for learning and demonstration of common blog features: user registration/login, post creation/editing, commenting, tagging, and search.

Repository: https://github.com/Pouyazadmehr83/d-site

## Project summary

d-site is a Django-based blogging platform created as a learning project. The code demonstrates a proper Django project structure, well-defined models, forms, views, and templates. Key user-facing features include:

- User accounts: registration, login/logout, password reset
- Post management: create, read, update, delete (CRUD) posts
- Drafts & publishing workflow (if implemented)
- Rich post metadata: tags and categories
- Commenting system with moderation controls (users can add comments)
- Full-text / basic search across posts
- Ability to create and edit posts, add tags, and search posts
- Responsive templates using SCSS/CSS and JavaScript
- Admin integration for site management

## Technologies

- Python 3.8+
- Django (see requirements.txt)
- SCSS / CSS / HTML / JavaScript for front-end
- Optional: PostgreSQL for production; SQLite for local development

## Requirements

- Git
- Python 3.8+
- pip
- virtualenv (recommended)
- Node.js + npm (optional — only if you need to compile SCSS locally)

## Installation — exact steps

1. Clone the repository
   git clone https://github.com/Pouyazadmehr83/d-site.git
   cd d-site

2. Create and activate a virtual environment
   # macOS / Linux
   python -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install Python dependencies
   pip install -r requirements.txt

   If requirements.txt is not present:
   pip install "django>=3.2" gunicorn psycopg2-binary django-environ django-crispy-forms

4. Configure environment variables
   Create a `.env` file or export environment variables. Example `.env`:
   SECRET_KEY=replace_with_secure_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1

   The project uses environment configuration (django-environ) — ensure settings.py reads from the `.env` or environment.

5. Apply database migrations
   python manage.py migrate

6. Create a superuser for admin and initial testing
   python manage.py createsuperuser
   # Follow prompts to set username/email/password

7. (Optional) Compile SCSS to CSS
   If SCSS is used and package.json contains build scripts:
   npm install
   npm run build
   Or with Dart Sass:
   npx sass scss/:static/css/ --no-source-map --style=compressed

8. Collect static files (production)
   python manage.py collectstatic --noinput

9. Run development server
   python manage.py runserver 0.0.0.0:8000
   Open http://localhost:8000

## Common management commands

- Make migrations:
  python manage.py makemigrations
- Apply migrations:
  python manage.py migrate
- Load demo fixtures (if provided):
  python manage.py loaddata fixtures/demo.json
- Run tests:
  python manage.py test

## Feature notes (as requested)

- Models: Post, Tag, Comment, Profile (or User extension) demonstrate relations and indexing for search.
- Comments: users can post comments on posts; moderation can be handled via admin.
- Posts: users can create and edit posts; posts support tagging and search.
- Search: initially implemented via ORM queries (icontains); can be upgraded to full-text search (Postgres) or external search engines.

## Contributing

- Fork → create a feature branch → open a pull request
- Include tests and update README if you add or change behavior

## License & Contact

- Add a LICENSE file (e.g., MIT) if you want to permit reuse.
- Author: Pouyazadmehr83

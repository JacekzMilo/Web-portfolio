# Web Portfolio

Personal portfolio built with **Django 3.2** showcasing my data-science projects and experiments.  
The site lists completed work, highlights the *next* upcoming project and provides an admin interface secured with **Two-Factor Authentication** (TOTP).

---

## ✨ Key Features
* Dynamic list of projects stored in the database (`landingpage.Project`)
* Sneak-peek section for the next planned project (`landingpage.NextProject`)
* Drag-and-drop ordering of projects in the Django admin via `django-admin-sortable2`
* Image uploads & media handling out of the box (`ImageField` + SQLite)
* Two-Factor Authentication for staff users (`django-two-factor-auth`)
* Production-ready: **Gunicorn** application server & static files served by **WhiteNoise**
* Fully containerised with **Docker** and **docker-compose**
* Automated CI/CD pipeline – GitHub Actions builds & deploys to a Raspberry Pi 5 (DEV & PROD)

---

## 🚀 Quick Start

### 1. Run with Docker (recommended)
```bash
# build & start the stack
docker compose up --build

# open in your browser
http://localhost:8000
```
This will:
1. Install all Python dependencies from `requirements.txt`.
2. Apply database migrations (the SQLite file is persisted on the host).
3. Launch Gunicorn on port 8000.

### 2. Run locally (without Docker)
```bash
python -m venv .venv && source .venv/bin/activate       # Linux/macOS
# on Windows: py -3 -m venv .venv && .venv\Scripts\activate

pip install -r requirements.txt
cp web_portfolio/.env.example web_portfolio/.env         # create & edit your secrets
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```
The site will be available at `http://127.0.0.1:8000`.

---

## ⚙️ Environment Variables
Define them in `web_portfolio/.env` or in container environment variables.

| Variable | Example | Description |
|----------|---------|-------------|
| `SECRET_KEY` | `django-insecure-CHANGE_ME` | Secret key used by Django to sign cookies |
| `DEBUG` | `1` | Enable/disable debug mode |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated list of allowed hosts |
| `HOST_PORT` | `8000` | Host port mapped to the container (docker-compose) |
| `DB_PATH` | `/absolute/path/db.sqlite3` | Path to SQLite database file persisted outside the container |

If you want to use PostgreSQL (e.g. in production) set a `DATABASE_URL` variable – it will be parsed by `dj-database-url`.

---

## 🗂️ Project Structure
```
├── landingpage/        # main portfolio app
│   ├── models.py       # Project & NextProject models
│   ├── views.py        # landing page, list, about views
│   ├── templates/      # HTML templates
│   └── static/         # app-specific images
├── web_portfolio/      # Django project configuration
│   ├── settings.py     # settings (reads .env)
│   ├── urls.py         # URL router
│   └── wsgi.py         # Gunicorn entry-point
├── static/             # global static files (CSS/JS/img)
├── docker-compose.yml  # docker-compose service definition
├── Dockerfile          # container build instructions
└── requirements.txt    # Python dependencies
```

---

## ⚡ Continuous Integration & Deployment

Every push to `master_dev` or a merged pull-request to `master` triggers a **GitHub Actions** workflow:

1. Checkout the repository on a GitHub runner.
2. Sync the code to the Raspberry Pi 5 over SSH + `rsync` (`dev` or `prod` folder, depending on branch).
3. Build/refresh Docker images and restart the stack (`docker compose up --build -d`).

Secrets such as SSH credentials & ports are stored in the repository’s encrypted **Secrets** section.

This provides fully automated, zero-downtime deployments directly to the device acting as a home server.

---

## 🛠️ Useful Commands
```bash
# create an admin user
python manage.py createsuperuser

# reload initial project data from JSON
auth python manage.py loaddata projects.json
```

---

## 📌 Roadmap / TODO
- [ ] Add unit and integration tests (pytest + django-test-plus)
- [ ] Fully responsive design (mobile-first)
- [ ] Serve images from a CDN (e.g. Cloudflare Images or S3)

---

## 📝 License
This project is released under the MIT License – see the **LICENSE** file for details.


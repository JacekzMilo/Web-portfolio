# Web Portfolio

## 📑 Table of Contents
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Roadmap](#roadmap)
- [Development Notes](#development-notes)
- [Project Structure](#project-structure)
- [CI/CD](#continuous-integration--deployment)
- [License](#license)

## Project Overview
This portfolio started more than five years ago as a single place to showcase all the experiments, side-projects and production-grade applications I built while shaping my career in IT. It began as a simple static site hosted on **Vercel**, but I quickly wanted to present more than a few screenshots.

The first milestone was rewriting the site in **Django** and deploying it to **Heroku**, which gave me a database and an admin panel where I could curate projects with ease. When Heroku moved to a paid model I decided to self-host: I bought a **Raspberry Pi 5**, containerised the stack with **Docker** and set up fully automated deployments via **GitHub Actions** (separate *dev* and *prod* environments).

The next natural step was integrating it with my private banking application **Bank_app**. After two-factor authentication I can now view the public portfolio and – in a protected area – analyse my personal expenses pulled from the bank API. The site is served behind **Cloudflare** on a sub-domain, with **Nginx** acting as a reverse proxy and handling TLS certificates.

The platform keeps evolving: every new side-project lands here as a dedicated entry with screenshots and a link to its repository, while the underlying infrastructure is continuously improved to follow industry best practices (CI/CD, monitoring, staging, etc.).

## Key Features
* Dynamic project directory (model `landingpage.Project`)
* "Coming soon" teaser section (`landingpage.NextProject`)
* Drag-and-drop ordering in Django admin (`django-admin-sortable2`)
* Two-Factor Authentication for staff accounts (`django-two-factor-auth`)
* Containerised with **Docker** and orchestrated via `docker-compose`
* Zero-touch deployments through **GitHub Actions** to a Raspberry Pi

## Tech Stack
* Backend: **Python 3.11**, **Django 3.2**, **Gunicorn**
* Frontend: **HTML/CSS + Bootstrap**, Django templates (planned migration to **React / Next.js**)
* Database: **SQLite** locally, **PostgreSQL** optionally in production
* CI/CD & Ops: **Docker**, **GitHub Actions**, **Nginx**, **Certbot**, **Cloudflare**
* Libraries: `django-two-factor-auth`, `django-admin-sortable2`

## Roadmap
* Migrate UI to **Next.js** + **Tailwind CSS**
* Split services into dedicated microservices (auth, projects, analytics)
* Add observability: **Prometheus** + **Grafana**
* Introduce unit & integration tests (pytest)
* Multi-region hosting with a replicated database

---

## Related Projects
- **[Bank_app](https://github.com/JacekzMilo/Bank_app)** – personal finance aggregator connected via single-sign-on.

---

## 📖 Development Notes
This repository contains the current consolidated version of the portfolio. Earlier iterations (static site, Heroku deployment, first Raspberry Pi setup) are tagged in Git for reference. The architecture remains intentionally straightforward — a Django application served by Gunicorn behind Nginx, all orchestrated with Docker Compose.

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

## 📝 License
This project is released under the MIT License – see the **LICENSE** file for details.

